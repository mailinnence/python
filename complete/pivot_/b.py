# 스프라이트 시트 통일 코드드

from PIL import Image
import os

def create_sprite_sheet(folder_path):     # 1. 폴더 내의 이미지 파일들을 읽기
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_files.append(filename)
    if not image_files:
        print("이미지 파일을 찾을 수 없습니다.")
        return
    max_width = 0     # 2. 모든 이미지의 크기를 확인하여 최대 크기 찾기
    max_height = 0
    images = []
    for filename in image_files:
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        images.append(img)
        max_width = max(max_width, img.width)
        max_height = max(max_height, img.height)
    images_per_row = 10    # 3. 스프라이트 시트 생성을 위한 계산
    num_rows = (len(images) + images_per_row - 1) // images_per_row  # 올림 나눗셈
    sheet_width = max_width * images_per_row  # 최종 스프라이트 시트의 크기 계산
    sheet_height = max_height * num_rows
    sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))  # 새로운 이미지 생성 (투명 배경)
    for idx, img in enumerate(images):  # 이미지들을 스프라이트 시트에 배치
        row = idx // images_per_row
        col = idx % images_per_row
        x = col * max_width  # 각 이미지의 위치 계산
        y = row * max_height
        img = img.convert('RGBA') # 이미지가 투명 배경을 가지도록 RGBA로 변환
        sprite_sheet.paste(img, (x, y)) # 이미지를 시트에 붙여넣기
    output_path = os.path.join(folder_path, 'sprite_sheet.png') # 결과 저장
    sprite_sheet.save(output_path)
    print(f"스프라이트 시트가 생성되었습니다: {output_path}")
    print(f"시트 크기: {sheet_width}x{sheet_height}")
    print(f"개별 스프라이트 크기: {max_width}x{max_height}")
    print(f"총 스프라이트 수: {len(images)}")

# 사용 예시
if __name__ == "__main__":
    folder_path = "C:\\Users\\Donkey\\Desktop\\anaconda"  # 여기에 실제 스프라이트가 있는 폴더 경로를 입력하세요
    create_sprite_sheet(folder_path)