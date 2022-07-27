from flask import Flask,render_template,request
from werkzeug.utils import secure_filename
import os
from PIL import Image, ImageEnhance
import  pytesseract

app = Flask(__name__)

uploads_dir = os.path.join(app.instance_path, 'uploads')
if not os.path.exists(uploads_dir):
    os.makedirs(uploads_dir)

@app.route('/')
def welcome():
    return render_template('imageUpload.html')

@app.route('/display',methods = ['POST'])  
def display():
    if request.method == 'POST':
        image = request.files['image'] 
        image.save(os.path.join(uploads_dir, secure_filename(image.filename))) 
        img = Image.open(os.path.join(uploads_dir, secure_filename(image.filename)))
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        enhancer1 = ImageEnhance.Sharpness(img)
        enhancer2 = ImageEnhance.Contrast(img)
        img_edit = enhancer1.enhance(20.0)
        img_edit = enhancer2.enhance(1.5)
        text = pytesseract.image_to_string(img_edit)
        #repr(text)
        #result = text.split("\n")
        return(text)

if __name__ == '__main__':
    app.run()    