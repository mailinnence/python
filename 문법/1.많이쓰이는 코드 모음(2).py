# 카운트 함수
# 리스트에서 최빈값을 구할 수 있는 함수
from collections import Counter
li = [1,1,1,1,1,1,2,2,2,2,3,3,3,4,5,6,6,6,6] 






# 최빈값 - 빈출
cnt_li = Counter(li).most_common()
print(cnt_li)
print(f"최빈값 {cnt_li[0][0]} 횟수 {cnt_li[0][1]}")
print(f"최소빈값 {cnt_li[-1][0]} 횟수 {cnt_li[-1][1]}")






# 리스트 길이 순으로 정렬... 파이썬은 참...하다
lst.sort()
lst.sort(key = len)







# 리스트에 튜플 넣기

'''
3
21 Junkyu
21 Dohyun
20 Sunyoung
'''

n = int(input())

ls = []
for _ in range(n):
    age, name = map(str, input().split())
    age = int(age)
    ls.append((age, name))

print(ls)

'''
[(21, 'Junkyu'), (21, 'Dohyun'), (20, 'Sunyoung')]
'''









# 정렬 기준
'''
sorted 함수는 파이썬 내장 함수 중 하나로, 정렬된 새로운 리스트를 반환합니다. 
sorted 함수의 첫 번째 인자로 정렬할 리스트를 전달하고, key 인자를 사용하여 정렬 기준을 설정할 수 있습니다.
'''
sorted_list = sorted(리스트,key=lambda x: a)






