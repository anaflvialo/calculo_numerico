

def f(x,y):
    return -x*y

def runge_kutta_2(x0,y0,m,h):
    print("x(i) | y(i) | k1 | k2")
    print(x0, "|", y0 ,"| - | - |")
    xj = x0
    yj = y0
    k1 = 0
    k2 = 0

    for j in range(int(m)):
        k1 = f(xj,yj)
        k2 = f((xj+h),(yj+h*k2))
        yj = yj + (h/2)*(k1+k2)
        xj = xj + h
        print(xj," | ", yj, " | ", k1, " | ", k2)


x0 = 0
y0 = 1
a = 0
b = 1
h = 0.2
m = (b-a)/h
runge_kutta_2(x0,y0,m,h)