import time

import streamlit as st

from models.model_loader import load_pipeline
from generate import generate_images
from utils.prompts import (
    default_negative_prompt,
    is_prompt_allowed,
)
from utils.storage import save_images_with_metadata


MODEL_ID = "runwayml/stable-diffusion-v1-5"


@st.cache_resource
def get_pipeline():
    pipe, device = load_pipeline(MODEL_ID)
    return pipe, device


def main():
    st.set_page_config(
        page_title="AI-Powered Text-to-Image Generator",
        layout="centered",
    )

    st.title("🎨 AI-Powered Text-to-Image Generator")
    st.markdown(
        "Convert your text descriptions into AI-generated images using open-source Stable Diffusion models."
    )

    with st.expander("ℹ️ Responsible Use, Safety & Model Info", expanded=False):
        st.write(
            "- This tool uses open-source diffusion models (Stable Diffusion family).\n"
            "- All images are **AI-generated** and automatically **watermarked**.\n"
            "- Prompts containing explicit, violent or hateful content are blocked.\n"
            "- Do not use generated images to mislead people or violate any laws.\n"
            "- On CPU, generation is slower; GPU is recommended for production use."
        )

    pipe, device = get_pipeline()
    st.sidebar.header("Generation Settings")

    base_prompt = st.text_area(
        "Enter your text prompt",
        value="a futuristic city at sunset",
        placeholder="Describe what you want to see...",
    )

    style = st.sidebar.selectbox(
        "Style",
        options=["Photorealistic", "Artistic", "Cartoon", "Anime", "Van Gogh Style"],
        index=0,
    )

    num_images = st.sidebar.slider("Number of images", min_value=1, max_value=4, value=1)

    steps = st.sidebar.slider("Inference steps", min_value=15, max_value=40, value=25)
    guidance_scale = st.sidebar.slider(
        "Guidance scale", min_value=5.0, max_value=12.0, value=7.5, step=0.5
    )

    height = st.sidebar.selectbox("Image height", [512, 640], index=0)
    width = st.sidebar.selectbox("Image width", [512, 640], index=0)

    st.sidebar.markdown("---")
    st.sidebar.write(f"💻 Detected device: **{device.upper()}**")

    if device == "cpu":
        st.info(
            "Running on **CPU**. Generation may take longer. "
            "For faster results, use fewer images, lower resolution, and fewer steps."
        )
    else:
        st.success("Running on **GPU**. High-resolution generation is supported.")

    negative_prompt_input = st.text_input(
        "Negative prompt (optional)",
        placeholder="If empty, a default quality-focused negative prompt is used.",
    )

    negative_prompt = (
        negative_prompt_input.strip()
        if negative_prompt_input.strip()
        else default_negative_prompt()
    )

    custom_prefix = st.text_input(
        "Custom filename prefix (optional)",
        placeholder="e.g. futuristic_city, robot_portrait ...",
    )

    generate_btn = st.button("Generate Images")

    if generate_btn:
        if not base_prompt.strip():
            st.warning("Please enter a prompt before generating.")
            return

        if not is_prompt_allowed(base_prompt):
            st.error(
                "Your prompt appears to contain inappropriate or unsafe content. "
                "Please modify it and try again."
            )
            return

        if device == "cpu":
            est_per_image = 8
        else:
            est_per_image = 2

        estimated_total = est_per_image * num_images
        st.write(f"⏱ Estimated completion time: ~{estimated_total} seconds")

        progress_bar = st.progress(0)
        status_text = st.empty()

        start_time = time.time()
        status_text.text("Initializing model and generating images...")

        for i in range(60):
            time.sleep(0.02)
            progress_bar.progress(i + 1)

        images, full_prompt = generate_images(
            pipe=pipe,
            base_prompt=base_prompt,
            style=style,
            negative_prompt=negative_prompt,
            num_images=num_images,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
            height=height,
            width=width,
        )

        elapsed = time.time() - start_time
        progress_bar.progress(100)
        status_text.text(f"Completed in {elapsed:.1f} seconds.")

        file_info_list = save_images_with_metadata(
            images=images,
            full_prompt=full_prompt,
            base_prompt=base_prompt,
            negative_prompt=negative_prompt,
            style=style,
            model_id=MODEL_ID,
            device=device,
            num_inference_steps=steps,
            guidance_scale=guidance_scale,
            custom_prefix=custom_prefix,
        )

        st.subheader("Generated Images")

        for info in file_info_list:
            st.image(info["pil_image"], caption=info["stem"], use_column_width=True)

            col1, col2 = st.columns(2)
            with col1:
                st.download_button(
                    label="Download PNG",
                    data=info["png_bytes"],
                    file_name=f"{info['stem']}.png",
                    mime="image/png",
                )
            with col2:
                st.download_button(
                    label="Download JPEG",
                    data=info["jpg_bytes"],
                    file_name=f"{info['stem']}.jpg",
                    mime="image/jpeg",
                )


if __name__ == "__main__":
    main()