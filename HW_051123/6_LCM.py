# import time as t
# def gcd(a,b):
#     if(a%b==0): return b
#     else: return gcd(b,a%b)
# def lcm(a,b): return int(a*b/gcd(a,b))
# lst=list(map(int,input().split()))
# a=lst[0]
# b=lst[1]
# t1=t.time()
# print(lcm(a,b))
# t2=t.time()
# print(f"time : {t1-t2}")
# #=========================================Euclidean Method=====================================
import time
def gcd(x, y):
    for i in range(max(x,y),0,-1):
        if(x>y):
            x-=y
            i=x
        elif(x<y):
            y-=x
            i=y
        else: break
    return x
def lcm(x,y): return x*y//gcd(x,y)
t1=time.time()
print(lcm(137690, 298))
t2=time.time()
print(f"time : {t2-t1}")