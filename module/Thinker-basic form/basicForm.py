from datetime import datetime
import tkinter
import os
import time
window=tkinter.Tk()
window.title("Sound Seperate Program")
window.geometry("900x620+100+100")
window.resizable(True, True)




class main:
    def __init__(self):
        self.selectNum=2
    def mainpage(self):
        #버튼으로 지우는 함수
        def page1():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            page1.pack_forget()
            page2.pack_forget()
            page3.pack_forget()
            main().page1()
        def page2():
            #place 지우는 함수
            fbutton1.pack_forget()
            fbutton2.pack_forget()
            #pack 지우는 함수
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginTwo1.pack_forget()
            marginTwo2.pack_forget()
            marginTwo3.pack_forget()
            page1.pack_forget()
            page2.pack_forget()
            page3.pack_forget()
            main().page2()
            
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
                if num==3:
                    os.startfile('folder3')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
                if num==3:
                    os.system('nautilus folder3')
                    
        #메뉴바 초기화
        menubar=tkinter.Menu(window)
        menu_1=tkinter.Menu(menubar, tearoff=0)
        window.config(menu=menubar)
        #한칸띄우기 용 위젯
        marginTwo1=tkinter.Label(window, height=10)
        marginTwo2=tkinter.Label(window, width=10 )
        marginTwo3=tkinter.Label(window, width=10 )
        marginTwo1.pack()
        #메인 테마 라벨
        marginOne1=tkinter.Label(window, text="Title")
        marginOne1.configure(font=("", 40, ""))
        marginOne1.pack()
        #plaintext
        marginOne2=tkinter.Label(window, height=5 ,text="explain text")
        marginOne2.configure(font=("", 16, ""))
        marginOne2.pack()
        #mp3 전환 페이지로 이동
        fbutton1 = tkinter.Button(window, width=15 , text="page1" , command=page1 )
        fbutton1.configure(font=("", 16, ""))
        marginTwo2.pack(side="left")
        fbutton1.pack(side="left")
        #mp3 분리 페이지로 이동
        fbutton2 = tkinter.Button(window, width=15 , text="page2", command=page2  )
        fbutton2.configure(font=("", 16, ""))
        marginTwo3.pack(side="right")
        fbutton2.pack(side="right")
        #한칸 내리기
        marginOne3=tkinter.Label(window, height=8)
        marginOne3.pack()
        #convert 리스트를 보여줌
        page1= tkinter.Button(window, width=15 , text="Open folder1 File",command=lambda: openfile(1) )
        page1.configure(font=("", 16, ""))
        page1.pack()
        #한칸 내리기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #mp3 리스트를 보여줌
        page2= tkinter.Button(window, width=15 , text="Open folder2 File",command=lambda: openfile(2) )
        page2.configure(font=("", 16, ""))
        page2.pack()
        #한칸 내리기
        marginOne5=tkinter.Label(window)
        marginOne5.pack()
        #sepearted 리스트를 보여줌
        page3= tkinter.Button(window, width=18 , text="Open folder3 File",command=lambda: openfile(3) )
        page3.configure(font=("", 16, ""))
        page3.pack()
        window.mainloop()
        
        
    def page1(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            actionbutton.pack_forget()
            showfolder1filebutton1.pack_forget()
            showfolder1filebutton2.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            main().mainpage()
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
                if num==3:
                    os.startfile('folder3')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
                if num==3:
                    os.system('nautilus folder3')
                    
        def action():
            try:
                print(3333)
                marginOne6['text']="Complete!!"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<folder List>__________\n")
        file_path = './folder1'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name2=name.split('.')
            #if name2[1]=="mp4":
            name+="\n"
            mp4list.insert(tkinter.CURRENT, name)
            
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="explain text")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        #전환 버튼
        actionbutton = tkinter.Button(window, width=15,text="action" ,command=action)
        actionbutton.configure(font=("", 16, ""))
        actionbutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showfolder1filebutton1 = tkinter.Button(window, width=15,text="Open folder1 File" ,command=lambda: openfile(1))
        showfolder1filebutton1.configure(font=("", 16, ""))
        showfolder1filebutton1.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window)
        marginOne4.pack()
        #파일열기 버튼
        showfolder1filebutton2 = tkinter.Button(window, width=15,text="Open folder2 File" ,command=lambda: openfile(2))
        showfolder1filebutton2.configure(font=("", 16, ""))
        showfolder1filebutton2.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()
        
        
    def page2(self):
        def movemainpage():
            marginTwo1.pack_forget()
            mp4list.pack_forget()
            plaintext1.pack_forget()
            actionbutton.pack_forget()
            showfolder2listbutton.pack_forget()
            showfolder3listbutton.pack_forget()
            marginOne1.pack_forget()
            marginOne2.pack_forget()
            marginOne3.pack_forget()
            marginOne4.pack_forget()
            marginOne5.pack_forget()
            marginOne6.pack_forget()
            # radio1.pack_forget()
            # radio2.pack_forget()
            # radio3.pack_forget()
            main().mainpage()
        def openfile(num):
            if os.name == 'nt':
                if num==1:
                    os.startfile('folder1')
                if num==2:
                    os.startfile('folder2')
                if num==3:
                    os.startfile('folder3')
            else:
                if num==1:
                    os.system('nautilus folder1')
                if num==2:
                    os.system('nautilus folder2')
                if num==3:
                    os.system('nautilus folder3')
        def selectNum(num):
            self.selectNum=num
        def action():
            try:
                print(3333)
                marginOne6['text']="Complete!!"
            except:
                marginOne6['text']="error"
        #메뉴바 설정
        menubar=tkinter.Menu(window)
        menu_3=tkinter.Menu(menubar, tearoff=0)
        menu_3.add_command(label="첫페이지로 돌아가기" ,command=movemainpage)
        menubar.add_cascade(label="끝내기", menu=menu_3)
        window.config(menu=menubar)
        #한칵 띄우기
        marginTwo1=tkinter.Label(window, width=2 )
        marginTwo1.pack(side="left")
        #mp4 파일 리스트 목록
        mp4list=tkinter.Text(window,width=23,height=18)
        mp4list.insert(tkinter.CURRENT, "_<Mp3 List>___________\n")
        file_path = './folder2'
        file_names = os.listdir(file_path)
        file_names
        for name in file_names:
            name+="\n"
            mp4list.insert(tkinter.CURRENT, name)
        mp4list.configure(font=("", 24, "") , state='disabled')
        mp4list.pack(side="left")
        #한칸 띄우기
        marginOne1=tkinter.Label(window, height="5" )
        marginOne1.pack()
        #설명문
        plaintext1=tkinter.Label(window , text="explain text")
        plaintext1.configure(font=("", 16, ""))
        plaintext1.pack()
        #한칸 띄우기
        marginOne2=tkinter.Label(window )
        marginOne2.pack()
        
        #한칸 띄우기
        marginOne3=tkinter.Label(window )
        marginOne3.pack()
        #분리 버튼
        actionbutton = tkinter.Button(window, width=15,text="action" ,command=action)
        actionbutton.configure(font=("", 16, ""))
        actionbutton.pack()
        #한칸 띄우기
        marginOne3=tkinter.Label(window)
        marginOne3.pack()
        #파일열기 버튼
        showfolder2listbutton = tkinter.Button(window, width=15,text="Open folder2 File" ,command=lambda: openfile(1))
        showfolder2listbutton.configure(font=("", 16, ""))
        showfolder2listbutton.pack()
        #한칸 띄우기
        marginOne4=tkinter.Label(window )
        marginOne4.pack()
        #파일열기 버튼
        showfolder3listbutton = tkinter.Button(window, width=18,text="Open folder3 File" ,command=lambda: openfile(2))
        showfolder3listbutton.configure(font=("", 16, ""))
        showfolder3listbutton.pack()
        #한칸 띄우기
        marginOne5=tkinter.Label(window ,text="")
        marginOne5.pack()
        #예외처리 결과
        marginOne6=tkinter.Label(window ,text="")
        marginOne6.configure(font=("", 16, ""))
        marginOne6.pack()







        # #mode selecter
        # RadioVariety_1=tkinter.IntVar()
        # radio1=tkinter.Radiobutton(window, text="choice1 (defalut) ", value=1, variable=RadioVariety_1 ,command=lambda: selectNum(2) )
        # radio1.configure(font=("", 16, ""))
        # radio1.pack()
        # radio2=tkinter.Radiobutton(window, text="choice2 ", value=3, variable=RadioVariety_1 ,command=lambda: selectNum(4))
        # radio2.configure(font=("", 16, ""))
        # radio2.pack()
        # radio3=tkinter.Radiobutton(window, text="choice3 ", value=9, variable=RadioVariety_1 ,command=lambda: selectNum(5))
        # radio3.configure(font=("", 16, ""))
        # radio3.pack()





if __name__=='__main__':
    main().mainpage()
