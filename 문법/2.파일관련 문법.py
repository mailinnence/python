

#파이썬 파일업로드

#읽을떄
f=open("C:\\Users\\maili\\OneDrive\\바탕 화면\program\\이어서 공부할 코딩\\python\\thinker 공부.txt","rt",encoding="utf-8")
#역슬래쉬 두번
c=f.read()
f.close() 
#썼으면 잘 닫아주고
print(c)

#쓰기
f=open("C:\\Users\\maili\\OneDrive\\바탕 화면\program\\이어서 공부할 코딩\\python\\thinker 공부.txt","wt",encoding="utf-8")
c='쓰고자 하는 내용'
f.write(c)
f.close() 
#썼으면 잘 닫아주고




#바이너리 파일 읽기
with open("", "rb") as f:
    a=f.read()
    f.close()

    
#바이너리 파일 쓰기
with open("", "wb") as f:
    f.write(a)
    f.close()


# 바이너리와 암호화
# 암호화 >> 바이너리 파일로 쓰기 >> 바이너리 파일 읽기 
# 문자열로 넣으려고 하면 안된다!!!!
#바이너리 파일 읽기

# 동영상 바이너리 파일 전환 
with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\aa.mp3", "rb") as f:
    a=f.read()
    f.close()
    #print(a)


with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\aa.bin", "wb") as f:
    f.write(a)
    f.close()
    
with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\aa.bin", "rb") as f:
    a=f.read()
    f.close()    
    

with open("C:\\Users\\maili\\OneDrive\\바탕 화면\\a1.mp3", "wb") as f:
    f.write(a)
    f.close()    







# 파일 확장자와 이름 바꾸기

file_path = 'D:\\NVIDIA_RTX3000_series\\workspace\\data_src_112\\'
file_names = os.listdir(file_path)
file_names    
    
i = 1
for name in file_names:
    src = os.path.join(file_path, name)
    dst = 'b'+str(i) + '.png'
    dst = os.path.join(file_path, dst)
    os.rename(src, dst)
    i += 1
    
    
    
# 특정 확장자 찾기
for i in range(len(a)):
    if os.path.splitext(os.getcwd()+a[i])[1]==".mp4":
        Text1.insert(1.0,a[i]+"\n")
    

    
    
    
#파일 다루기
data=f.readline() # txt 파일의 첫번째 줄만 가져옵니다.
data= f.readlines() # 각 줄의 문자 데이터를 하나의 문자 데이터로 인식하여 가져옵니다.
line = line.strip() # 4) 양 옆의 공백을 제거합니다. 













    
