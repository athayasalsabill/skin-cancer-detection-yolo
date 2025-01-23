import os
import shutil

# Folder asal dataset
dataset_dir = 'C:/file D/Teknik Elektro/Riset Skin Cancer Claassification/dataset dari open source/SkinLesionDetection.v2i.yolov8'

# Path folder train, valid, test
folders = ['train', 'valid', 'test']

# Folder tujuan baru
new_images_dir = os.path.join(dataset_dir, 'images')
new_labels_dir = os.path.join(dataset_dir, 'labels')

# Membuat folder baru jika belum ada
os.makedirs(new_images_dir, exist_ok=True)
os.makedirs(new_labels_dir, exist_ok=True)

# Fungsi untuk membaca digit pertama dari file label .txt dan memindahkan gambar dan label
def process_files(src_images_dir, src_labels_dir):
    for label_file in os.listdir(src_labels_dir):
        if label_file.endswith('.txt'):
            label_path = os.path.join(src_labels_dir, label_file)

            # Membaca digit pertama dari file label .txt
            with open(label_path, 'r') as f:
                first_digit = f.readline().split()[0]

            # Membuat folder untuk kelas (class1, class2, dll.) berdasarkan digit pertama
            class_folder_images = os.path.join(new_images_dir, f'class{first_digit}')
            class_folder_labels = os.path.join(new_labels_dir, f'class{first_digit}')
            os.makedirs(class_folder_images, exist_ok=True)
            os.makedirs(class_folder_labels, exist_ok=True)

            # Path gambar dan label asal
            image_file = label_file.replace('.txt', '.jpg')  # Sesuaikan dengan ekstensi gambar Anda
            image_path = os.path.join(src_images_dir, image_file)

            # Pindahkan gambar dan file label ke folder yang sesuai
            if os.path.exists(image_path):
                shutil.move(image_path, os.path.join(class_folder_images, image_file))
            shutil.move(label_path, os.path.join(class_folder_labels, label_file))

# Proses setiap folder (train, valid, test)
for folder in folders:
    images_dir = os.path.join(dataset_dir, folder, 'images')
    labels_dir = os.path.join(dataset_dir, folder, 'labels')

    process_files(images_dir, labels_dir)

print("Dataset restructuring completed successfully.")
