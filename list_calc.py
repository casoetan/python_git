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
multiply(5,3,4)
print(addition(5,3,4))