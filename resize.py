from PIL import Image
import os
from tqdm import tqdm

input_root = 'dataset'  # <-- folder asal
output_root = 'dataset_224x'  # <-- folder hasil resize
size = (224, 224)

# Bikin folder output utama
os.makedirs(output_root, exist_ok=True)

# Loop semua folder class
for class_name in tqdm(os.listdir(input_root), desc="Resize per class"):
    class_input_path = os.path.join(input_root, class_name)
    class_output_path = os.path.join(output_root, class_name)

    if not os.path.isdir(class_input_path):
        continue  # skip file

    os.makedirs(class_output_path, exist_ok=True)

    for filename in os.listdir(class_input_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
            input_path = os.path.join(class_input_path, filename)
            output_path = os.path.join(class_output_path, filename)

            try:
                img = Image.open(input_path).convert('RGB')
                img = img.resize(size)
                img.save(output_path)
            except Exception as e:
                print(f"⚠️ Error processing {filename} in {class_name}: {e}")

print("✅ Semua gambar udah resize ke 224x224. Siap training lagi nggak nih?! 😤💕")
