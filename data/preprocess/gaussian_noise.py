import os
import cv2
import numpy as np

input_folder = "./data/train/leftImg"
output_folder = "./data/train/augmentation/leftImg"

# input_folder = "./data/train/labelIds"
# output_folder = "./data/train/augmentation/labelIds"

# 저장할 폴더가 없다면 생성
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 원본 이미지 폴더 내의 모든 이미지 파일에 대해 가우시안 노이즈 적용 후 저장
for filename in os.listdir(input_folder):
    image_path = os.path.join(input_folder, filename)
    output_path = os.path.join(output_folder, filename)

    # 이미지 불러오기
    image = cv2.imread(image_path)

    # 가우시안 노이즈 생성
    noise = np.random.normal(0, 0.6, image.shape).astype(np.uint8)

    # 원본 이미지에 노이즈 추가
    noisy_image = cv2.add(image, noise)

    # 노이즈가 적용된 이미지 저장
    cv2.imwrite(output_path, noisy_image)

    print(f"Saved noisy image: {output_path}")