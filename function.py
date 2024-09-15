def findSquare(num):
    return num*num

def myfun(n):
    return lambda a: a**n

print(findSquare(int(input("num : "))))

x = lambda a, b : a**b
print(x(6, 7))

a = myfun(int(input("enter power : ")))
print(a(int(input("base : "))))