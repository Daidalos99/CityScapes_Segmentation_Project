import os
from PIL import Image

# input_folder = "./data/train/leftImg"
# output_folder = "./data/train/augmentation/leftImg"

input_folder = "./data/train/labelIds"
output_folder = "./data/train/augmentation/labelIds"

# 저장할 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 원본 이미지 폴더 내의 모든 이미지 파일에 대해 뒤집은 후 저장
for filename in os.listdir(input_folder):
    image_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # 이미지 불러오기
    image = Image.open(image_path)

    # 이미지 뒤집기
    flipped_image = image.transpose(Image.FLIP_LEFT_RIGHT)

    # 뒤집힌 이미지 저장
    flipped_image.save(output_path)

    print(f"Saved flipped image: {output_path}")