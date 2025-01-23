""""
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


dengan struktur datase seperti di atas, buatkan code untuk memindahkan 10 gambar dari 
setiap kelas di folder valid ke kelas di folder test
"""



import os
import shutil
import random

# Fungsi untuk memindahkan 10 gambar dari valid ke test
def move_images(valid_folder, test_folder, num_images=10):
    # Loop melalui setiap kelas di folder valid
    for class_name in os.listdir(valid_folder):
        class_valid_folder = os.path.join(valid_folder, class_name)
        class_test_folder = os.path.join(test_folder, class_name)

        # Pastikan folder kelas di test ada, jika tidak buat
        os.makedirs(class_test_folder, exist_ok=True)

        # Dapatkan daftar gambar di folder valid
        images = [img for img in os.listdir(class_valid_folder) if img.endswith(('.jpg', '.jpeg', '.png'))]
        
        # Jika jumlah gambar kurang dari num_images, gunakan seluruh gambar
        if len(images) < num_images:
            num_images = len(images)

        # Pilih 10 gambar secara acak
        images_to_move = random.sample(images, num_images)

        # Pindahkan gambar ke folder test
        for img in images_to_move:
            src_path = os.path.join(class_valid_folder, img)
            dest_path = os.path.join(class_test_folder, img)
            shutil.move(src_path, dest_path)
            print(f"Moved {img} from {class_valid_folder} to {class_test_folder}")

# Path ke folder valid dan test
valid_folder = 'Dataset-Athaya/valid'
test_folder = 'Dataset-Athaya/test'

# Pindahkan 10 gambar dari valid ke test untuk setiap kelas
move_images(valid_folder, test_folder, num_images=10)
