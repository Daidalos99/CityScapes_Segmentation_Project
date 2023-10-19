import cv2

# 입력 비디오 파일 경로
input_video_path = 'C:/Users/daida/Desktop/DL_Project/data/video_test/black_box.mp4'

# 출력 비디오 파일 경로
output_video_path = 'C:/Users/daida/Desktop/DL_Project/data/video_test/black_box_128.mp4'

# 리사이즈할 크기
resize_width = 128
resize_height = 128

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(input_video_path)

# 입력 비디오의 프레임 속성 가져오기
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
fps = int(cap.get(5))

print(frame_width, frame_height, fps)

# 비디오 출력 객체 생성
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_video_path, fourcc, fps, (resize_width, resize_height))

while True:
    # 프레임 읽기
    ret, frame = cap.read()
    if not ret:
        break

    # 프레임을 지정된 크기로 리사이즈
    frame = cv2.resize(frame, (resize_width, resize_height), interpolation=cv2.INTER_LANCZOS4)

    # 리사이즈된 프레임을 출력 비디오에 쓰기
    out.write(frame)

# 비디오 파일 닫기
cap.release()
out.release()

print("Video resize completed!!")

# 창 닫기
cv2.destroyAllWindows()