import os

folder_path = "C:/Users/daida/Desktop/CityScapes_Segmentation_Project/data/dataset/test/leftImg"

new_prefix = ""  # Specify the new prefix for the filenames

counter = 1 # 시작 숫자 몇번부터?
for filename in os.listdir(folder_path):
    if filename.endswith(".jpg"):
        new_filename = f"{new_prefix}{counter:03d}.jpg" # 숫자 이름 몇 자리로 할건지
        os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
        counter += 1