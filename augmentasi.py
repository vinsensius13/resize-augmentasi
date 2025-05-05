import cv2
import os
import albumentations as A

input_folder = 'foto-masjid'
output_folder = 'foto_masjid_aug'
augment_per_image = 5  # berapa augmentasi tiap gambar

# Bikin folder output kalau belum ada
os.makedirs(output_folder, exist_ok=True)

# Define transformasi
transform = A.Compose([
    A.HorizontalFlip(p=0.5),
    A.RandomBrightnessContrast(p=0.5),
    A.Rotate(limit=20, p=0.5),
    A.ShiftScaleRotate(shift_limit=0.05, scale_limit=0.1, rotate_limit=15, p=0.5),
    A.Blur(p=0.2),
    A.RandomCrop(height=280, width=280, p=0.3),
    A.Resize(300, 300)  # supaya tetap 300x300
])

# Loop setiap gambar
for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        img_path = os.path.join(input_folder, filename)
        image = cv2.imread(img_path)
        basename = os.path.splitext(filename)[0]

        for i in range(augment_per_image):
            augmented = transform(image=image)['image']
            outname = f"{basename}_aug{i+1}.jpg"
            cv2.imwrite(os.path.join(output_folder, outname), augmented)

print("Augmentasi selesai, puas kan?! 😤")
