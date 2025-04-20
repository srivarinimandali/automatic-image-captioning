
# 🖼️ Automatic Image Captioning Web App for Visually Impaired

This project is an **Automatic Image Captioning Web App** that uses a deep learning model trained on image descriptions to generate captions for uploaded or webcam-captured images. It features a camera interface, image selection, and a Flask backend to serve a caption prediction engine.  
✨ **Specially designed to assist visually impaired users** by providing audio and text-based image descriptions.

![Python](https://img.shields.io/badge/Python-Flask-blue?style=for-the-badge&logo=python)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-lightgrey?style=for-the-badge&logo=html5)
![Deep Learning](https://img.shields.io/badge/Model-CNN%2BRNN%20Caption%20Generator-orange?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/Webcam-Capture%20Photo-brightgreen?style=for-the-badge&logo=opencv)
![NLP](https://img.shields.io/badge/NLP-Tokenizer%20%7C%20Beam%20Search-red?style=for-the-badge)
![Accessibility](https://img.shields.io/badge/Accessibility-Visually%20Impaired%20Support-ff69b4?style=for-the-badge)


---

## 🔍 Features

### 🧑‍🦯 Accessibility-First Design
- 🎧 Audio-based instructions for navigation
- 🗣️ Text-to-speech integration for caption playback
- 📷 Capture or upload images independently
- 👁️ Describe surroundings visually for blind and low-vision users

### 🔒 User Features
- Webcam & file image input
- Real-time caption generation
- User-friendly interface
- Voice-enabled interactions

---

## ⚙️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Flask (Python)
- **Machine Learning**:
  - CNN encoder (e.g., InceptionV3 or VGG16)
  - RNN/GRU/LSTM decoder
  - Beam search or greedy decoding
  - Pre-trained tokenizer (`tokenizer.p`)
- **Tools**: OpenCV, PIL, NumPy, Keras/TensorFlow

---

## 🗃️ File Structure

```
/templates
    capturephoto.html
    backupcapturephoto.html
    options.html

/static
    css/
    js/
    logo1.png, webcam.gif, etc.

app.py                       ← Flask web server
training_caption_generator.ipynb  ← Model training notebook
testing_caption_generator.py      ← Caption generation logic
tokenizer.p                  ← Pre-trained tokenizer
Model files/                 ← Saved model weights and architectures
descriptions.txt             ← Caption dataset
```

---

## 🔧 Setup & Run Locally

```bash
git clone https://github.com/yourusername/image-captioning-webapp.git
cd image-captioning-webapp

python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

### Add Model Files
- Place weights in `/Model files`
- Add `tokenizer.p`, `descriptions.txt` to project root

### Run App
```bash
python app.py
```

Go to `http://localhost:5000`

---

## 🧠 How It Works

1. User accesses camera or uploads an image
2. CNN extracts features from image
3. RNN generates descriptive sentence from features
4. Caption is rendered and optionally read aloud

---
## 👨‍💻 Developer

**Srivarini Mandali**  
🔗 [GitHub](https://github.com/srivarinimandali)


