
import matplotlib.pyplot as plt
import math
import time


class TimeComplexity():
    def List(self):
        global x ,y
        x = []
        y = []
        
    def show(self):
        plt.figure()
        plt.plot(x, y)
        plt.show()
        
    def Graph(self,  n , method):
        TimeComplexity().List()
        for i in range(0, n, 10000):        # 0, 10, 2
            start = time.time()
            method(i+1)
            end = time.time()
            y.append(end - start)
            x.append(i+1)
            
    def run(self , n ,method):
        TimeComplexity().Graph(n ,method)         
        TimeComplexity().show()
        
    def factorial(self, n):
        if n<=1:
            return 1
        else:
            return (n * TimeComplexity().factorial(n-1))
        
    def factorial_iter(self, n):
        result =1
        for i in range(n):
            i +=1
            result = result * i
        return result 



# 오류 난다 >> 순환의 단점 메모리 부족
# TimeComplexity().run(10000 ,TimeComplexity().factorial )

# 반복
TimeComplexity().run(100000 ,TimeComplexity().factorial_iter )
