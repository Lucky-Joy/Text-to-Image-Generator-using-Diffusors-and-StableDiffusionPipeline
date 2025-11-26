from typing import List, Optional

from PIL import Image
from diffusers import StableDiffusionPipeline

from utils.prompts import build_prompt


def generate_images(
    pipe: StableDiffusionPipeline,
    base_prompt: str,
    style: str,
    negative_prompt: Optional[str],
    num_images: int = 1,
    num_inference_steps: int = 25,
    guidance_scale: float = 7.5,
    height: int = 512,
    width: int = 512,
) -> (List[Image.Image], str):
    full_prompt = build_prompt(base_prompt, style)

    prompt_list = [full_prompt] * num_images
    neg_list = (
        [negative_prompt] * num_images if negative_prompt and negative_prompt.strip() else None
    )

    result = pipe(
        prompt=prompt_list,
        negative_prompt=neg_list,
        num_inference_steps=num_inference_steps,
        guidance_scale=guidance_scale,
        height=height,
        width=width,
    )

    return result.images, full_prompt