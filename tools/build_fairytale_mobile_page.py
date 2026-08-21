#!/usr/bin/env python3
"""Deterministic mobile portrait build for the Goldilocks fairytale page."""

from __future__ import annotations

import json
import textwrap
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parent.parent
OUTPUT_DIR = ROOT / "published" / "fairytales" / "goldilocks"

CANVAS = (1080, 1920)
BG = (247, 244, 236)
DARK = (29, 43, 58)
TEAL = (14, 141, 132)
GOLD = (190, 145, 47)
WHITE = (255, 255, 255)


def load_font(style: str, size: int) -> ImageFont.FreeTypeFont:
    family = {
        "regular": r"C:\Windows\Fonts\arial.ttf",
        "bold": r"C:\Windows\Fonts\arialbd.ttf",
    }
    path = family.get(style, family["regular"])
    return ImageFont.truetype(path, size)


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


def load_scene(name: str) -> Image.Image:
    return Image.open(OUTPUT_DIR / f"scene__{name}__v1.png").convert("RGB")


def draw_rounded_card(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int, int, int],
    radius: int = 20,
    fill: tuple[int, int, int] = WHITE,
    outline: tuple[int, int, int] = DARK,
    width: int = 2,
) -> None:
    draw.rounded_rectangle(xy, radius=radius, fill=fill, outline=outline, width=width)


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    text: str,
    font: ImageFont.FreeTypeFont,
    x: int,
    y: int,
    max_width: int,
    color: tuple[int, int, int] = DARK,
    line_spacing: int = 6,
) -> int:
    lines = wrap_text(text, font, max_width)
    for line in lines:
        draw.text((x, y), line, font=font, fill=color)
        y += font.size + line_spacing
    return y


def build() -> Path:
    canvas = Image.new("RGB", CANVAS, BG)
    draw = ImageDraw.Draw(canvas)

    # Header
    font_label = load_font("bold", 24)
    font_title = load_font("bold", 56)
    font_subtitle = load_font("regular", 32)

    header_x = 60
    hy = 60
    draw.text((header_x, hy), "PATCH FAIRYTALES", font=font_label, fill=TEAL)
    hy += font_label.size + 10
    hy = draw_text_block(draw, "Goldilocks and the Right Amount of Guidance", font_title, header_x, hy, CANVAS[0] - 120)
    hy += 15
    draw.text((header_x, hy), "Too much. Not enough. Just right.", font=font_subtitle, fill=DARK)
    row_y = hy + font_subtitle.size + 40

    scenes = [
        ("too_much", "TOO MUCH", "Too much guidance becomes another problem to solve. When tools, rules and competing instructions pile up, Patch spends his effort reconciling context instead of moving."),
        ("not_enough", "NOT ENOUGH", "Too little guidance leaves too many equally reasonable next moves. A vague goal forces Patch to guess which path matters."),
        ("just_right", "JUST RIGHT", "Give enough useful structure for Patch to choose what matters and act. Clear, organised guidance supports a confident next decision."),
    ]

    font_scene_label = load_font("bold", 28)
    font_scene_body = load_font("regular", 22)
    row_h = 430
    card_margin = 60
    card_w = CANVAS[0] - 2 * card_margin
    image_w = 540
    image_h = 304

    for file_key, label, caption in scenes:
        scene = load_scene(file_key)
        scene = scene.resize((image_w, image_h), Image.Resampling.LANCZOS)

        card_box = (card_margin, row_y, card_margin + card_w, row_y + row_h)
        draw_rounded_card(draw, card_box)

        img_x = card_margin + 40
        img_y = row_y + (row_h - image_h) // 2
        canvas.paste(scene, (img_x, img_y))

        text_x = img_x + image_w + 40
        text_y = img_y + 10
        text_w = card_w - image_w - 40 - 40 - 40

        draw.text((text_x, text_y), label, font=font_scene_label, fill=DARK)
        text_y += font_scene_label.size + 20
        draw_text_block(draw, caption, font_scene_body, text_x, text_y, text_w)

        row_y += row_h + 20

    # Lesson bar
    lesson_y = row_y + 10
    lesson_h = 220
    lesson_box = (card_margin, lesson_y, card_margin + card_w, lesson_y + lesson_h)
    draw_rounded_card(draw, lesson_box, fill=WHITE)

    font_lesson_label = load_font("bold", 24)
    font_lesson_body = load_font("regular", 26)
    lesson_label = "THE LESSON"
    lesson_text = "Good agent guidance is not maximum context. It is enough relevant context for a confident next decision."

    lx = card_margin + 40
    ly = lesson_y + 30
    draw.text((lx, ly), lesson_label, font=font_lesson_label, fill=GOLD)
    ly += font_lesson_label.size + 20
    draw_text_block(draw, lesson_text, font_lesson_body, lx, ly, card_w - 80)

    out_path = OUTPUT_DIR / "page__right_amount_of_guidance__v1-mobile.png"
    canvas.save(out_path, "PNG")
    return out_path


def update_manifest() -> None:
    manifest_path = OUTPUT_DIR / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    manifest["artifact_lanes"]["finished_page_mobile"] = "present"
    manifest["files"]["finished_page_mobile"] = "page__right_amount_of_guidance__v1-mobile.png"
    manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def main() -> None:
    out = build()
    print(f"wrote: {out}")
    update_manifest()
    print("updated manifest.json")


if __name__ == "__main__":
    main()
