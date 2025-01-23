import os

# Fungsi untuk mengganti digit pertama yang bernilai -1 menjadi 4 dalam file label YOLO
def replace_negative_class_id(label_dir):
    # Loop melalui semua file .txt di dalam direktori
    for label_file in os.listdir(label_dir):
        if label_file.endswith('.txt'):
            label_path = os.path.join(label_dir, label_file)
            
            # Baca isi file label
            with open(label_path, 'r') as f:
                lines = f.readlines()

            # Ganti digit pertama (class_id) yang bernilai -1 menjadi 4
            modified_lines = []
            for line in lines:
                line_parts = line.split()
                if line_parts and line_parts[0] == '-1':
                    line_parts[0] = '4'  # Ubah class_id dari -1 menjadi 4
                modified_lines.append(" ".join(line_parts) + "\n")

            # Tulis ulang file label dengan perubahan
            with open(label_path, 'w') as f:
                f.writelines(modified_lines)

    print(f"Processed labels in {label_dir}")

# Path ke folder Dataset-Athaya-YOLOv8
dataset_base_dir = 'Dataset-Athaya-YOLOv8'

# Proses folder train/labels dan valid/labels
train_labels_dir = os.path.join(dataset_base_dir, 'train', 'labels')
valid_labels_dir = os.path.join(dataset_base_dir, 'valid', 'labels')

# Jalankan fungsi untuk kedua folder
replace_negative_class_id(train_labels_dir)
replace_negative_class_id(valid_labels_dir)
