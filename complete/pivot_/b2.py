from PIL import Image
import os

def create_custom_sprite_sheet(folder_path, sprite_width, sprite_height):       # 1. 폴더 내의 이미지 파일들을 읽기
    image_files = []
    for filename in os.listdir(folder_path):
        if filename.endswith(('.png', '.jpg', '.jpeg', '.gif')):
            image_files.append(filename)
    if not image_files:
        print("이미지 파일을 찾을 수 없습니다.")
        return
    images = []                                                                 # 2. 이미지들을 지정된 크기로 처리
    for filename in image_files:
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        img = img.convert('RGBA')                                                # 이미지를 RGBA로 변환 (투명도 지원)
        new_img = Image.new('RGBA', (sprite_width, sprite_height), (0, 0, 0, 0)) # 새로운 크기의 투명한 이미지 생성
        paste_x = (sprite_width - img.width) // 2                                # 원본 이미지를 새 이미지의 중앙에 배치
        paste_y = (sprite_height - img.height) // 2
        new_img.paste(img, (paste_x, paste_y))
        images.append(new_img)
    images_per_row = 5                                                        # 3. 스프라이트 시트 생성을 위한 계산
    num_rows = (len(images) + images_per_row - 1) // images_per_row
    sheet_width = sprite_width * images_per_row                                 # 최종 스프라이트 시트의 크기 계산
    sheet_height = sprite_height * num_rows
    sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))  # 새로운 이미지 생성 (투명 배경)
    for idx, img in enumerate(images):                                           # 이미지들을 스프라이트 시트에 배치
        row = idx // images_per_row
        col = idx % images_per_row
        x = col * sprite_width
        y = row * sprite_height
        sprite_sheet.paste(img, (x, y))
    output_path = os.path.join(folder_path, 'custom_sprite_sheet.png')          # 결과 저장
    sprite_sheet.save(output_path)
    print(f"스프라이트 시트가 생성되었습니다: {output_path}")
    print(f"시트 크기: {sheet_width}x{sheet_height}")
    print(f"개별 스프라이트 크기: {sprite_width}x{sprite_height}")
    print(f"총 스프라이트 수: {len(images)}")






# 사용 예시
if __name__ == "__main__":
    folder_path = "C:\\Users\\Donkey\\Desktop\\anaconda"
    width = 218
    height = 123
    create_custom_sprite_sheet(folder_path, width, height)

'''
(218, 123)
'''