import os
import shutil

# Fungsi untuk mengganti class_id di file label
def update_class_id(label_file, old_class_id, new_class_id):
    with open(label_file, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        class_id, *rest = line.strip().split()
        if class_id == str(old_class_id):
            class_id = str(new_class_id)
        new_lines.append(f"{class_id} " + " ".join(rest) + "\n")

    with open(label_file, 'w') as f:
        f.writelines(new_lines)

# Fungsi untuk menyalin gambar dan label serta mengganti class_id
def copy_and_update_class(src_images_dir, src_labels_dir, dst_images_dir, dst_labels_dir, old_class_id, new_class_id, max_count):
    os.makedirs(dst_images_dir, exist_ok=True)
    os.makedirs(dst_labels_dir, exist_ok=True)
    
    count = 0
    for label_file in os.listdir(src_labels_dir):
        label_path = os.path.join(src_labels_dir, label_file)
        with open(label_path, 'r') as f:
            lines = f.readlines()
        
        # Jika file label mengandung class_id yang dicari
        if any(line.startswith(str(old_class_id)) for line in lines):
            # Salin gambar dan label
            image_file = label_file.replace('.txt', '.jpg')  # Asumsikan ekstensi gambar .jpg
            src_image_path = os.path.join(src_images_dir, image_file)
            dst_image_path = os.path.join(dst_images_dir, image_file)

            # Salin file gambar dan label
            shutil.copyfile(src_image_path, dst_image_path)
            shutil.copyfile(label_path, os.path.join(dst_labels_dir, label_file))
            
            # Update class_id di file label
            update_class_id(os.path.join(dst_labels_dir, label_file), old_class_id, new_class_id)

            count += 1
            if count >= max_count:
                break

# Path dataset asli
src_base_dir = 'Dataset-Athaya-3.0-yolov8'
src_train_images_dir = os.path.join(src_base_dir, 'train', 'images')
src_train_labels_dir = os.path.join(src_base_dir, 'train', 'labels')
src_valid_images_dir = os.path.join(src_base_dir, 'valid', 'images')
src_valid_labels_dir = os.path.join(src_base_dir, 'valid', 'labels')
src_test_images_dir = os.path.join(src_base_dir, 'test', 'images')
src_test_labels_dir = os.path.join(src_base_dir, 'test', 'labels')

# Path tujuan
dst_base_dir = 'Dataset-Athaya-SK-SL'
dst_train_images_dir = os.path.join(dst_base_dir, 'train', 'images')
dst_train_labels_dir = os.path.join(dst_base_dir, 'train', 'labels')
dst_valid_images_dir = os.path.join(dst_base_dir, 'valid', 'images')
dst_valid_labels_dir = os.path.join(dst_base_dir, 'valid', 'labels')
dst_test_images_dir = os.path.join(dst_base_dir, 'test', 'images')
dst_test_labels_dir = os.path.join(dst_base_dir, 'test', 'labels')

# Copy gambar dan label untuk train, valid, test dengan batasan
copy_and_update_class(src_train_images_dir, src_train_labels_dir, dst_train_images_dir, dst_train_labels_dir, 6, 8, max_count=2000)
copy_and_update_class(src_train_images_dir, src_train_labels_dir, dst_train_images_dir, dst_train_labels_dir, 7, 9, max_count=2000)

copy_and_update_class(src_valid_images_dir, src_valid_labels_dir, dst_valid_images_dir, dst_valid_labels_dir, 6, 8, max_count=200)
copy_and_update_class(src_valid_images_dir, src_valid_labels_dir, dst_valid_images_dir, dst_valid_labels_dir, 7, 9, max_count=200)

copy_and_update_class(src_test_images_dir, src_test_labels_dir, dst_test_images_dir, dst_test_labels_dir, 6, 8, max_count=50)
copy_and_update_class(src_test_images_dir, src_test_labels_dir, dst_test_images_dir, dst_test_labels_dir, 7, 9, max_count=50)

print("Copy dan update class_id selesai.")
