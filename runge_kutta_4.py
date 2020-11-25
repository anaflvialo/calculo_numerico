

def f(x,y):
    return -x*y

def runge_kutta_4(x0,y0,m,h):
    print("x(i) | y(i) | k1 | k2 | k3 | k4")
    print(x0, "|", y0 ,"| - | - | - | - |")
    xj = x0
    yj = y0
    k1 = 0
    k2 = 0
    k3 = 0
    k4 = 0

    for j in range(int(m)):
        k1 = f(xj,yj)
        k2 = f((xj+h/2),(yj+h/2*k1))
        k3 = f((xj+h/2),(yj+(h/2)*k2))
        k4 = f((xj+h),(yj+h*k3))

        yj = yj + (h/6)*(k1+2*k2+2*k3+k4)
        xj = xj + h
        print(xj," | ", yj, " | ", k1, " | ", k2, " | ", k3, " | ", k4)


x0 = 0
y0 = 1
a = 0
b = 1
h = 0.2
m = (b-a)/h
runge_kutta_4(x0,y0,m,h)