def format_check(s):
    if(not isinstance(s,str)): raise TypeError("Input is not a string")
    if(s[0]!="+"): raise LookupError("Missing country code")
    if(s[0]=="+" and (not s[1].isnumeric() or not s[2].isnumeric)): raise ValueError("Incorrect format country code") #guess this statement means the code is not numeric?
    if(s[0]=="+" and len(s)!=13): raise ValueError("Incorrect number length")
    if(s[1]=="6" and s[2]=="6"): return "Thailand"
    elif(s[1]=="3" and s[2]=="4"): return "Spain"
    else: return "Other country"
#a=int(input()) for test TypeError
a=input()
print(format_check(a))