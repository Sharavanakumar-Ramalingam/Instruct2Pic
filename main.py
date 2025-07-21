import torch
import PIL
import requests
import gradio as gr
from PIL import Image, ImageOps
from diffusers import StableDiffusionInstructPix2PixPipeline, EulerAncestralDiscreteScheduler

model_id = "timbrooks/instruct-pix2pix"
pipe = StableDiffusionInstructPix2PixPipeline.from_pretrained(
    model_id,
    torch_dtype=torch.float16,
    safety_checker=None
)
pipe.to("cuda")
pipe.scheduler = EulerAncestralDiscreteScheduler.from_config(pipe.scheduler.config)

def download_image_from_url(url):
    image = Image.open(requests.get(url, stream=True).raw)
    image = ImageOps.exif_transpose(image)
    image = image.convert("RGB")
    return image

def generate(image, prompt):
    image = image.convert("RGB")
    result = pipe(prompt=prompt, image=image, num_inference_steps=10, image_guidance_scale=1).images[0]
    return result

# Gradio Interface
with gr.Blocks() as demo:
    gr.Markdown("## InstructPix2Pix - Image Editing with Instructions")
    with gr.Row():
        with gr.Column():
            input_image = gr.Image(type="pil", label="Upload Image")
            prompt = gr.Textbox(label="Instruction Prompt", value="turn him into cyborg")
            btn = gr.Button("Generate")
        with gr.Column():
            output_image = gr.Image(label="Output Image")

    btn.click(fn=generate, inputs=[input_image, prompt], outputs=output_image)

demo.launch()
