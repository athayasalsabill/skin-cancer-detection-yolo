"""
menghitung gambar setiap kelas dengan struktur seperti ini:
├── Dataset
│   ├── class1 
|            ├── img1.jpg
|            ├── img2.jpg
│   ├── class2 
|            ├── img1.jpg
|            ├── img2.jpg 
"""

import os

# Fungsi untuk menghitung jumlah gambar di setiap kelas
def count_images_in_classes(root_folder):
    class_counts = {}
    
    # Loop melalui setiap subfolder (kelas)
    for class_name in os.listdir(root_folder):
        class_folder = os.path.join(root_folder, class_name)
        
        if os.path.isdir(class_folder):
            # Hitung jumlah gambar dalam subfolder yang merupakan kelas
            num_images = len([img for img in os.listdir(class_folder) if img.endswith(('.jpg', '.jpeg', '.png'))])
            class_counts[class_name] = num_images
    
    return class_counts

# Path ke folder train
train_folder = 'ISIC Archive'

# Hitung jumlah gambar di setiap kelas
class_counts = count_images_in_classes(train_folder)

# Cetak hasil
for class_name, count in class_counts.items():
    print(f"Class {class_name}: {count} images")
