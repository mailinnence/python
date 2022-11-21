# 실습.1


def my_len(x):
    length = 0
    for i in x:
        length +=1
    return length


a = [5,5,6,7,8,3]
b = 'Life is short.'
print(len(a), len(b)) # 내장 함수 len()
print(my_len(a), my_len(b)) # my_len()


c=[1,23,4,5,6,6]
print(c.__len__())




# 실습.2
def mult(a, b):
    ans = 1
    for i in range(a,b+1):
        ans *=i
    return ans


def mult1(a, b):
    ans = 1
    while a <= b:
        ans*=a
        a+=1
    return ans


        
print(mult(1, 3))
print(mult1(2, 5))




# 실습.3
def sum_pos_neg(l):
    possum = 0
    negsum = 0
    for i in range(len(l)):
        if l[i] > 0:
            possum += l[i]
        else:
            negsum += l[i]
    return possum,negsum


possum,negsum = sum_pos_neg([3,4,-6,-3])
print(possum,negsum) # 7 -9
mylist=[0,0,0,0,0,0,0,0,0,1,-1]
possum2,negsum2 = sum_pos_neg(mylist)
print(possum2,negsum2) # 1 -1




def count_even(*n):
    cnt = 0
    for v in n:
        if v % 2 == 0:
            cnt += 1f mult1(a, b):
    ans = 1
    while b < 10:
        print(a)
    return cnt


count_even(1,2,3,4,5)








# 실습.4
import numpy as np




def vector_sum(vector, *vectors):
    u = np.array(vector , dtype=float)
    w = np.array(vectors, dtype=float)
    for i in vectors:
        w = np.array(i)
        u+=w
    return u
            
    
    
    
v1=[0, 1]
v2=[0.5, 0.5]
v3=[1, 0]
v4=[6, 4]
v5=[3.14, 2.72]
m1 = vector_sum(v1, v2, v3)
m2 = vector_sum(v1, v2, v3, v4)
m3 = vector_sum(v3, v5)
print(m1 , m2 , m3)    




# 실습.5
def merge_list(a=[0], b=[0]):
    c = a+b
    c.sort()
    return c

    
    
l = [3, 5, 9, 1, 2]
ml1 = merge_list(l,[2,1])
ml2 = merge_list([6,9,4])
ml3 = merge_list()
print(ml1)
print(ml2)
print(ml3)
    



# 실습.6
import random
print("** 로또 번호 자동 기입을 시작합니다 **")
for i in range(5):
    a= random.sample(range(45), 6)
    print(str(i+1) +"번째 자동 기입 ==>" ,end="")
    print(a)







# 실습.7
def get_min_max(l):
    l.remove(min(l))
    l.remove(max(l))
    min_val = min(l)
    max_val = max(l)
    return min_val,max_val
    
    
l = [3, 5, 9, 1, 2]
min_val, max_val = get_min_max(l)
print(min_val)
print(max_val)
print(l)







# 실습.8
from collections import Counter


def comb_dict(d1, d2):
    result = dict(Counter(d1)+Counter(d2))
    dic = dict(sorted(result.items()))
    return dic
    

comb_dict(d1, d2)












# 9.실습
def diff(*n):
    n=list(n)
    if len(n) > 1:
        return max(n) - min(n)
    else:
        print("error")
    
print(diff(1,2,3,4,5))
print(diff(-100, 200))
diff(1) # 오류발생!













