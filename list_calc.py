def multiply(*args):
    x=1
    for num in args:
        x *=num
    print(x)
def addition(*args):
    result=0
    for y in args:
        result +=y
    return result
def subtraction(*args):
    sum=args[0]
    for z in args[1:]:
        sum-=z
    return sum


print(subtraction())
multiply(5,3,4)
print(addition(5,3,4))