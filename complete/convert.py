import os
from moviepy.editor import *

def convert_videos_to_wav(input_folder, output_folder):
    # 폴더가 없으면 생성
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    for filename in os.listdir(input_folder):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, os.path.splitext(filename)[0] + '.wav')
        if input_path.endswith(('.mp4', '.avi', '.mkv', '.mpeg')):
            try:
                video = VideoFileClip(input_path)
                audio = video.audio
                audio.write_audiofile(output_path)
                print(f"{filename} 변환 완료")
            except Exception as e:
                print(f"{filename} 변환 실패: {str(e)}")




# 입력 폴더와 출력 폴더 경로 설정
input_folder = "C:\\Users\\user\\OneDrive\\바탕 화면\\새 폴더"
output_folder = "C:\\Users\\user\\OneDrive\\바탕 화면\\새 폴더2"

# 영상 파일을 WAV로 변환
convert_videos_to_wav(input_folder, output_folder)
