
from flask import Flask, render_template, request, make_response
import os
from ultralytics import YOLO
from pathlib import Path
from PIL import Image  # Tambahkan import untuk PIL.Image
import numpy as np
import io
import cv2  # Tambahkan OpenCV untuk konversi warna

app = Flask(__name__)

@app.after_request
def add_header(response):
    response.headers['ngrok-skip-browser-warning'] = 'true'
    return response

# Load model YOLOv8
model = YOLO('best28.pt')

def clear_static_folder():
    for filename in os.listdir('static'):
        file_path = os.path.join('static', filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

def clear_images_folder():
    for filename in os.listdir('images'):
        file_path = os.path.join('images', filename)
        if os.path.isfile(file_path):
            os.remove(file_path)

@app.route('/', methods=["GET", "POST"])
def predict():
    clear_static_folder()
    clear_images_folder()

    if request.method == "POST":
        if 'imagefile' in request.files:
            imagefile = request.files['imagefile']
            if imagefile.filename == 'captured_image.png':  # Gambar dari kamera
                img = Image.open(io.BytesIO(imagefile.read()))
                image_path = os.path.join('./images', 'captured_image.png')
                img.save(image_path)
            else:  # Gambar dari upload file
                image_path = os.path.join('./images', imagefile.filename)
                imagefile.save(image_path)

            # Melakukan inference menggunakan YOLOv8
            results = model.predict(source=image_path, save=False)

            # Mengecek apakah ada bounding box yang terdeteksi
            if len(results[0].boxes) > 0:
                # Dapatkan bounding box dengan confidence tertinggi
                confidences = results[0].boxes.conf.cpu().numpy()  # Dapatkan confidence setiap bounding box
                best_box_idx = confidences.argmax()  # Indeks bounding box dengan confidence tertinggi
                result_image_np = results[0].plot(boxes=[results[0].boxes[best_box_idx]])  # Plot hanya bounding box terbaik
            else:
                # Jika tidak ada bounding box, tampilkan gambar input tanpa bounding box
                result_image_np = cv2.imread(image_path)

            # Convert BGR (OpenCV format) to RGB (PIL format)
            result_image_rgb = cv2.cvtColor(result_image_np, cv2.COLOR_BGR2RGB)

            # Konversi numpy.ndarray ke PIL.Image
            result_image_pil = Image.fromarray(result_image_rgb)

            # Simpan hasil gambar ke direktori static
            static_image_path = os.path.join('static', imagefile.filename)
            result_image_pil.save(static_image_path)

            return render_template('index.html', output_image=imagefile.filename)

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('./images'):
        os.makedirs('./images')
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(port=3000)
