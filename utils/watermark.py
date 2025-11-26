from PIL import Image, ImageDraw, ImageFont

def add_watermark(
    image: Image.Image,
    text: str = "AI-generated image",
) -> Image.Image:
    img = image.copy().convert("RGBA")
    overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    try:
        font_size = max(16, img.width // 40)
        font = ImageFont.truetype("arial.ttf", size=font_size)
    except Exception:
        font = ImageFont.load_default()

    text_width, text_height = draw.textsize(text, font=font)
    margin = max(10, img.width // 80)

    x = img.width - text_width - margin
    y = img.height - text_height - margin

    rect_margin = 4
    draw.rectangle(
        [x - rect_margin, y - rect_margin, x + text_width + rect_margin, y + text_height + rect_margin],
        fill=(0, 0, 0, 120),
    )

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 200))

    out = Image.alpha_composite(img, overlay).convert("RGB")
    return out