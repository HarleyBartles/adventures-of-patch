#!/usr/bin/env python3
"""Deterministic build for the 'Introducing Patch' one-pager.

The single generated source image (the 16:9 desktop base) is reused for both
formats. The desktop final uses the base directly. The mobile final crops Patch
out of the base with a Pillow flood-fill mask and places the cut-out on a
portrait canvas.
"""

from __future__ import annotations

import json
import math
import subprocess
import sys
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PKG = ROOT / "published" / "misc" / "introducing-patch"
SRC = PKG / "source_images"

BG = (247, 244, 236)
DARK = (29, 43, 58)
TEAL = (14, 141, 132)
WHITE = (255, 255, 255)

CARDS = [
    ("Who am I?", "A friendly autonomous software agent."),
    ("What do I do?", "Turn agentic workflow ideas into small, followable stories."),
    ("How do I learn?", "One clear next step at a time."),
]

FOOTER = (
    "Adventures of Patch and Patch and related characters are reserved. "
    "Images are CC BY-ND 4.0: free to share and inspect, not to modify or derive without permission."
)


def load_font(style: str, size: int) -> ImageFont.FreeTypeFont:
    family = {
        "regular": r"C:\Windows\Fonts\arial.ttf",
        "bold": r"C:\Windows\Fonts\arialbd.ttf",
    }
    return ImageFont.truetype(family.get(style, family["regular"]), size)


def wrap_text(text: str, font: ImageFont.FreeTypeFont, max_width: int) -> list[str]:
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if font.getlength(trial) <= max_width:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines


def draw_rounded_card(draw: ImageDraw.ImageDraw, xy, radius=20, fill=WHITE, outline=DARK, width=2):
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_text_block(draw, text, font, x, y, max_width, color=DARK, line_spacing=6) -> int:
    for line in wrap_text(text, font, max_width):
        draw.text((x, y), line, font=font, fill=color)
        y += font.size + line_spacing
    return y


def _extract_patch(base: Image.Image) -> Image.Image:
    """Return the base with only Patch (and props) opaque and the rest transparent."""
    rgba = base.convert("RGBA")
    mask = Image.new("L", base.size, 255)
    work = base.convert("RGB").copy()

    # Flood fill the background from each corner with a sentinel colour.
    w, h = work.size
    ImageDraw.floodfill(work, (0, 0), value=(0, 255, 0), thresh=50)
    ImageDraw.floodfill(work, (w - 1, 0), value=(0, 255, 0), thresh=50)
    ImageDraw.floodfill(work, (0, h - 1), value=(0, 255, 0), thresh=50)
    ImageDraw.floodfill(work, (w - 1, h - 1), value=(0, 255, 0), thresh=50)

    # Any pixel that is now (0, 255, 0) is background and becomes transparent.
    work_rgba = work.convert("RGBA")
    pixels = work_rgba.load()
    mask_data = mask.load()
    for y in range(h):
        for x in range(w):
            if pixels[x, y][:3] == (0, 255, 0):
                mask_data[x, y] = 0

    cutout = rgba.copy()
    cutout.putalpha(mask)
    return cutout


def _background_sample(image: Image.Image) -> tuple[int, int, int]:
    corners = [
        image.getpixel((0, 0)),
        image.getpixel((image.width - 1, 0)),
        image.getpixel((0, image.height - 1)),
        image.getpixel((image.width - 1, image.height - 1)),
    ]
    return tuple(int(round(sum(c[i] for c in corners) / len(corners))) for i in range(3))


def _tight_bbox(image: Image.Image) -> tuple[int, int, int, int]:
    alpha = image.getchannel("A")
    return alpha.getbbox()


def build_desktop() -> Path:
    canvas = Image.open(SRC / "page_base_desktop__v1.png").convert("RGB")
    draw = ImageDraw.Draw(canvas)
    w, h = canvas.size

    font_brand = load_font("bold", 24)
    font_title = load_font("bold", 56)
    font_subtitle = load_font("regular", 32)
    font_card_label = load_font("bold", 28)
    font_card_body = load_font("regular", 22)
    font_footer = load_font("regular", 16)

    # Header on the right
    header_x = 1300
    hy = 80
    draw.text((header_x, hy), "ADVENTURES OF PATCH", font=font_brand, fill=TEAL)
    hy += font_brand.size + 20
    draw.text((header_x, hy), "Introducing Patch", font=font_title, fill=DARK)
    hy += font_title.size + 20
    draw_text_block(draw, "An autonomous software agent who makes workflows easy to follow.", font_subtitle, header_x, hy, w - header_x - 80)

    # Cards on the right
    card_x = 1200
    card_w = 900
    card_margin = 40
    cy = 360
    for label, body in CARDS:
        card_h = 200
        draw_rounded_card(draw, (card_x, cy, card_x + card_w, cy + card_h))
        tx = card_x + card_margin
        ty = cy + 30
        draw.text((tx, ty), label, font=font_card_label, fill=DARK)
        ty += font_card_label.size + 20
        draw_text_block(draw, body, font_card_body, tx, ty, card_w - 2 * card_margin)
        cy += card_h + 30

    # Footer bottom right
    footer_lines = wrap_text(FOOTER, font_footer, 900)
    fy = h - 60 - (len(footer_lines) * (font_footer.size + 4))
    for line in footer_lines:
        draw.text((w - 80 - font_footer.getlength(line), fy), line, font=font_footer, fill=DARK)
        fy += font_footer.size + 4

    out = PKG / "page__v1.png"
    canvas.save(out, "PNG")
    return out


