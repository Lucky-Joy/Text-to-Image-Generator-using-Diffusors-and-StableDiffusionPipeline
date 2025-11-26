from typing import Literal

StyleType = Literal["Photorealistic", "Artistic", "Cartoon", "Anime", "Van Gogh Style"]


def build_prompt(user_prompt: str, style: StyleType) -> str:
    style_map = {
        "Photorealistic": (
            "highly detailed, 4k, ultra realistic, "
            "professional photography, sharp focus, cinematic lighting"
        ),
        "Artistic": (
            "oil painting, rich colors, brush strokes, artstation, "
            "highly detailed, dramatic lighting"
        ),
        "Cartoon": (
            "cartoon, 2D illustration, bold outlines, flat colors, "
            "cute, vibrant, clean lines"
        ),
        "Anime": (
            "anime style, clean line art, cel shading, vibrant colors, "
            "highly detailed, studio quality"
        ),
        "Van Gogh Style": (
            "oil painting, thick brush strokes, swirling patterns, "
            "post-impressionist, vivid colors, in the style of Van Gogh"
        ),
    }

    style_suffix = style_map.get(style, "")
    base = user_prompt.strip()
    if style_suffix:
        return f"{base}, {style_suffix}"
    return base


BANNED_KEYWORDS = [
    "nsfw",
    "nude",
    "nudity",
    "porn",
    "sexual",
    "sex",
    "erotic",
    "gore",
    "blood",
    "violence",
    "kill",
    "murder",
    "terrorist",
    "hate",
    "racist",
]


def is_prompt_allowed(prompt: str) -> bool:
    p = prompt.lower()
    return not any(bad in p for bad in BANNED_KEYWORDS)


def default_negative_prompt() -> str:
    return (
        "blurry, low quality, distorted, lowres, bad anatomy, "
        "extra limbs, extra fingers, disfigured, watermark, logo, text, nsfw"
    )