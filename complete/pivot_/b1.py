from PIL import Image
import os

def find_largest_image_size(folder_path): # 최대 크기를 저장할 변수 초기화
    max_width = 0
    max_height = 0
    largest_file = ""
    for filename in os.listdir(folder_path): # 폴더 내의 모든 이미지 파일 확인
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')): # 이미지 파일 확장자 체크
            img_path = os.path.join(folder_path, filename)
            with Image.open(img_path) as img:             # 이미지 열기
                if img.width > max_width or img.height > max_height: # 현재 이미지가 더 크다면 최대 크기 업데이트
                    max_width = max(max_width, img.width)
                    max_height = max(max_height, img.height)
                    largest_file = filename
    print(f"가장 큰 이미지 크기: {max_width}x{max_height}")
    print(f"해당 파일: {largest_file}")
    return max_width, max_height


# 사용 예시
if __name__ == "__main__":
    folder_path = "C:\\Users\\Donkey\\Desktop\\anaconda"  # 여기에 실제 스프라이트가 있는 폴더 경로를 입력하세요
    find_largest_image_size(folder_path)