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
t1=time.time()
print(gcd(137690, 298))
t2=time.time()
print(f"time : {t2-t1}")