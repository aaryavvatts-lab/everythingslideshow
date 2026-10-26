#!/usr/bin/env python3
"""render_static.py - turn a .pptx or .pdf into one PNG per slide so you can look at it.

Usage:
  python3 render_static.py deck.pptx --out qc/ [--dpi 110]
  python3 render_static.py deck.pdf  --out qc/

How it renders, best first:
  .pdf   PyMuPDF (pip install pymupdf), else pdftoppm.
  .pptx  1. LibreOffice (soffice) -> PDF -> PNGs. Most faithful, works on any OS.
         2. macOS QuickLook (qlmanage), one slide at a time. Substitutes fonts and does not draw
            charts, so say so in the report when you rely on it.
         3. Nothing available: exits with code 3 and tells you what to install.

Writes s01.png, s02.png ... into --out. Exit code 0 = ok, 2 = bad input, 3 = no renderer.
"""
import os
import re
import shutil
import subprocess
import sys
import tempfile
import zipfile


def arg(name, default=None):
    a = sys.argv
    return a[a.index(name) + 1] if name in a else default


def pdf_to_pngs(pdf, out, dpi):
    try:
        import fitz  # PyMuPDF
        doc = fitz.open(pdf)
        for i, page in enumerate(doc, 1):
            page.get_pixmap(dpi=dpi).save(os.path.join(out, f"s{i:02d}.png"))
        return len(doc)
    except ImportError:
        pass
    if shutil.which("pdftoppm"):
        subprocess.run(["pdftoppm", "-r", str(dpi), "-png", pdf, os.path.join(out, "p")], check=True)
        files = sorted(f for f in os.listdir(out) if f.startswith("p-") and f.endswith(".png"))
        for i, f in enumerate(files, 1):
            os.rename(os.path.join(out, f), os.path.join(out, f"s{i:02d}.png"))
        return len(files)
    return None


def pptx_via_soffice(pptx, out, dpi):
    soffice = shutil.which("soffice") or shutil.which("libreoffice") or "/Applications/LibreOffice.app/Contents/MacOS/soffice"
    if not os.path.exists(soffice) and not shutil.which(soffice):
        return None
    with tempfile.TemporaryDirectory() as td:
        subprocess.run([soffice, "--headless", "--convert-to", "pdf", "--outdir", td, pptx], check=True,
                       stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL, timeout=240)
        pdf = os.path.join(td, os.path.splitext(os.path.basename(pptx))[0] + ".pdf")
        if not os.path.exists(pdf):
            return None
        return pdf_to_pngs(pdf, out, dpi)


def pptx_via_quicklook(pptx, out):
    if sys.platform != "darwin" or not shutil.which("qlmanage"):
        return None
    z = zipfile.ZipFile(pptx)
    pres = z.read("ppt/presentation.xml").decode("utf8")
    ids = re.findall(r"<p:sldId [^>]*/>", pres)
    count = 0
    with tempfile.TemporaryDirectory() as td:
        for k, keep in enumerate(ids, 1):
            new = re.sub(r"(<p:sldIdLst>).*?(</p:sldIdLst>)", lambda m: m.group(1) + keep + m.group(2), pres, flags=re.S)
            one = os.path.join(td, f"s{k:02d}.pptx")
            with zipfile.ZipFile(one, "w", zipfile.ZIP_DEFLATED) as o:
                for it in z.infolist():
                    data = z.read(it.filename)
                    if it.filename == "ppt/presentation.xml":
                        data = new.encode("utf8")
                    o.writestr(it.filename, data)
            try:
                subprocess.run(["qlmanage", "-t", "-s", "1600", "-o", td, one], capture_output=True, timeout=45)
            except subprocess.TimeoutExpired:
                # QuickLook can hang without a desktop session; give up and let the next renderer try
                subprocess.run(["pkill", "-f", "qlmanage -t"], capture_output=True)
                return None
            png = one + ".png"
            if os.path.exists(png):
                shutil.move(png, os.path.join(out, f"s{k:02d}.png"))
                count += 1
    return count


