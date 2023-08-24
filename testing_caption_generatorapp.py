from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.applications.xception import Xception
from keras.models import load_model
from pickle import load
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import argparse


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/predict',methods = ['GET','POST'])
def upload():
    if request.method == 'POST':
    	f = request.files['image']
    	print("current path")
    	basepath = os.path.dirname(__file__)
    	print("current path", basepath)
    	filepath = os.path.join(basepath,'uploads',f.filename)
    	print("upload folder is ", filepath)
    	f.save(filepath)
    	text = modelpredict(filepath)
    	return text

def extract_features(filename, model):
    image = Image.open(filename)
    
    image = image.resize((299,299))
    image = np.array(image)
    # for images that has 4 channels, we convert them into 3 channels
    if image.shape[2] == 4:
        image = image[..., :3]
    image = np.expand_dims(image, axis=0)
    image = image/127.5
    image = image - 1.0
    feature = model.predict(image)
    return feature

def word_for_id(integer, tokenizer):
 for word, index in tokenizer.word_index.items():
     if index == integer:
         return word
 return None


def generate_desc(model, tokenizer, photo, max_length):
    in_text = 'start'
    for i in range(max_length):
        sequence = tokenizer.texts_to_sequences([in_text])[0]
        sequence = pad_sequences([sequence], maxlen=max_length)
        pred = model.predict([photo,sequence], verbose=0)
        pred = np.argmax(pred)
        word = word_for_id(pred, tokenizer)
        if word is None:
            break
        in_text += ' ' + word
        if word == 'end':
            break
    return in_text

#path = 'Flicker8k_Dataset/111537222_07e56d5a30.jpg'
def modelpredict(filepath):
    max_length = 32
    tokenizer = load(open("C:/Users/prads/Downloads/python-project-image-caption-generator/tokenizer.p/tokenizer.p","rb"))
    model = load_model('C:/Users/prads/Downloads/python-project-image-caption-generator/models/model_9.h5')
    xception_model = Xception(include_top=False, pooling="avg")
    photo = extract_features(img_path, xception_model)
    #img = Image.open(img_path)
    description = generate_desc(model, tokenizer, photo, max_length)
    print(description)
    return description

if __name__ == '__main__':
    app.run(debug = True, threaded = False)