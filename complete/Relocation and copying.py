import os
import tkinter as tk

from tkinter import filedialog, messagebox
import pyperclip  # 클립보드 복사를 위한 라이브러리






def translate_ko():
    # 텍스트 창의 내용 가져오기
    text_to_translate = text_output.get(1.0, tk.END).strip()
    text_to_translate = "".join(text_to_translate.splitlines())
    print(text_to_translate)

    if not text_to_translate:
        messagebox.showerror("오류", "번역할 텍스트가 없습니다.")
        return
    
    try:
        pyperclip.copy(text_to_translate)
        text_output.delete(1.0, tk.END)  # 기존 텍스트 삭제
        text_output.insert(tk.END, text_to_translate)  # 번역된 텍스트 삽입
        
    except Exception as e:
        messagebox.showerror("번역 오류", f"번역 중 오류가 발생했습니다.\n{str(e)}")




def change_text_size(event=None):
    try:
        # Spinbox 값을 가져와서 기본 크기(10)에 더함
        size = int(spinbox.get()) + 10  # 기본 크기를 10으로 설정
        # 텍스트 위젯의 폰트 크기 변경
        current_font = ('TkDefaultFont', size)
        text_output.configure(font=current_font)
    except ValueError:
        # Spinbox 값이 숫자가 아닌 경우 처리
        messagebox.showerror("오류", "올바른 숫자를 입력하세요.")
        spinbox.delete(0, tk.END)
        spinbox.insert(0, "0")



def on_window_resize(event=None):
    # 창 크기에 맞춰 텍스트 영역 조정
    # 위쪽 버튼들과 레이블을 위한 공간을 고려하여 높이 조정
    window_width = root.winfo_width()
    window_height = root.winfo_height()
    
    # 텍스트 창의 새로운 크기 계산
    # 위쪽 여백(120px)을 남기고 아래쪽 여백(20px)을 고려
    new_height = (window_height - 140) // 20  # 폰트 크기를 고려한 라인 수 계산
    new_width = (window_width - 40) // 8  # 평균 문자 폭을 고려한 너비 계산
    
    text_output.config(height=new_height, width=new_width)





# Tkinter 애플리케이션 생성
root = tk.Tk()
root.title("Relocation and copying")
root.geometry("300x200+100+50")

# 최소 창 크기 설정
root.minsize(300, 200)

# 상단 프레임 (고정 높이)
top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, padx=10, pady=5)



# 버튼을 수평으로 배치하기 위한 프레임
button_frame = tk.Frame(top_frame)
button_frame.pack(pady=5)


translate_button = tk.Button(button_frame, text="재배치 및 복사", command=translate_ko)
translate_button.pack(side=tk.LEFT, padx=5)


# Spinbox 추가
spinbox = tk.Spinbox(button_frame, from_=0, to=100, width=5, increment=5  ,command=change_text_size)
spinbox.pack(side=tk.LEFT, padx=2)
spinbox.delete(0, tk.END)
spinbox.insert(0, "0")

# Spinbox 값 변경 시 텍스트 크기 변경을 위한 바인딩 추가
spinbox.bind('<Return>', change_text_size)  # Enter 키 입력 시
spinbox.bind('<FocusOut>', change_text_size)  # 포커스 잃을 때



# 텍스트 출력을 위한 프레임 (반응형)
text_frame = tk.Frame(root)
text_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

# OCR 결과 텍스트 위젯 (스크롤바 추가)
text_output = tk.Text(text_frame, wrap=tk.WORD)
scrollbar = tk.Scrollbar(text_frame, orient=tk.VERTICAL, command=text_output.yview)
text_output.configure(yscrollcommand=scrollbar.set)




# 텍스트 위젯과 스크롤바 배치
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
text_output.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# 창 크기 조절 이벤트 바인딩
root.bind('<Configure>', on_window_resize)


# 초기 크기 조정 실행
on_window_resize()

# 메인 루프 실행
root.mainloop()
