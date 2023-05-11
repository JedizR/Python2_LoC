def enum(lst):
    return [(i+1, elem) for i, elem in enumerate(lst)]
lst=eval(input())
print(enum(lst))