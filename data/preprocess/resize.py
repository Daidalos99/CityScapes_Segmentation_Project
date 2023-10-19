import os
from PIL import Image

# 이미지가 있는 경로 설정
image_dir = r"./data/test/labelIds"

# 이미지 파일들의 절대 경로 가져오기
image_files = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(".png")]

# 이미지 리사이즈
for image_file in image_files:
    image = Image.open(image_file)
    resized_image = image.resize((1024, 512))
    resized_image.save(image_file)
    print(f"Resized: {image_file}")

print("Resize complete.")