def f(x):
    return -x**2+3*x-2
x=1
while x <=2.04:
    print(f(x))
    print("when", round(x,4), "=>", round(f(x),4))
    x += 0.05

first = f(1)
last = f(2)
print(first,last)
x = 1.05
total = 0
while x < 2:
    total +=f(x)
    x += 0.05
print(total)
def t():
    return (0.05/2)*(first+2*total+last)
print(t())
def error():
    return (((1/6)-t())*100)/(1/6)
print(error())
a = int(input("real a"))
b = int(input("real b"))
n = int(input("real n"))
h = (b-a)/n
