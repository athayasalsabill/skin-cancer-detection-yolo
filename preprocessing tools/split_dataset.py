"""split gambar dari folder
├── Dataset
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 

menjadi bentuk sperti:

/Dataset 
├── train 
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
├── valid 
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
├── test
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
"""

import os
import shutil
import random

# Fungsi untuk split dataset menjadi train, valid, test
def split_dataset(dataset_folder, train_size=1100, valid_size=200, test_size=40):
    # Dapatkan daftar kelas (subfolder)
    classes = [d for d in os.listdir(dataset_folder) if os.path.isdir(os.path.join(dataset_folder, d))]

    for class_name in classes:
        class_path = os.path.join(dataset_folder, class_name)
        images = [img for img in os.listdir(class_path) if img.endswith(('.jpg', '.jpeg', '.png'))]
        
        # Shuffle gambar agar pemilihan acak
        random.shuffle(images)
        
        # Pastikan ada cukup gambar untuk split
        if len(images) < (train_size + valid_size + test_size):
            print(f"Not enough images in class {class_name} to split. Skipping this class.")
            continue
        
        # Buat folder train, valid, dan test jika belum ada
        train_folder = os.path.join(dataset_folder, 'train', class_name)
        valid_folder = os.path.join(dataset_folder, 'valid', class_name)
        test_folder = os.path.join(dataset_folder, 'test', class_name)

        os.makedirs(train_folder, exist_ok=True)
        os.makedirs(valid_folder, exist_ok=True)
        os.makedirs(test_folder, exist_ok=True)

        # Split dataset
        train_images = images[:train_size]
        valid_images = images[train_size:train_size + valid_size]
        test_images = images[train_size + valid_size:train_size + valid_size + test_size]

        # Copy gambar ke folder train
        for img in train_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(train_folder, img)
            shutil.move(src_path, dest_path)

        # Copy gambar ke folder valid
        for img in valid_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(valid_folder, img)
            shutil.move(src_path, dest_path)

        # Copy gambar ke folder test
        for img in test_images:
            src_path = os.path.join(class_path, img)
            dest_path = os.path.join(test_folder, img)
            shutil.move(src_path, dest_path)

        # Menghapus gambar yang tersisa
        remaining_images = images[train_size + valid_size + test_size:]
        for img in remaining_images:
            img_path = os.path.join(class_path, img)
            os.remove(img_path)

        print(f"Processed class {class_name} - Train: {len(train_images)}, Valid: {len(valid_images)}, Test: {len(test_images)}")

# Path ke dataset utama
dataset_path = 'Dataset'

# Split dataset menjadi train, valid, test
split_dataset(dataset_path)