def build_mobile() -> Path:
    base = Image.open(SRC / "page_base_desktop__v1.png").convert("RGB")
    w, h = 1080, 1920
    canvas = Image.new("RGB", (w, h), _background_sample(base))

    cutout = _extract_patch(base)
    bbox = _tight_bbox(cutout)
    if bbox:
        cutout = cutout.crop(bbox)

    # Fit Patch in the upper part of the canvas, leaving room for text below.
    max_w = w - 120
    max_h = 900
    scale = min(max_w / cutout.width, max_h / cutout.height)
    new_size = (int(cutout.width * scale), int(cutout.height * scale))
    cutout = cutout.resize(new_size, Image.Resampling.LANCZOS)

    paste_x = (w - cutout.width) // 2
    paste_y = 80
    canvas.paste(cutout, (paste_x, paste_y), cutout)
    patch_bottom = paste_y + cutout.height

    draw = ImageDraw.Draw(canvas)

    font_brand = load_font("bold", 22)
    font_title = load_font("bold", 56)
    font_subtitle = load_font("regular", 26)
    font_card_label = load_font("bold", 26)
    font_card_body = load_font("regular", 22)
    font_footer = load_font("regular", 16)

    # Header below Patch
    hx = 60
    hy = patch_bottom + 40
    draw.text((hx, hy), "ADVENTURES OF PATCH", font=font_brand, fill=TEAL)
    hy += font_brand.size + 15
    draw.text((hx, hy), "Introducing Patch", font=font_title, fill=DARK)
    hy += font_title.size + 15
    hy = draw_text_block(draw, "An autonomous software agent who makes workflows easy to follow.", font_subtitle, hx, hy, w - 120)

    # Cards below header
    card_x = 60
    card_w = w - 120
    card_margin = 30
    cy = hy + 40
    for label, body in CARDS:
        body_w = card_w - 2 * card_margin
        body_lines = wrap_text(body, font_card_body, body_w)
        label_h = font_card_label.size + 20
        body_h = len(body_lines) * (font_card_body.size + 6)
        card_h = 40 + label_h + body_h
        draw_rounded_card(draw, (card_x, cy, card_x + card_w, cy + card_h))
        tx = card_x + card_margin
        ty = cy + 20
        draw.text((tx, ty), label, font=font_card_label, fill=DARK)
        ty += font_card_label.size + 15
        draw_text_block(draw, body, font_card_body, tx, ty, body_w)
        cy += card_h + 20

    # Footer at bottom
    footer_lines = wrap_text(FOOTER, font_footer, w - 120)
    fy = h - 40 - (len(footer_lines) * (font_footer.size + 4))
    for line in footer_lines:
        draw.text((60, fy), line, font=font_footer, fill=DARK)
        fy += font_footer.size + 4

    out = PKG / "page__v1-mobile.png"
    canvas.save(out, "PNG")
    return out


def update_manifest() -> None:
    manifest = {
        "domain": "misc",
        "family": "introducing-patch",
        "package_id": "introducing-patch",
        "package_type": "one_pager",
        "status": "approved",
        "artifact_lanes": {
            "source_images": "present",
            "finished_page": "present",
            "finished_page_mobile": "present",
            "compiled_asset_sheets": "absent_not_required",
            "reference_sheets": "absent_not_required",
        },
        "files": {
            "source_images": ["page_base_desktop__v1.png"],
            "finished_page": "page__v1.png",
            "finished_page_mobile": "page__v1-mobile.png",
            "compiled_asset_sheets": [],
            "reference_sheets": [],
        },
        "provenance_notes": [
            "The single source base was generated using the Patch style bible and the OpenAI image generation MCP.",
            "The finished desktop page overlays the source base with deterministic text and cards.",
            "The finished mobile page extracts the Patch figure from the same source base and re-uses it on a portrait canvas.",
            "All final published one-pagers include the Adventures of Patch licence footer.",
        ],
        "core_lesson": "Patch makes hard workflows feel like a clear next step.",
    }
    manifest_path = PKG / "manifests" / "manifest.json"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    print(f"Building {build_desktop()}")
    print(f"Building {build_mobile()}")
    update_manifest()
    print("Updated manifest.json")

    for name in ["page__v1.png", "page__v1-mobile.png"]:
        out = PKG / name
        subprocess.run([sys.executable, "tools/generate_image_sidecar.py", str(out)])
    for name in ["source_images/page_base_desktop__v1.png"]:
        out = PKG / name
        subprocess.run([sys.executable, "tools/generate_image_sidecar.py", str(out)])


if __name__ == "__main__":
    main()
