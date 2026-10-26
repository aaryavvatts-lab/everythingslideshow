#!/usr/bin/env node
// to_pdf.mjs - export an HTML slide deck to a 16:9 PDF, one slide per page.
//
// Usage:
//   node to_pdf.mjs deck.html deck.pdf [--size 1920x1080] [--slides N] [--wait 600]
//                   [--slide-selector ".slide"] [--images]
//
// Default mode ("print") injects print CSS so every slide is shown, stacked, fully revealed and
// un-animated, with a page size equal to the slide stage, then asks Chrome to print it. Text stays
// selectable. The common traps it handles: Chrome defaults to Letter portrait, slides hidden by
// visibility/opacity, reveal animations that never ran, transforms that scale the stage.
//
// --images mode screenshots every slide by pressing the arrow key and joins the pictures into a PDF
// (needs Python 3 with Pillow). Always works, but the text is not selectable. Use it when print mode
// gives the wrong page count (the script prints a warning when it can tell).
//
// Exit codes: 0 ok, 1 page count does not match the slide count, 2 could not run.

import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { createRequire } from 'node:module';
import { execSync, spawnSync } from 'node:child_process';
import { pathToFileURL, fileURLToPath } from 'node:url';

const args = process.argv.slice(2);
const SELF = fileURLToPath(import.meta.url);
if (args.length < 2 || args.includes('-h') || args.includes('--help')) {
  console.log(fs.readFileSync(SELF, 'utf8').split('\n').slice(1, 20).join('\n').replace(/^\/\/ ?/gm, ''));
  process.exit(args.includes('-h') || args.includes('--help') ? 0 : 2);
}
const VALUE_FLAGS = ['--size', '--slides', '--wait', '--slide-selector'];
const opt = (name, def) => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : def; };
const positional = args.filter((a, i) => !a.startsWith('--') && !VALUE_FLAGS.includes(args[i - 1]));
const [src, dest] = positional;
const [W, H] = opt('--size', '1920x1080').split('x').map(Number);
const wait = Number(opt('--wait', '600'));
const selector = opt('--slide-selector', null);
const imagesMode = args.includes('--images');

function npmRoot() { try { return execSync('npm root -g', { stdio: ['ignore', 'pipe', 'ignore'] }).toString().trim(); } catch { return null; } }
function resolvePlaywright() {
  const g = npmRoot();
  const roots = [process.cwd(), path.dirname(SELF)];
  if (g) roots.push(g, path.join(g, '@playwright/cli/node_modules'));
  for (const root of roots) for (const pkg of ['playwright-core', 'playwright', '@playwright/test']) {
    try { return createRequire(path.join(root, 'x.js'))(pkg); } catch { /* next */ }
  }
  return null;
}
function findChrome() {
  const c = [process.env.CHROME_PATH, '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome', '/usr/bin/google-chrome', '/usr/bin/chromium', '/usr/bin/chromium-browser'].filter(Boolean);
  for (const p of c) if (fs.existsSync(p)) return p;
  const cache = path.join(os.homedir(), 'Library/Caches/ms-playwright');
  if (fs.existsSync(cache)) for (const d of fs.readdirSync(cache).filter((n) => n.startsWith('chromium-')).sort().reverse()) {
    for (const sub of ['chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing', 'chrome-mac/Chromium.app/Contents/MacOS/Chromium']) {
      const p = path.join(cache, d, sub); if (fs.existsSync(p)) return p;
    }
  }
  return null;
}

if (!src || !dest || !fs.existsSync(src)) { console.error('to_pdf: usage: node to_pdf.mjs deck.html deck.pdf'); process.exit(2); }

if (imagesMode) {
  const tmp = fs.mkdtempSync(path.join(os.tmpdir(), 'deck-pdf-'));
  const here = path.dirname(SELF);
  spawnSync('node', [path.join(here, 'render_deck.mjs'), src, '--out', tmp, '--size', `${W}x${H}`, '--wait', String(wait), ...(opt('--slides') ? ['--slides', opt('--slides')] : [])], { stdio: 'inherit' });
  const py = `
import sys,os,re
from PIL import Image
d,out=sys.argv[1],sys.argv[2]
files=sorted(f for f in os.listdir(d) if re.match(r'^s\\d+\\.png$',f))
ims=[Image.open(os.path.join(d,f)).convert('RGB') for f in files]
ims[0].save(out,save_all=True,append_images=ims[1:],resolution=144)
print('to_pdf: wrote %d pages (image mode, text not selectable) -> %s'%(len(ims),out))`;
  const r2 = spawnSync('python3', ['-c', py, tmp, path.resolve(dest)], { stdio: 'inherit' });
  fs.rmSync(tmp, { recursive: true, force: true });
  process.exit(r2.status === 0 ? 0 : 2);
}

const pw = resolvePlaywright();
if (!pw) { console.error('to_pdf: Playwright not found. Run: npm i -g playwright-core'); process.exit(2); }
const browser = await pw.chromium.launch({ headless: true, executablePath: findChrome() || undefined });
const page = await browser.newPage({ viewport: { width: W, height: H } });
await page.goto(pathToFileURL(path.resolve(src)).href, { waitUntil: 'load' });
await page.waitForTimeout(wait);
await page.evaluate(() => (document.fonts ? document.fonts.ready : null));

const sel = selector || await page.evaluate(() => {
  for (const s of ['.slide', '[data-slide]', '.reveal .slides > section', 'section']) if (document.querySelectorAll(s).length > 1) return s;
  return null;
});
const expected = opt('--slides') ? Number(opt('--slides')) : (sel ? await page.evaluate((s) => document.querySelectorAll(s).length, sel) : 0);

await page.addStyleTag({ content: `
@page { size: ${W}px ${H}px; margin: 0; }
@media print {
  html, body { margin: 0 !important; padding: 0 !important; background: none; width: ${W}px !important; height: auto !important; overflow: visible !important; }
  *, *::before, *::after { animation: none !important; transition: none !important; }
  ${sel ? `${sel} { position: relative !important; inset: auto !important; display: block !important; visibility: visible !important; opacity: 1 !important; transform: none !important; width: ${W}px !important; height: ${H}px !important; min-height: ${H}px !important; max-height: ${H}px !important; overflow: hidden !important; page-break-after: always; break-after: page; page-break-inside: avoid; break-inside: avoid; margin: 0 !important; }` : ''}
  [class*="reveal"], [class*="fragment"], [data-reveal], [data-step], .r, .anim, .fade, .stagger > * { opacity: 1 !important; visibility: visible !important; transform: none !important; }
}` });
await page.emulateMedia({ media: 'print' });
await page.pdf({ path: path.resolve(dest), width: `${W}px`, height: `${H}px`, printBackground: true, margin: { top: 0, right: 0, bottom: 0, left: 0 }, preferCSSPageSize: true });
await browser.close();

// count pages without extra dependencies: count "/Type /Page" objects (not "/Pages")
const raw = fs.readFileSync(path.resolve(dest), 'latin1');
const pages = (raw.match(/\/Type\s*\/Page(?![s])/g) || []).length;
console.log(`to_pdf: ${pages} pages -> ${path.resolve(dest)} (print mode, text selectable)`);
if (expected && pages !== expected) {
  console.log(`to_pdf: WARNING expected ${expected} pages (one per slide) but got ${pages}. Check the PDF, or re-run with --images, or pass --slide-selector for your slide element.`);
  process.exit(1);
}
process.exit(0);
