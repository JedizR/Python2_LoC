import time
def gcd(x, y):
    for d in range(10000000, 0, -1):
        if x % d == 0 and y % d == 0:
            break
    return d

t1 = time.time()
print(gcd(834544563, 834544563*4236564643675))
t2 = time.time()
print(t2-t1)