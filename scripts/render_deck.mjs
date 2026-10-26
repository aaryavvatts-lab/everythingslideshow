#!/usr/bin/env node
// render_deck.mjs - screenshot every slide of an HTML deck and flag layout problems.
//
// Usage:
//   node render_deck.mjs deck.html --out qc/ [--size 1920x1080] [--mode keys|scroll]
//                        [--slides N] [--key ArrowRight] [--min-font 18] [--wait 400]
//
// What it does
//   1. Opens the deck in headless Chrome at the given size (default 1920x1080).
//   2. Steps through the slides (keys mode presses a key between shots; scroll mode
//      scrolls one viewport per shot). Slide count comes from --slides, or is detected
//      from .slide / [data-slide] / section, or by stepping until the picture stops changing.
//   3. Writes s01.png, s02.png ... and qc.json into --out.
//   4. For every slide it records: elements that spill outside the viewport, text boxes whose
//      content is taller than the box, the smallest visible font size, broken images,
//      console errors and failed requests.
//
// Exit code: 0 = clean, 1 = at least one FAIL (overflow, broken image, console error), 2 = could not run.
// Needs Node 18+ and playwright-core with a Chrome or Chromium. See resolvePlaywright().

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import crypto from 'node:crypto';
import { createRequire } from 'node:module';
import { execSync } from 'node:child_process';
import { pathToFileURL, fileURLToPath } from 'node:url';

const args = process.argv.slice(2);
const SELF = fileURLToPath(import.meta.url);
if (!args.length || args.includes('-h') || args.includes('--help')) {
  console.log(fs.readFileSync(SELF, 'utf8').split('\n').slice(1, 20).join('\n').replace(/^\/\/ ?/gm, ''));
  process.exit(args.length ? 0 : 2);
}
const VALUE_FLAGS = ['--out', '--size', '--mode', '--slides', '--key', '--min-font', '--wait'];
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : def; };
const file = args.find((a, i) => !a.startsWith('--') && !VALUE_FLAGS.includes(args[i - 1]));
const outDir = path.resolve(opt('--out', 'qc'));
const [W, H] = opt('--size', '1920x1080').split('x').map(Number);
const mode = opt('--mode', 'keys');
const key = opt('--key', 'ArrowRight');
const minFont = Number(opt('--min-font', '18'));
const wait = Number(opt('--wait', '400'));
const fixedCount = opt('--slides') ? Number(opt('--slides')) : null;

