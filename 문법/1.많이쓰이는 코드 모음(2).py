
# 카운트 함수
# 리스트에서 최빈값을 구할 수 있는 함수

from collections import Counter
li = [1,1,1,1,1,1,2,2,2,2,3,3,3,4,5,6,6,6,6] 

# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
print(cnt_li)
print(f"최빈값 {cnt_li[0][0]} 횟수 {cnt_li[0][1]}")
print(f"최소빈값 {cnt_li[-1][0]} 횟수 {cnt_li[-1][1]}")







