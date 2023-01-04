a=10
b=9
try:
    if a<0 or b<0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDvisionError:
    print("please enter valid integer value")
