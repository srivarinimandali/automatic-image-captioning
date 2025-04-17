
# 🖼️ Automatic Image Captioning Web App

This project is an **Automatic Image Captioning Web App** that uses a deep learning model trained on image descriptions to generate captions for uploaded or webcam-captured images. It features a camera interface, image selection, and a Flask backend to serve a caption prediction engine.

![Python](https://img.shields.io/badge/Python-Flask-blue?style=for-the-badge&logo=python)
![HTML](https://img.shields.io/badge/Frontend-HTML%2FCSS%2FJS-lightgrey?style=for-the-badge&logo=html5)
![Deep Learning](https://img.shields.io/badge/Model-CNN%2BRNN%20Caption%20Generator-orange?style=for-the-badge)
![OpenCV](https://img.shields.io/badge/Webcam-Capture%20Photo-brightgreen?style=for-the-badge&logo=opencv)
![NLP](https://img.shields.io/badge/NLP-Tokenizer%20%7C%20Beam%20Search-red?style=for-the-badge)

---

## 🔍 Features

- 📸 Capture image using webcam
- 🖼️ Upload image from local device
- 🧠 Generate natural language captions for images
- 🗂️ Dataset-based image description lookup
- 🎨 Clean and engaging UI (HTML/CSS/JS + Bootstrap)
- 🎙️ Voice instructions and user prompts

---

## ⚙️ Tech Stack

- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap
- **Backend**: Flask (Python)
- **Machine Learning**:
  - CNN encoder (e.g., InceptionV3 or VGG16)
  - RNN/GRU/LSTM decoder
  - Beam search or greedy decoding
  - Pre-trained tokenizer (`tokenizer.p`)
- **Tools**: OpenCV (for webcam capture), PIL, NumPy, Keras/TensorFlow

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

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/image-captioning-webapp.git
cd image-captioning-webapp
```

### 2. Create & activate virtual environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Place your model files

- Save trained model weights and architecture in the `/Model files` folder
- Make sure `tokenizer.p` and `descriptions.txt` are placed at the root

### 5. Start the Flask app

```bash
python app.py
```

The app runs on `http://localhost:5000`

---

## 🧪 How It Works

1. Navigate to `localhost:5000`
2. Choose an image input mode:
   - Upload image
   - Capture using webcam
3. Click **"Generate the Caption"**
4. View the result with dynamically rendered caption

---

## 🧠 Model Summary

- **Encoder**: Pre-trained CNN extracts image features
- **Decoder**: LSTM/GRU model trained on MSCOCO-style dataset
- **Input**: Image → Extracted features + partial sentence
- **Output**: Natural language sentence describing the image

---
## 👨‍💻 Developer

**Srivarini Mandali**  
🔗 [GitHub](https://github.com/srivarinimandali)