def pptx_via_pillow(pptx, out):
    """Last resort: draw an APPROXIMATE preview from the PPTX data (boxes, text, pictures).

    Good enough to spot overlap, crowding, off-slide shapes and empty slides. It does not match
    real fonts, charts, gradients or effects, so never use it to judge polish."""
    try:
        from PIL import Image, ImageDraw, ImageFont
        from pptx import Presentation
        from pptx.enum.shapes import MSO_SHAPE_TYPE
        from pptx.dml.color import RGBColor
    except ImportError:
        return None
    prs = Presentation(pptx)
    scale = 1600.0 / prs.slide_width
    font_paths = ["/System/Library/Fonts/Helvetica.ttc", "/Library/Fonts/Arial.ttf",
                  "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", "C:/Windows/Fonts/arial.ttf"]
    font_path = next((p for p in font_paths if os.path.exists(p)), None)

    def font(pt):
        px = max(8, int(pt * 12700 * scale))
        try:
            return ImageFont.truetype(font_path, px) if font_path else ImageFont.load_default()
        except Exception:
            return ImageFont.load_default()

    def wrap(draw, text, fnt, width):
        lines = []
        for para in text.split("\n"):
            cur = ""
            for word in para.split(" "):
                trial = (cur + " " + word).strip()
                if draw.textlength(trial, font=fnt) <= width or not cur:
                    cur = trial
                else:
                    lines.append(cur)
                    cur = word
            lines.append(cur)
        return lines

    n = 0
    for k, slide in enumerate(prs.slides, 1):
        W, H = 1600, int(prs.slide_height * scale)
        bg = (255, 255, 255)
        for holder in (slide, slide.slide_layout, slide.slide_layout.slide_master):
            try:
                if holder.background.fill.type == 1:
                    c = holder.background.fill.fore_color.rgb
                    bg = (c[0], c[1], c[2])
                    break
            except Exception:
                continue
        im = Image.new("RGB", (W, H), bg)
        d = ImageDraw.Draw(im)
        for sp in slide.shapes:
            if sp.left is None or sp.width is None:
                continue
            x, y = int(sp.left * scale), int(sp.top * scale)
            w, h = int(sp.width * scale), int(sp.height * scale)
            if getattr(sp, "has_table", False) and sp.has_table:
                tbl = sp.table
                cy = y
                for row in tbl.rows:
                    rh = int(row.height * scale)
                    cx = x
                    for ci, cell in enumerate(row.cells):
                        cw = int(tbl.columns[ci].width * scale)
                        d.rectangle([cx, cy, cx + cw, cy + rh], outline=(150, 150, 150))
                        try:
                            if cell.fill.type == 1:
                                c = cell.fill.fore_color.rgb
                                d.rectangle([cx + 1, cy + 1, cx + cw - 1, cy + rh - 1], fill=(c[0], c[1], c[2]))
                        except Exception:
                            pass
                        size = next((r.font.size.pt for p in cell.text_frame.paragraphs for r in p.runs if r.font.size), 14)
                        fnt = font(size)
                        ty = cy + 3
                        for line in wrap(d, cell.text, fnt, max(cw - 10, 20)):
                            d.text((cx + 5, ty), line, fill=(30, 30, 30), font=fnt)
                            ty += int(size * 12700 * scale * 1.25)
                        cx += cw
                    cy += rh
                continue
            if sp.shape_type == MSO_SHAPE_TYPE.PICTURE:
                try:
                    import io
                    pic = Image.open(io.BytesIO(sp.image.blob)).convert("RGB").resize((max(w, 1), max(h, 1)))
                    im.paste(pic, (x, y))
                except Exception:
                    d.rectangle([x, y, x + w, y + h], outline=(180, 0, 0))
                continue
            is_oval = False
            try:
                from pptx.enum.shapes import MSO_SHAPE
                is_oval = sp.shape_type == MSO_SHAPE_TYPE.AUTO_SHAPE and sp.auto_shape_type == MSO_SHAPE.OVAL
            except Exception:
                pass
            fill_rgb = None
            try:
                if sp.fill.type == 1:
                    rgb = sp.fill.fore_color.rgb
                    fill_rgb = (rgb[0], rgb[1], rgb[2])
            except Exception:
                pass
            line_rgb, line_w = None, 1
            try:
                if sp.line.fill.type == 1 and sp.line.width and sp.line.width > 0:
                    lc = sp.line.color.rgb
                    line_rgb = (lc[0], lc[1], lc[2])
                    line_w = max(1, int(sp.line.width * scale))
            except Exception:
                pass
            if fill_rgb or line_rgb:
                if is_oval:
                    d.ellipse([x, y, x + w, y + h], fill=fill_rgb, outline=line_rgb, width=line_w)
                else:
                    try:
                        d.rounded_rectangle([x, y, x + w, y + h], radius=6, fill=fill_rgb, outline=line_rgb, width=line_w)
                    except Exception:
                        d.rectangle([x, y, x + w, y + h], fill=fill_rgb, outline=line_rgb, width=line_w)
            if sp.has_text_frame and sp.text_frame.text.strip():
                cy = y + 4
                for para in sp.text_frame.paragraphs:
                    size = next((r.font.size.pt for r in para.runs if r.font.size), 18)
                    color = (30, 30, 30)
                    try:
                        c = next((r.font.color.rgb for r in para.runs if r.font.color and r.font.color.type == 1), None)
                        if c is not None:
                            color = (c[0], c[1], c[2])
                    except Exception:
                        pass
                    fnt = font(size)
                    for line in wrap(d, para.text, fnt, max(w - 12, 20)):
                        d.text((x + 6, cy), line, fill=color, font=fnt)
                        cy += int(size * 12700 * scale * 1.25)
        im.save(os.path.join(out, f"s{k:02d}.png"))
        n += 1
    return n


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(__doc__)
        return 2
    src = sys.argv[1]
    out = arg("--out", "qc")
    dpi = int(arg("--dpi", "110"))
    if not os.path.exists(src):
        print(f"render_static: {src} not found")
        return 2
    os.makedirs(out, exist_ok=True)
    ext = os.path.splitext(src)[1].lower()
    n = None
    method = ""
    if ext == ".pdf":
        n, method = pdf_to_pngs(src, out, dpi), "pdf"
    elif ext == ".pptx":
        n, method = pptx_via_soffice(src, out, dpi), "libreoffice"
        if n is None:
            n, method = pptx_via_quicklook(src, out), "quicklook (fonts substituted, charts not drawn)"
        if not n:
            n, method = pptx_via_pillow(src, out), (
                "APPROXIMATE preview. No real renderer worked (LibreOffice missing, QuickLook "
                "unavailable or timed out). It draws text boxes, solid fills, solid slide backgrounds, "
                "tables and pictures only. It does NOT draw charts, gradients, picture backgrounds, "
                "shadows or real fonts, so a blank area may be a drawing gap, not a real fault. "
                "Do not judge polish from it")
    else:
        print("render_static: give a .pptx or .pdf")
        return 2
    if not n:
        print("render_static: no renderer found. Install one of: LibreOffice (brew install --cask libreoffice), "
              "PyMuPDF (pip3 install pymupdf) for PDFs, or use macOS for QuickLook.")
        return 3
    print(f"render_static: {n} slides via {method} -> {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
