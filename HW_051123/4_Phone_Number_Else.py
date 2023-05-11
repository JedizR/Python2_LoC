def format_check(s):
    assert isinstance(s,str),"Input is not a string"
    assert s[0]=="+","Missing country code"
    assert s[0]!="+" or(s[1].isnumeric() and s[2].isnumeric),"Incorrect format country code" #guess this statement means the code is not numeric?
    assert s[0]!="+" or len(s)==13,"Incorrect number length"
    if(s[1]=="6" and s[2]=="6"): return "Thailand"
    elif(s[1]=="3" and s[2]=="4"): return "Spain"
    else: return "Other country"
#a=int(input()) #for test TypeError
a=input()
print(format_check(a))