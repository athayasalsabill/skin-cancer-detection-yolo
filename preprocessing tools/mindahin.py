"""mindahin gambar dari folder 'basal-cell-carcinoma' ke folder 'Dataset' 
dan displit ke train, valid, dan testnya"""


import os
import shutil
import random

# Fungsi untuk memindahkan gambar ke folder train, valid, dan test
def split_and_move_images(source_folder, train_folder, valid_folder, test_folder, train_count=4750, valid_count=200, test_count=40):
    # Buat folder train, valid, test jika belum ada
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(valid_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # Dapatkan daftar semua gambar di folder sumber
    images = [img for img in os.listdir(source_folder) if img.endswith(('.JPG','.jpg', '.jpeg', '.png'))]

    # Shuffle gambar agar pemilihan acak
    random.shuffle(images)

    # Cek apakah ada cukup gambar untuk split
    total_required = train_count + valid_count + test_count
    if len(images) < total_required:
        print(f"Not enough images. Only found {len(images)} images, but need {total_required}.")
        return

    # Bagi gambar untuk train, valid, dan test
    train_images = images[:train_count]
    valid_images = images[train_count:train_count + valid_count]
    test_images = images[train_count + valid_count:train_count + valid_count + test_count]

    # Pindahkan gambar ke folder train
    for img in train_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(train_folder, img))
    print(f"Moved {len(train_images)} images to {train_folder}")

    # Pindahkan gambar ke folder valid
    for img in valid_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(valid_folder, img))
    print(f"Moved {len(valid_images)} images to {valid_folder}")

    # Pindahkan gambar ke folder test
    for img in test_images:
        shutil.move(os.path.join(source_folder, img), os.path.join(test_folder, img))
    print(f"Moved {len(test_images)} images to {test_folder}")

# Path ke folder basal-cell-carcinoma asli
source_folder = 'ISIC Archive/squamous-cell-carcinoma'  # Ganti dengan path yang sesuai

# Path ke folder tujuan (train, valid, test)
train_folder = 'Dataset-Athaya-3.0/train/squamous-cell-carcinoma'
valid_folder = 'Dataset-Athaya-3.0/valid/squamous-cell-carcinoma'
test_folder = 'Dataset-Athaya-3.0/test/squamous-cell-carcinoma'

# Jalankan fungsi untuk memindahkan dan membagi gambar
split_and_move_images(source_folder, train_folder, valid_folder, test_folder, train_count=1100, valid_count=200, test_count=50)
