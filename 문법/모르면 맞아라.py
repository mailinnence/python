# 변수를 받을 떄 이렇게 받아야 가장 빠르다
import sys
n = int(sys.stdin.readline())
List = []
for _ in range(n):
    List.append(int(sys.stdin.readline()))


# 변수를 한번이라도 덜 쓰는게 최적화에 좋다.
List.sort()     # o
a = List.sort() # x



# from collections import Counter 
