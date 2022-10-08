
# 구글 드라이브 마운트 하고
from google.colab import drive
drive.mount('/content/drive')
import pandas as pd

#파일 부르는 법
df= pd.read_csv('/content/drive/MyDrive/과일가게.csv')

print(type(df),'\n')
print(df,'\n')
print(df.head(10)  ,'\n')  	# n행 까지 출력
print(df.tail(10)  ,'\n')  	#  tail : 뒤에서부터 n행까지 출력
			

#데이터를 읽으면서 칼럼명을 추가하고 싶을 때
df = pd.read_csv('/content/name.csv', index_col = 0, names = ['품목', '크기', '금액', '수수료'])
print(df.head(10)  ,'\n')  	


# 원하는 칼럼만 쓰고 싶을 때
df = pd.read_csv('/content/과일가게.csv', usecols = ['품목', '크기'])
print(df.head(10)  ,'\n')  	# n행 까지 출력

