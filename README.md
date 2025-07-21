# 🖼️ Instruct2Pic – Image Editing with Instructions

This project demonstrates interactive image editing using natural language prompts powered by the **InstructPix2Pix** model from Hugging Face's `diffusers` library. It allows users to upload an image, provide a textual instruction (prompt), and receive an AI-generated modified image.

The application is built with **PyTorch**, **Gradio**, and the **Stable Diffusion InstructPix2Pix pipeline** using a GPU for real-time image editing.

---

## 📁 Project Structure

Instruct2Pic/  
├── main.py                # Main Python script with Gradio interface  
├── requirements.txt       # List of Python dependencies  

---

## 🚀 Features

🧠 Edit any image by giving a natural language prompt  
🖼️ Upload images directly from local storage  
⚡ Powered by Stable Diffusion InstructPix2Pix  
🎨 Real-time inference with GPU acceleration  
💻 Clean interface using Gradio  

---

## ⚙️ Technologies Used

- Python 3.10+  
- PyTorch  
- Hugging Face diffusers  
- PIL (Pillow)  
- Gradio  
- CUDA (for GPU execution)  

---

## 🧪 Installation & Running Locally

1. Clone the repository  
git clone https://github.com/Sharavanakumar-Ramalingam/Instruct2Pic.git  
cd Instruct2Pic  

2. Create virtual environment (optional but recommended)  
python -m venv venv  
source venv/bin/activate (Linux/macOS) or venv\Scripts\activate (Windows)  

3. Install dependencies  
pip install -r requirements.txt  

4. Launch the application  
python main.py  

This will start a Gradio interface at:  
http://127.0.0.1:7860  

---

## 🧠 How It Works

The app loads the `timbrooks/instruct-pix2pix` model from Hugging Face, sets the scheduler to Euler Ancestral, and runs inference using `StableDiffusionInstructPix2PixPipeline`.  
The uploaded image is preprocessed and passed along with the prompt to the model, which returns the modified output image.  

The app uses `torch.float16` and runs on GPU (`cuda`) for efficient performance.  

---

## 📜 requirements.txt

torch  
Pillow  
requests  
gradio  
diffusers  
transformers  
accelerate  

You can create a file named `requirements.txt` with the above content or install them manually.  

---

## 🙏 Acknowledgements

- Hugging Face for the `diffusers` library and InstructPix2Pix model  
- Tim Brooks for the original model  
- Gradio for the UI framework  

---

## 👨‍💻 Author

Sharavanakumar Ramalingam  
> Built as an experimental AI-powered image editor for creative use cases  

---

## 🌟 Support

If you found this project helpful, give it a ⭐ on GitHub:  
https://github.com/Sharavanakumar-Ramalingam/Instruct2Pic
