#! /Library/Frameworks/Python.framework/Versions/3.6/bin/python3
import math
import matplotlib.pyplot as plt
import json

with open('config.json', 'r') as f:
    tmp = f.read()
data = json.loads(tmp)
A = data['A']
OMEGA = data['OMEGA']
FI = data['FI']
OMEGA_ZERO = data['OMEGA_ZERO']
BETA = data['BETA']
T0 = data['T0']
T1 = data['T1']
Y1_0 = data['Y1_0']
Y2_0 = data['Y2_0']
N = data['N']
SHOW_TABLE = data['SHOW_TABLE']
SHOW_Y1_PLOT = data['SHOW_Y1_PLOT']
SHOW_Y2_PLOT = data['SHOW_Y2_PLOT']


def showConf(data):
    for k, v in data.items():
        print(k, "=", v)


def plot():
    vx, vy1, vy2 = rk4(fun1, fun2, T0, T1, Y1_0, Y2_0, N)
    if SHOW_TABLE:
        i = 0
        for t in vx:
            print("%4.1f %10.5f %10.5f" % (t, vy1[i], vy2[i]))
            i += 1
    if SHOW_Y1_PLOT: plt.plot(vx, vy1, 'b-')
    if SHOW_Y2_PLOT: plt.plot(vx, vy2, 'r-')
    plt.show()

def rk4(f, g, t0, t1, y10, y20, n):
    vt = [0] * (n + 1)
    vy1 = [0] * (n + 1)
    vy2 = [0] * (n + 1)
    h = (t1 - t0) / float(n)
    vt[0] = t = t0
    vy1[0] = y1 = y10
    vy2[0] = y2 = y20
    for i in range(1, n + 1):
        k1 = h * f(t, y1, y2)
        l1 = h * g(t, y1, y2)
        k2 = h * f(t + 0.5 * h, y1 + 0.5 * k1, y2 + 0.5 * l1)
        l2 = h * g(t + 0.5 * h, y1 + 0.5 * k1, y2 + 0.5 * l1)
        k3 = h * f(t + 0.5 * h, y1 + 0.5 * k2, y2 + 0.5 * l2)
        l3 = h * g(t + 0.5 * h, y1 + 0.5 * k2, y2 + 0.5 * l2)
        k4 = h * f(t + h, y1 + k3, y2 + l3)
        l4 = h * g(t + h, y1 + k3, y2 + l3)
        vt[i] = t = t0 + i * h
        vy1[i] = y1 = y1 + (k1 + k2 + k2 + k3 + k3 + k4) / 6
        vy2[i] = y2 = y2 + (l1 + l2 + l2 + l3 + l3 + l4) / 6
    return vt, vy1, vy2


def fun1(t, y1, y2):
    return y2


def fun2(t, y1, y2):
    return A*math.sin(OMEGA*t+FI) - OMEGA_ZERO*OMEGA_ZERO*y1-2*BETA*y2


print("/"*50)
print("/", "Witaj w programie!", " "*27, "/")
print("/", " "*46, "/")
print("/", "Autorzy: Jędzrzej Dobrucki, Mateusz Wasilewski", "/")
print("/", "FTIMS, Informatyka 2017/18", " "*19, "/")
print("/", "Metody numeryczne, zadanie 6 wariant \'A\'", " "*5, "/")
print("/"*50, "\n\n")


while True:
    print("\nWybierz opcje: ")
    print("1. Aktualna konfiugaracja. ")
    print("2. Rysuj wykres. ")
    print("3. Wyjście. ")
    ch = int(input("Wybór: "))
    if ch == 1:
        showConf(data)
    elif ch == 2:
        plot()
    else:
        exit(0)
