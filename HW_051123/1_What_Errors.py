def do_something(x):
    answer = 0
    array = [x, x ** 0, x // x , x % (x - 4), [x]]
    for i in range(x):
        answer += array[i]
    return answer
x = int(input())
try:
    do_something(x)
except ZeroDivisionError:
    print("Sorry mate you're (force to) devided a number by 0") #occur with 1,2,3,4
except ValueError:
    print("Input can't be 4 because you couldn't defined the value of mod 0") #never occurs!
except TypeError:
    print("Input can't be greater than 3 otherwise you will (force to) combine int with list or the index of array will be out of range") #occur with 5,6,7,...