function npmRoot() {
  try { return execSync('npm root -g', { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim(); } catch { return null; }
}
function resolvePlaywright() {
  const g = npmRoot();
  const roots = [process.cwd(), path.dirname(SELF)];
  if (g) roots.push(g, path.join(g, '@playwright/cli/node_modules'));
  for (const root of roots) {
    for (const pkg of ['playwright-core', 'playwright', '@playwright/test']) {
      try { return createRequire(path.join(root, 'x.js'))(pkg); } catch { /* try next */ }
    }
  }
  return null;
}
function findChrome() {
  const cands = [
    process.env.CHROME_PATH,
    '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser',
    'C:/Program Files/Google/Chrome/Application/chrome.exe',
  ].filter(Boolean);
  for (const c of cands) if (fs.existsSync(c)) return c;
  const cache = path.join(os.homedir(), 'Library/Caches/ms-playwright');
  if (fs.existsSync(cache)) {
    for (const d of fs.readdirSync(cache).filter((n) => n.startsWith('chromium-')).sort().reverse()) {
      for (const sub of ['chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing', 'chrome-mac/Chromium.app/Contents/MacOS/Chromium']) {
        const p = path.join(cache, d, sub); if (fs.existsSync(p)) return p;
      }
    }
  }
  return null;
}

if (!file || !fs.existsSync(file)) { console.error('render_deck: give an existing .html file'); process.exit(2); }
const pw = resolvePlaywright();
if (!pw) { console.error('render_deck: Playwright not found. Run: npm i -g playwright-core   (and install Chrome, or: npx playwright install chromium)'); process.exit(2); }
const exe = findChrome();
fs.mkdirSync(outDir, { recursive: true });

// Runs inside the page. Kept free of closures over Node variables.
const probe = () => {
  const vw = window.innerWidth, vh = window.innerHeight;
  const visible = (el) => {
    const cs = getComputedStyle(el);
    if (cs.visibility === 'hidden' || cs.display === 'none' || Number(cs.opacity) < 0.05) return false;
    const r = el.getBoundingClientRect();
    return r.width > 1 && r.height > 1;
  };
  const issues = []; let smallest = 999; let words = 0;
  for (const el of document.body.querySelectorAll('*')) {
    if (!visible(el)) continue;
    const r = el.getBoundingClientRect();
    const tag = el.tagName.toLowerCase();
    if (['script', 'style', 'noscript'].includes(tag)) continue;
    const label = tag + (el.id ? '#' + el.id : '') + (typeof el.className === 'string' && el.className.trim() ? '.' + el.className.trim().split(/\s+/).slice(0, 2).join('.') : '');
    const hasText = [...el.childNodes].some((n) => n.nodeType === 3 && n.textContent.trim());
    const outside = r.right > vw + 2 || r.bottom > vh + 2 || r.left < -2 || r.top < -2;
    if (outside && (hasText || ['img', 'svg', 'canvas', 'video'].includes(tag))) {
      issues.push({ kind: 'outside-viewport', el: label, rect: [Math.round(r.left), Math.round(r.top), Math.round(r.right), Math.round(r.bottom)] });
    }
    if (hasText) {
      const cs = getComputedStyle(el);
      const size = parseFloat(cs.fontSize);
      if (size < smallest) smallest = size;
      words += [...el.childNodes].filter((n) => n.nodeType === 3).map((n) => n.textContent.trim().split(/\s+/).filter(Boolean).length).reduce((a, b) => a + b, 0);
      if (['hidden', 'auto', 'scroll'].includes(cs.overflowY) && el.scrollHeight > el.clientHeight + 4)
        issues.push({ kind: 'text-clipped', el: label, scrollH: el.scrollHeight, clientH: el.clientHeight });
    }
    if (tag === 'img') {
      if (!el.complete || el.naturalWidth === 0) issues.push({ kind: 'broken-image', el: label, src: el.currentSrc || el.src });
      else if (!el.getAttribute('alt') && el.getAttribute('role') !== 'presentation') issues.push({ kind: 'missing-alt', el: label, severity: 'warn' });
    }
  }
  const de = document.documentElement;
  const scrollsX = Math.max(de.scrollWidth, document.body.scrollWidth) > vw + 2;
  const visuals = [...document.querySelectorAll('img,svg,canvas,video')].filter(visible).length;
  const stillRunning = document.getAnimations().filter((a) => a.playState === 'running').length;
  return { smallestFont: smallest === 999 ? null : Math.round(smallest * 10) / 10, words, visuals, stillRunning, issues, scrollsX };
};

const browser = await pw.chromium.launch({ headless: true, executablePath: exe || undefined });
const page = await browser.newPage({ viewport: { width: W, height: H } });
const consoleErrors = []; const failed = [];
page.on('console', (m) => { if (m.type() === 'error') consoleErrors.push(m.text()); });
page.on('pageerror', (e) => consoleErrors.push(String(e)));
page.on('requestfailed', (r) => failed.push(r.url().slice(0, 140)));
await page.goto(pathToFileURL(path.resolve(file)).href, { waitUntil: 'load' });
await page.waitForTimeout(wait + 600);
await page.evaluate(() => (document.fonts ? document.fonts.ready : null));

let count = fixedCount;
if (!count) {
  count = await page.evaluate(() => {
    for (const s of ['.slide', '[data-slide]', '.reveal .slides > section', 'section']) {
      const n = document.querySelectorAll(s).length;
      if (n > 1) return n;
    }
    return 0;
  });
}
const auto = !count; if (auto) count = 120;

const slides = []; let lastHash = null; let repeats = 0;
for (let i = 1; i <= count; i++) {
  if (i > 1) {
    if (mode === 'scroll') await page.evaluate((h) => window.scrollBy(0, h), H);
    else {
      await page.keyboard.press(key);
      // Arrow keys also scroll a page that overflows sideways; undo that so each slide is judged on its own.
      await page.evaluate(() => window.scrollTo(0, 0));
    }
    await page.waitForTimeout(wait);
  }
  // Staggered reveals and CSS transitions are animations; wait for them so we do not photograph a half-drawn slide.
  await page.evaluate(() => Promise.race([
    Promise.all(document.getAnimations().map((a) => a.finished.catch(() => null))),
    new Promise((r) => setTimeout(r, 4000)),
  ]));
  await page.waitForTimeout(150);
  const png = path.join(outDir, `s${String(i).padStart(2, '0')}.png`);
  const buf = await page.screenshot({ path: png });
  const hash = crypto.createHash('md5').update(buf).digest('hex');
  if (hash === lastHash) {
    repeats++;
    if (auto && repeats >= 1) { fs.unlinkSync(png); break; }
  } else repeats = 0;
  lastHash = hash;
  const res = await page.evaluate(probe);
  slides.push({ n: i, image: path.basename(png), ...res, sameAsPrevious: repeats > 0 });
}
await browser.close();

const fails = []; const warns = [];
for (const s of slides) {
  for (const it of s.issues) (it.severity === 'warn' ? warns : fails).push(`slide ${s.n}: ${it.kind} ${it.el}${it.src ? ' ' + it.src.slice(0, 80) : ''}`);
  if (s.scrollsX && !fails.some((f) => f.includes('scrolls sideways')))
    fails.push(`from slide ${s.n}: the page scrolls sideways (something, maybe on a hidden slide, is wider than the stage); arrow keys will scroll the page`);
  if (s.smallestFont !== null && s.smallestFont < minFont) warns.push(`slide ${s.n}: smallest font ${s.smallestFont}px (< ${minFont}px at ${W}px wide)`);
  if (s.words > 90) warns.push(`slide ${s.n}: ${s.words} words, probably too dense for a spoken deck`);
  if (s.words < 2 && s.visuals === 0) warns.push(`slide ${s.n}: looks empty (almost no text and no image, svg or canvas). A reveal may not have played; try a larger --wait`);
  if (s.stillRunning > 0) warns.push(`slide ${s.n}: ${s.stillRunning} animation(s) still running at capture; the picture may be mid-motion (endless loops are normal)`);
  if (s.sameAsPrevious) warns.push(`slide ${s.n}: looks identical to the previous slide (navigation key may not be working)`);
}
consoleErrors.forEach((e) => fails.push('console error: ' + e.slice(0, 160)));
failed.forEach((u) => fails.push('request failed: ' + u));
// Collapse identical messages that differ only by slide number ("slide 2: x", "slide 3: x" -> "slides 2, 3: x").
const collapse = (list) => {
  const groups = new Map();
  for (const m of list) {
    const mt = m.match(/^slide (\d+): (.*)$/);
    if (!mt) { groups.set(m, null); continue; }
    if (!groups.has(mt[2])) groups.set(mt[2], []);
    groups.get(mt[2])?.push(mt[1]);
  }
  return [...groups].map(([msg, ns]) => (ns === null ? msg : ns.length === 1 ? `slide ${ns[0]}: ${msg}` : `slides ${ns.join(', ')}: ${msg}`));
};
const failsOut = collapse(fails); const warnsOut = collapse(warns);
const report = { file: path.resolve(file), size: [W, H], slides: slides.length, fails: failsOut, warns: warnsOut, perSlide: slides };
fs.writeFileSync(path.join(outDir, 'qc.json'), JSON.stringify(report, null, 2));
console.log(`render_deck: ${slides.length} slides -> ${outDir}`);
console.log(`FAIL ${failsOut.length}  WARN ${warnsOut.length}`);
failsOut.slice(0, 40).forEach((f) => console.log('  FAIL ' + f));
warnsOut.slice(0, 40).forEach((w) => console.log('  WARN ' + w));
console.log('  NOTE this script does not check overlap between elements, colour contrast or invisible SVG strokes. Look at the pictures (contact_sheet.py) for those.');
process.exit(failsOut.length ? 1 : 0);
