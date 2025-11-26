# **AI-Powered Text-to-Image Generator**

An open-source text-to-image generation system built using **Stable Diffusion**, **PyTorch**, and **Streamlit**.
This project demonstrates the ability to implement generative AI systems locally, with support for prompt engineering, negative prompts, adjustable parameters, image export, metadata storage, and ethical AI safeguards.

---

## **1. Project Overview**

This project converts text descriptions into AI-generated images using open-source diffusion models.
It is designed as a hands-on implementation of:

* Text-to-image generation
* Prompt engineering
* Image quality enhancement
* Ethical AI considerations
* Local deployment with CPU/GPU fallback
* Saving images with metadata

The system includes a simple Streamlit interface where users can:

* Enter text prompts
* Choose visual style presets
* Adjust generation parameters
* Generate multiple images
* Download outputs
* Save metadata (prompt, parameters, timestamp)

---

## **2. Architecture**

### **High-Level Flow**

```
User Prompt → Streamlit UI → Generation Pipeline → Stable Diffusion Model → 
Image + Metadata → Saved to Disk → Optional Export
```

### **Project Structure**

```
ai-image-generator/
│
├── app.py                    # Streamlit UI
├── generate.py               # Image generation wrapper
├── requirements.txt
│
├── models/
│   ├── __init__.py
│   └── model_loader.py       # Loads SD model with CPU/GPU fallback
│
├── utils/
│   ├── __init__.py
│   ├── prompts.py            # Prompt engineering + content filtering
│   ├── storage.py            # Saving images + metadata in folders
│   └── watermark.py          # Watermark for ethical compliance
│
└── generated/                # Auto-created timestamp folders
    └── YYYY-MM-DD/
```

### **Key Components**

* **Streamlit UI** → Takes user input
* **Model Loader** → Loads Stable Diffusion v1.5
* **Generate Module** → Runs inference with specified settings
* **Utilities** → Prompt engineering, watermarking, metadata storage
* **Generated Folder** → Saves images + JSON metadata

---

## **3. Setup and Installation**

### **Clone the Repository**

```bash
git clone https://github.com/<your-username>/ai-image-generator.git
cd ai-image-generator
```

### **Create a Virtual Environment (Optional but Recommended)**

```bash
python -m venv venv
```

Activate it:

**Windows:**

```bash
venv\Scripts\activate
```

**Linux/macOS:**

```bash
source venv/bin/activate
```

### **Install Dependencies**

```bash
pip install -r requirements.txt
```

### **Model Download Instructions**

The first time you run the app, the Stable Diffusion model
**`runwayml/stable-diffusion-v1-5`**
will be automatically downloaded from Hugging Face.

If required, create a free HuggingFace account and accept the model license.

---

## **4. Hardware Requirements**

### **Recommended (GPU)**

* NVIDIA GPU with **8 GB+ VRAM**
* Much faster generation
* Higher resolution possible

### **CPU-Only**

* Works on modern CPUs (e.g., Intel i5)
* Slower generation time
* Recommended CPU settings:

  * 1–2 images per prompt
  * 512×512 resolution
  * 20–25 inference steps

The system automatically detects whether to use:

```
CUDA (GPU)
or
CPU Fallback
```

---

## **5. Usage Instructions**

### **Run the Application**

```bash
streamlit run app.py
```

This opens a local web app at:

```
http://localhost:8501
```

### **Interface Features**

#### **Inputs**

* Enter your text prompt
* Choose style:

  * Photorealistic
  * Artistic
  * Cartoon
  * Anime
  * Van Gogh Style
* Generation parameters:

  * Number of images (1–4)
  * Inference steps (15–40)
  * Guidance scale (5.0–12.0)
  * Resolution (512×512 or 640×640)
* Optional:

  * Negative prompt
  * Custom filename prefix

#### **Outputs**

* Generated images displayed on the page
* Download buttons (PNG and JPEG)
* Images saved automatically under:

  ```
  generated/YYYY-MM-DD/
  ```
* Each image gets an accompanying JSON metadata file containing:

  * Prompt + engineered prompt
  * Negative prompt
  * Style
  * Inference steps
  * Guidance scale
  * Timestamp
  * Model ID
  * Device used

### **Example Prompts**

```
a futuristic city at sunset
portrait of a robot in van gogh style
a cute cat playing piano, cartoon style
a warrior standing on a cliff, cinematic lighting, photorealistic
anime girl reading under cherry blossom trees
```

---

## **6. Technology Stack**

* **Language:** Python
* **Deep Learning Framework:** PyTorch
* **Model Library:** Diffusers (Hugging Face)
* **Stable Diffusion Model:** `runwayml/stable-diffusion-v1-5`
* **UI Framework:** Streamlit
* **Image Processing:** Pillow (PIL)
* **Acceleration:** xformers (optional for GPU)

---

## **7. Prompt Engineering: Tips & Best Practices**

### **Quality Boosters**

Add these descriptors for better results:

* *“highly detailed”*
* *“4k resolution”*
* *“cinematic lighting”*
* *“professional photography”*
* *“ultra realistic”*

### **Artistic Styles**

You can enrich prompts by referencing:

* “oil painting, textured brush strokes”
* “studio ghibli style”
* “watercolor, soft pastel tones”
* “digital art, trending on ArtStation”

### **Negative Prompts**

These help avoid issues:

```
blurry, low quality, distorted, watermark, extra limbs, extra fingers, bad anatomy
```

### **General Tips**

* More specific prompt → better output
* Avoid overly long sentences
* Style + subject + environment works best
* Increase inference steps for higher quality (at cost of speed)

---

## **8. Limitations**

* **Slow on CPU**: Stable Diffusion is heavy without GPU acceleration
* **VRAM Requirements**: Larger models (SDXL) require 8–12 GB VRAM
* **Prompt Sensitivity**: Poor prompts can give inconsistent results
* **Safety Filter is Basic**: Only keyword-based for simplicity
* **Memory Usage**: Multiple images + high resolution uses more RAM

---

## **9. Future Improvements**

* Add support for **SDXL** or other newer open-source models
* Add **LoRA fine-tuning** for custom styles
* Implement **image-to-image** or **inpainting** modes
* Add **web deployment** (HuggingFace Spaces, Render, etc.)
* Optimize model loading and caching
* Add real-time step-by-step preview
* Add style transfer from user-uploaded reference images

---
