import os
from collections import deque
from PIL import Image

def create_custom_sprite_sheet(folder_path, sprite_width, sprite_height, image_files):
    images = []
    name = image_files[0][:-5]
    for filename in image_files:
        img_path = os.path.join(folder_path, filename)
        img = Image.open(img_path)
        img = img.convert('RGBA')
        new_img = Image.new('RGBA', (sprite_width, sprite_height), (0, 0, 0, 0))
        paste_x = (sprite_width - img.width) // 2
        paste_y = (sprite_height - img.height) // 2
        new_img.paste(img, (paste_x, paste_y))
        images.append(new_img)
    images_per_row = 5
    num_rows = (len(images) + images_per_row - 1) // images_per_row
    sheet_width = sprite_width * images_per_row
    sheet_height = sprite_height * num_rows
    sprite_sheet = Image.new('RGBA', (sheet_width, sheet_height), (0, 0, 0, 0))
    for idx, img in enumerate(images):
        row = idx // images_per_row
        col = idx % images_per_row
        x = col * sprite_width
        y = row * sprite_height
        sprite_sheet.paste(img, (x, y))
    output_path = os.path.join(folder_path, 'custom_sprite_sheet.png')
    sprite_sheet.save(output_path)
    print(f"스프라이트 시트가 생성되었습니다: {output_path}")
    print(f"시트 크기: {sheet_width}x{sheet_height}")
    print(f"개별 스프라이트 크기: {sprite_width}x{sprite_height}")
    print(f"총 스프라이트 수: {len(images)}")


def go():
    folder_path = "C:\\Users\\Donkey\\Desktop\\anaconda"
    image_extensions = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff"}
    try:
        files = os.listdir(folder_path)
        image_files = [f for f in files if os.path.splitext(f)[1].lower() in image_extensions]
        image_files.sort(key=lambda x: int(''.join(filter(str.isdigit, x))) if any(c.isdigit() for c in x) else x)
        image_queue = deque(image_files)
        print("이미지 파일 목록:")
        for img in image_queue:
            print(img)
        create_custom_sprite_sheet(folder_path, 218, 123, image_queue)
    except FileNotFoundError:
        print("폴더를 찾을 수 없습니다.")


go()
