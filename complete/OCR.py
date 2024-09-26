
# V_2 ---- 사진 비업로드 시 같은 폴더 안에 1.png 파일 자동 초기화 ----------------------------- 
import os
import tkinter as tk
from PIL import Image
import pytesseract
from tkinter import filedialog, messagebox

# os 에 맞게 다운받을 것
# https://github.com/UB-Mannheim/tesseract/wiki

# 라이브러리 자동 설치 ---------------------------------------------
try:
    import pytesseract
except ImportError:
    try:
        os.system("pip install pytesseract")
    except Exception as e:
        pass
# ------------------------------------------------------------------

filepath = ""  # 파일 경로를 전역 변수로 정의

# 파일 경로 초기화 함수
def initialize_filepath():
    global filepath
    if not filepath:  # 파일 경로가 비어 있을 경우
        default_file = os.path.join(os.getcwd(), "1.png")
        if os.path.exists(default_file):
            filepath = default_file
            selected_file_label.config(text="선택된 파일: " + filepath)  # 파일 경로를 업데이트
        else:
            # messagebox.showerror("오류", "1.png 파일이 존재하지 않습니다.")
            selected_file_label.config(text="선택된 파일: 없음")  # 파일 경로 없음으로 표시

def open_file_explorer():
    global filepath  # 전역 변수로 선언
    # 파일 탐색기 열기
    filepath = filedialog.askopenfilename()
    filepath = filepath.replace("/", "\\")
    selected_file_label.config(text="선택된 파일: " + filepath)  # 파일 경로를 업데이트

def OCR_RUN():
    global filepath  # 전역 변수로 선언
    if not filepath:
        messagebox.showerror("오류", "파일을 선택하세요.")
        return
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    try:
        text = pytesseract.image_to_string(Image.open(filepath), lang='Eng+kor')
        # 결과를 텍스트 위젯에 표시
        text_output.delete(1.0, tk.END)  # 이전 내용 지우기
        text_output.insert(tk.END, text)  # 새 텍스트 삽입
    except Exception as e:
        messagebox.showerror("오류", "OCR 처리 중 오류가 발생했습니다.\n" + str(e))

# Tkinter 애플리케이션을 생성합니다.
root = tk.Tk()
root.title("OCR Program")  # 창의 제목 설정
root.geometry("800x700+100+50")  # 가로 800픽셀, 세로 700픽셀 크기로 조절

# 파일 탐색기 열기 버튼 생성
file_explorer_button = tk.Button(root, text="파일 탐색기 열기", command=open_file_explorer)
file_explorer_button.pack(pady=10)

# 선택된 파일 경로를 표시할 텍스트 레이블 생성
selected_file_label = tk.Label(root, text="선택된 파일: ")
selected_file_label.pack(pady=5)

# OCR 실행 버튼 생성
ocr_button = tk.Button(root, text="OCR 실행", command=OCR_RUN)
ocr_button.pack(pady=5)

# OCR 결과를 표시할 텍스트 위젯 생성
text_output = tk.Text(root, wrap='word', height=42, width=105)
text_output.pack(pady=10)

# 파일 경로 초기화 호출
initialize_filepath()

# 창을 띄웁니다.
root.mainloop()



















# V_1 --------------------------------------------------------------------------------------------------------------------------
import os
import tkinter as tk
from PIL import Image
import pytesseract
from tkinter import filedialog, messagebox

# os 에 맞게 다운받을 것
# https://github.com/UB-Mannheim/tesseract/wiki

# 라이브러리 자동 설치 ---------------------------------------------
try:
    import pytesseract
except ImportError:
    try:
        os.system("pip install pytesseract")
    except Exception as e:
        pass
# ------------------------------------------------------------------

filepath = ""  # 파일 경로를 전역 변수로 정의

def open_file_explorer():
    global filepath  # 전역 변수로 선언
    # 파일 탐색기 열기
    filepath = filedialog.askopenfilename()
    filepath = filepath.replace("/", "\\")
    selected_file_label.config(text="선택된 파일: " + filepath)  # 파일 경로를 업데이트

def OCR_RUN():
    global filepath  # 전역 변수로 선언
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    text = pytesseract.image_to_string(Image.open(filepath), lang='Eng+kor')
    
    # 결과를 텍스트 위젯에 표시
    text_output.delete(1.0, tk.END)  # 이전 내용 지우기
    text_output.insert(tk.END, text)  # 새 텍스트 삽입

# Tkinter 애플리케이션을 생성합니다.
root = tk.Tk()
root.title("OCR Program")  # 창의 제목 설정
root.geometry("800x700+100+50")  # 가로 700픽셀, 세로 600픽셀 크기로 조절

# 파일 탐색기 열기 버튼 생성
file_explorer_button = tk.Button(root, text="파일 탐색기 열기", command=open_file_explorer)
file_explorer_button.pack(pady=10)

# 선택된 파일 경로를 표시할 텍스트 레이블 생성
selected_file_label = tk.Label(root, text="선택된 파일: ")
selected_file_label.pack(pady=5)

# OCR 실행 버튼 생성
ocr_button = tk.Button(root, text="OCR 실행", command=OCR_RUN)
ocr_button.pack(pady=5)

# OCR 결과를 표시할 텍스트 위젯 생성
text_output = tk.Text(root, wrap='word', height=42, width=105)
text_output.pack(pady=10)

# 창을 띄웁니다.
root.mainloop()
