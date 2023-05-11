def gcd(a,b):
    if(a%b==0): return b
    else: return gcd(b,a%b)
def lcm(a,b): return int(a*b/gcd(a,b))
lst=list(map(int,input().split()))
a=lst[0]
b=lst[1]
print(f"gcd is {gcd(a,b)}, lcm is {lcm(a,b)}")