import os
import shutil

# Fungsi untuk mengubah struktur dataset
def restructure_dataset(base_dir, output_dir):
    os.makedirs(output_dir, exist_ok=True)
    
    # Folder untuk image dan label train, valid, dan test
    images_train_dir = os.path.join(output_dir, 'images', 'train')
    labels_train_dir = os.path.join(output_dir, 'labels', 'train')
    images_valid_dir = os.path.join(output_dir, 'images', 'valid')
    labels_valid_dir = os.path.join(output_dir, 'labels', 'valid')
    images_test_dir = os.path.join(output_dir, 'images', 'test')
    labels_test_dir = os.path.join(output_dir, 'labels', 'test')

    # Buat direktori baru untuk train, valid, test
    os.makedirs(images_train_dir, exist_ok=True)
    os.makedirs(labels_train_dir, exist_ok=True)
    os.makedirs(images_valid_dir, exist_ok=True)
    os.makedirs(labels_valid_dir, exist_ok=True)
    os.makedirs(images_test_dir, exist_ok=True)
    os.makedirs(labels_test_dir, exist_ok=True)

    # Fungsi untuk memindahkan file
    def move_files(src_img_dir, src_label_dir, dest_img_dir, dest_label_dir):
        for class_name in os.listdir(src_img_dir):
            class_img_dir = os.path.join(src_img_dir, class_name)
            class_label_dir = os.path.join(src_label_dir, class_name)

            for img_file in os.listdir(class_img_dir):
                if img_file.endswith(('.jpg', '.jpeg', '.png')):
                    # Pindahkan gambar
                    src_img_path = os.path.join(class_img_dir, img_file)
                    dest_img_path = os.path.join(dest_img_dir, img_file)
                    shutil.move(src_img_path, dest_img_path)

                    # Pindahkan label yang sesuai
                    label_file = img_file.replace('.jpg', '.txt').replace('.jpeg', '.txt').replace('.png', '.txt')
                    src_label_path = os.path.join(class_label_dir, label_file)
                    dest_label_path = os.path.join(dest_label_dir, label_file)

                    if os.path.exists(src_label_path):
                        shutil.move(src_label_path, dest_label_path)

    # Pindahkan file untuk train
    train_img_dir = os.path.join(base_dir, 'train')
    train_label_dir = os.path.join(base_dir, 'labels')
    move_files(train_img_dir, train_label_dir, images_train_dir, labels_train_dir)

    # Pindahkan file untuk valid
    valid_img_dir = os.path.join(base_dir, 'valid')
    valid_label_dir = os.path.join(base_dir, 'labels-valid')
    move_files(valid_img_dir, valid_label_dir, images_valid_dir, labels_valid_dir)

    # Pindahkan file untuk test
    test_img_dir = os.path.join(base_dir, 'test')
    test_label_dir = os.path.join(base_dir, 'labels')
    move_files(test_img_dir, test_label_dir, images_test_dir, labels_test_dir)

    print(f"Dataset successfully restructured and moved to {output_dir}")

# Fungsi untuk membuat file data.yaml
def create_data_yaml(output_dir, num_classes):
    data_yaml_content = f"""
train: {os.path.join(output_dir, 'images', 'train')}
val: {os.path.join(output_dir, 'images', 'valid')}
test: {os.path.join(output_dir, 'images', 'test')}

nc: {num_classes}  # Jumlah kelas

names: ['actinic keratosis', 'basal cell carcinoma', 'melanoma', 'nevus', 'pigmented benign keratosis', 'seborrheic keratosis', 'squamous cell carcinoma', 'uncategorized']  # Ganti sesuai kelas Anda
"""
    with open(os.path.join(output_dir, 'data.yaml'), 'w') as f:
        f.write(data_yaml_content)
    print(f"data.yaml created at {output_dir}")

# Path ke folder Dataset-Athaya
base_dir = 'Dataset-Athaya'
output_dir = 'Dataset-Athaya-YOLOv8'
num_classes = 8  # Jumlah kelas Anda

# Jalankan fungsi untuk restrukturisasi dataset dan pembuatan file data.yaml
restructure_dataset(base_dir, output_dir)
create_data_yaml(output_dir, num_classes)
