import cv2
import os
import albumentations as A

input_folder = 'dataset/rumah-hakim'  # folder asal
output_folder = 'dataset-aug/rumah-hakim-aug'  # folder hasil augmentasi
augment_per_image = 7

os.makedirs(output_folder, exist_ok=True)

# Transformasi untuk augmentasi
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=20, p=0.5),
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=15, p=0.5),
    A.Blur(p=0.2),
    A.Resize(224, 224)  # ukuran final (sama kayak ori)
])

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path)

        if image is None:
            print(f"⚠️ Gagal membaca: {filename}")
            continue

        basename = os.path.splitext(filename)[0]

        # Simpan gambar original (langsung copy aja, karena sudah 224x224)
        ori_out = os.path.join(output_folder, f"ori_{basename}.jpg")
        cv2.imwrite(ori_out, image)

        # Augmentasi
        for i in range(augment_per_image):
            augmented = transform(image=image)["image"]
            outname = f"{basename}_aug{i+1}.jpg"
            cv2.imwrite(os.path.join(output_folder, outname), augmented)

print("✅ Semua gambar ori + augment udah 224x224 dan konsisten. Jangan diacak-acak lagi yaa 😤💕")
