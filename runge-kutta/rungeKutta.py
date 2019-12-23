'''AUTHOR- FOLARANMI AKINOLA DAVIDSON
23/12/2019
======================================'''

'''This module utilises the runge kutta algorithm for
solving differential equations. It includes the second
order and fourth order runge kutta scheme.

The arguments required to make use of this module are the
initial values of the function of interest, [x1,x2]; the step,
h; the number of iterations, n; the differential function, f.

Exceptions have been added to the functions for each scheme. This
modification makes the module suitable for evaluating differential functions
typed into tkinter GUI entry boxes.

'''

from math import *

def rkguif(f, x, y):
    return eval(f)

def RK2A(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2

    for i in range(1, n + 1):
        subList = []
        try: 
            k1 = f(x,y)
            k2 = f(x + h, y + (h * k1))
        except:
            k1 = rkguif(f, x, y)
            k2 = rkguif(f, x + h, y + (h * k1))
    
        y = y + ((h / 2) * (k1 + k2))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RK2B(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2

    for i in range(1, n + 1):
        subList = []
        try:
            k1 = f(x,y)
            k2 = f(x + (0.5 * h), y + (0.5 * h * k1))
        except:
            k1 = rkguif(f,x,y)
            k2 = rkguif(f,x + (0.5 * h), y + (0.5 * h * k1))

        y = y + (h * k2)
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RK2C(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2

    for i in range(1, n + 1):
        subList = []
        try:
            k1 = f(x,y)
            k2 = f(x + ((3 / 4) * h), y + ((3 / 4) * h * k1))
        except:
            k1 = rkguif(f,x,y)
            k2 = rkguif(f, x + ((3 / 4) * h), y + ((3 / 4) * h * k1))

        y = y + ((h / 3) * (k1 + (2 * k2)))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RK3(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2
    for i in range(1, n + 1):
        subList = []
        try:
            k1 = f(x,y)
            k2 = f(x + (h / 2), y + ((h * k1) / 2))
            k3 = f(x + h, y - (h * k1) + (2 * h * k2))
        except:
            k1 = rkguif(f,x,y)
            k2 = rkguif(f, x + (h / 2), y + ((h * k1) / 2))
            k3 = rkguif(f, x + h, y - (h * k1) + (2 * h * k2))

        y = y + ((h / 6) * (k1 + (4 * k2) + k3))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RK4(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2
    for i in range(1, n + 1):
        subList = []
        try:
            k1 = h * f(x, y)
            k2 = h * f(x + (0.5 * h), y + (0.5 * k1))
            k3 = h * f(x + (0.5 * h), y + (0.5 * k2))
            k4 = h * f(x + h, y + k3)
        except:
            k1 = h * rkguif(f,x, y)
            k2 = h * rkguif(f, x + (0.5 * h), y + (0.5 * k1))
            k3 = h * rkguif(f, x + (0.5 * h), y + (0.5 * k2))
            k4 = h * rkguif(f, x + h, y + k3)

        y = y + ((1.0/6.0) * (k1 + (2 * k2) + (2 * k3) + k4))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RK5(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2
    for i in range(1, n + 1):
        subList = []
        try:
            k1 = f(x, y)
            k2 = f(x + (h / 4), y + (h * k1 / 4))
            k3 = f(x + (h / 4), y + (h * k1 / 8) + (h * k2 / 8))
            k4 = f(x + (h / 2), y - (h * k2 / 2) + (h * k3))
            k5 = f(x + (3 * h / 4), y + (3 * h * k1 /16) + (9 * h * k4 / 16))
            k6 = f(x + h, y - (3 * h * k1 / 7) + (2 * h * k2 / 7) + (12 * h * k3 / 7) - (12 * h * k4 / 7) + (8 * h * k5 / 7))
        except:
            k1 = rkguif(f, x, y)
            k2 = rkguif(f, x + (h / 4), y + (h * k1 / 4))
            k3 = rkguif(f, x + (h / 4), y + (h * k1 / 8) + (h * k2 / 8))
            k4 = rkguif(f, x + (h / 2), y - (h * k2 / 2) + (h * k3))
            k5 = rkguif(f, x + (3 * h / 4), y + (3 * h * k1 /16) + (9 * h * k4 / 16))
            k6 = rkguif(f, x + h, y - (3 * h * k1 / 7) + (2 * h * k2 / 7) + (12 * h * k3 / 7) - (12 * h * k4 / 7) + (8 * h * k5 / 7))

        y = y + ((h / 90) * ((7 * k1) + (32 * k3) + (12 * k4) + (32 * k5) + (7 * k6)))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values

def RKF45(x1, x2, h, n, f):
    values = [[x1,x2]]
    x = x1
    y = x2
    for i in range(1, n + 1):
        subList = []
        try:
            k1 = f(x, y)
            k2 = f(x + (h / 5), y + (h * k1 / 5))
            k3 = f(x + (3 * h / 10), y + (3 * h * k1 / 40) + (9 * h * k2 / 40))
            k4 = f(x + (3 * h / 5), y + (3 * h * k1 / 10) - (9 * h * k2 / 10) + (6 * h * k3 / 5))
            k5 = f(x + h, y - (11 * h * k1 /54) + (5 * h * k2 / 2) - (70 * h * k3 / 27) + (35 * h * k4 / 27))
            k6 = f(x + (7 * h / 8), y + (1631 * h * k1 / 55296) + (175 * h * k2 / 512) + (575 * h * k3 / 13824) - (44275 * h * k4 / 110592) + (253 * h * k5 / 4096))
        except:
            k1 = rkguif(f,x,y)
            k2 = rkguif(f, x + (h / 5), y + (h * k1 / 5))
            k3 = rkguif(f, x + (3 * h / 10), y + (3 * h * k1 / 40) + (9 * h * k2 / 40))
            k4 = rkguif(f, x + (3 * h / 5), y + (3 * h * k1 / 10) - (9 * h * k2 / 10) + (6 * h * k3 / 5))
            k5 = rkguif(f, x + h, y - (11 * h * k1 /54) + (5 * h * k2 / 2) - (70 * h * k3 / 27) + (35 * h * k4 / 27))
            k6 = rkguif(f, x + (7 * h / 8), y + (1631 * h * k1 / 55296) + (175 * h * k2 / 512) + (575 * h * k3 / 13824) - (44275 * h * k4 / 110592) + (253 * h * k5 / 4096))

        y = y + (h * ((37 * k1 / 378) + (250 * k3 / 621) + (125 * k4 / 594) + (512 * k6 / 1771)))
        x = x + h

        subList.append(x)
        subList.append(y)

        values.append(subList)
    return values


        

        


