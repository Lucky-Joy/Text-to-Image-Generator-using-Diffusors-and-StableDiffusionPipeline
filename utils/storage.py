import json
import os
from datetime import datetime
from io import BytesIO
from typing import List, Dict, Any, Optional

from PIL import Image

from .watermark import add_watermark


def ensure_dir(path: str) -> None:
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)


def get_output_folder(base_dir: str = "generated") -> str:
    today = datetime.now().strftime("%Y-%m-%d")
    folder = os.path.join(base_dir, today)
    ensure_dir(folder)
    return folder


def save_images_with_metadata(
    images: List[Image.Image],
    full_prompt: str,
    base_prompt: str,
    negative_prompt: str,
    style: str,
    model_id: str,
    device: str,
    num_inference_steps: int,
    guidance_scale: float,
    custom_prefix: Optional[str] = None,
    base_dir: str = "generated",
) -> List[Dict[str, Any]]:
    output_folder = get_output_folder(base_dir)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    results = []

    if custom_prefix and custom_prefix.strip():
        safe_prefix = custom_prefix.strip()
    else:
        safe_prefix = "".join(
            c if c.isalnum() or c in (" ", "_") else "_"
            for c in base_prompt
        ).strip()
        safe_prefix = "_".join(safe_prefix.split())[:40] or "image"

    for idx, img in enumerate(images, start=1):
        img_wm = add_watermark(img)

        stem = f"{safe_prefix}_{timestamp}_{idx}"
        png_path = os.path.join(output_folder, f"{stem}.png")
        jpg_path = os.path.join(output_folder, f"{stem}.jpg")
        json_path = os.path.join(output_folder, f"{stem}.json")

        img_wm.save(png_path, format="PNG")
        img_wm.convert("RGB").save(jpg_path, format="JPEG", quality=95)

        meta = {
            "prompt": full_prompt,
            "base_prompt": base_prompt,
            "negative_prompt": negative_prompt,
            "style": style,
            "timestamp": datetime.now().isoformat(),
            "model_id": model_id,
            "num_inference_steps": num_inference_steps,
            "guidance_scale": guidance_scale,
            "device": device,
            "png_path": png_path,
            "jpg_path": jpg_path,
            "filename_prefix": safe_prefix,
        }
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(meta, f, indent=2)

        png_bytes_io = BytesIO()
        img_wm.save(png_bytes_io, format="PNG")
        png_bytes_io.seek(0)

        jpg_bytes_io = BytesIO()
        img_wm.convert("RGB").save(jpg_bytes_io, format="JPEG", quality=95)
        jpg_bytes_io.seek(0)

        results.append(
            {
                "pil_image": img_wm,
                "stem": stem,
                "png_bytes": png_bytes_io,
                "jpg_bytes": jpg_bytes_io,
            }
        )

    return results