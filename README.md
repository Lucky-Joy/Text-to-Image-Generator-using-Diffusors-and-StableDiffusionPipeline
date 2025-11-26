# Text-to-Image-Generator-using-Diffusors-and-StableDiffusionPipeline

This project implements an AI-powered text-to-image generation system using an open-source Stable Diffusion model. Users can enter textual prompts, select a visual style, and generate high-quality images via a simple web interface built with Streamlit.

---

## 1. Project Overview

- **Objective:** Convert text descriptions into images using open-source generative AI.
- **Model:** Stable Diffusion v1.5 (`runwayml/stable-diffusion-v1-5`) via the Hugging Face `diffusers` library.
- **Frameworks:** PyTorch for model execution, Streamlit for the user interface.
- **Key Features:**
  - Text-to-image generation with multiple styles.
  - Adjustable generation parameters (number of images, steps, guidance scale, resolution).
  - Image saving with metadata (prompt, timestamp, parameters).
  - Export in PNG and JPEG formats with user-friendly download buttons.
  - Simple content filtering and watermarking for ethical AI use.

---

## 2. Architecture

High-level components:

- **Web UI (`app.py`):** Streamlit app for interacting with the model.
- **Model Loader (`models/model_loader.py`):** Loads Stable Diffusion pipeline on CPU/GPU.
- **Generation Logic (`generate.py`):** Wraps the pipeline to generate images from prompts.
- **Utilities (`utils/`):**
  - `prompts.py`: Prompt engineering helpers, style presets, safety checks.
  - `storage.py`: Handles saving images and metadata in structured folders.
  - `watermark.py`: Adds an AI-origin watermark to each generated image.

Data flow:

`User → Streamlit UI → Generation API → Stable Diffusion Model → Image + Metadata → Disk + UI`

---

## 3. Setup & Installation

### 3.1. Clone the Repository

```bash
git clone https://github.com/<your-username>/ai-image-generator.git
cd ai-image-generator
