"""ini buat resize gambar jadi 640x640 (input yolo) untuk semua gambar di folder 
dataset dimana strukutur datasetnya seperti berikut
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
import cv2

# Fungsi untuk mengubah ukuran gambar menjadi 640x640
def resize_image(image, target_size=(640, 640)):
    return cv2.resize(image, target_size)

# Fungsi untuk meresize semua gambar dalam dataset
def resize_dataset(dataset_folder, target_size=(640, 640)):
    # Loop melalui folder train, valid, dan test
    for split in ['train', 'valid', 'test']:
        split_folder = os.path.join(dataset_folder, split)
        
        # Loop melalui setiap kelas dalam folder (train, valid, test)
        for class_name in os.listdir(split_folder):
            class_folder = os.path.join(split_folder, class_name)
            
            # Pastikan hanya memproses folder yang berisi gambar
            if os.path.isdir(class_folder):
                # Loop melalui semua gambar dalam setiap kelas
                for img_name in os.listdir(class_folder):
                    if img_name.endswith(('.jpg', '.jpeg', '.png')):
                        img_path = os.path.join(class_folder, img_name)
                        img = cv2.imread(img_path)
                        
                        if img is not None:
                            # Ubah ukuran gambar menjadi 640x640
                            resized_img = resize_image(img, target_size)

                            # Simpan kembali gambar yang sudah diubah ukurannya
                            cv2.imwrite(img_path, resized_img)
                            print(f"Resized {img_name} in {class_name}/{split} to {target_size}")
                        else:
                            print(f"Failed to load image: {img_name}")

# Path ke folder dataset
dataset_folder = 'Dataset-Athaya-4.0-resize'  # Ganti dengan path yang benar ke dataset

# Jalankan fungsi untuk meresize gambar dalam dataset
resize_dataset(dataset_folder)
