import torch
from diffusers import StableDiffusionPipeline

def load_pipeline(
    model_id: str = "runwayml/stable-diffusion-v1-5",
    use_fp16: bool = True,
):
    if torch.cuda.is_available():
        device = "cuda"
        dtype = torch.float16 if use_fp16 else torch.float32
    else:
        device = "cpu"
        dtype = torch.float32

    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=dtype,
        safety_checker=None,
    )

    pipe = pipe.to(device)

    if device == "cuda":
        try:
            pipe.enable_xformers_memory_efficient_attention()
        except Exception:
            pass

    return pipe, device