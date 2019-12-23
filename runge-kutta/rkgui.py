from tkinter import *
import tkinter.scrolledtext as tkst
import matplotlib.pyplot as plt
import numpy as np
from math import *

import rungeKutta as rk

'''
AUTHOR - FOLARANMI AKINOLA DAVIDSON
'''



def GUI():
    def evaluateparameters():
        x, y = eval(xy.get())
        h = eval(increment.get())
        n = eval(iterations.get())
        return x, y, h, n

    def intro(scheme):
        txt = 'The following results were obtained using the '+ scheme +' scheme' + '\n' +'=============================================================='
        return txt


    def loadData():
        output = open("rkgui.txt","r")
        texts = output.read()
        outputspace.insert("1.0",texts)

    def writetextfiles(vals, scheme):
        outfile = open('rkgui.txt', 'w')
        outfile2 = open('rkgui2.txt', 'w')
        t = intro(scheme)

        outfile.write(t)
        outfile.write('\n')
        for values in vals:
            outfile.write(str(round((values[0]), 6)))
            outfile.write(',')            
            outfile.write(str(round((values[1]), 10)))
            outfile.write('\n')
            outfile.write('***********************************************************')
            outfile.write('\n')
        outfile.close()

        valx = [values[0] for values in vals]
        valy = [values[1] for values in vals]

        outfile2.write(str(valx))
        outfile2.write('\n')
        outfile2.write(str(valy))
        outfile2.close()

    def order2a():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK2A(x, y, step, iters, f)

        writetextfiles(vals, 'RK2A')

        
        loadData()

    def order2b():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK2B(x, y, step, iters, f)

        writetextfiles(vals,'RK2B')
        
        loadData()


    def order2c():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK2C(x, y, step, iters, f)

        writetextfiles(vals,'RK2C')
        
        loadData()

    def order3():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK3(x, y, step, iters, f)

        writetextfiles(vals,'RK3')
        
        loadData()
        
    def order4():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK4(x, y, step, iters, f)

        writetextfiles(vals,'RK4')
        
        loadData()

    def order5():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RK5(x, y, step, iters, f)

        writetextfiles(vals,'RK5')
        
        loadData()
        
    def orderf45():
        
        x, y, step, iters = evaluateparameters()

        f = E5.get()

        vals = rk.RKF45(x, y, step, iters, f)

        writetextfiles(vals,'RKF45')
        
        loadData()
        
    def plot():
        vals = np.genfromtxt('rkgui2.txt', delimiter=',')
        X,Y = vals[0],vals[1]
        plt.plot(X, Y, label = 'Numerical Solution')

        try:
            exacty = [eval(E6.get()) for x in X]
            plt.plot(X, exacty, label = 'Exact Solution')
        except:
            pass
        
        plt.grid()
        plt.legend()
        plt.xlabel('x')
        plt.ylabel('y')

    def show():
        plt.show()


    
    master = Tk()

    xy = StringVar()
    increment = StringVar()
    iterations = StringVar()
    fprimex = StringVar()
    fx = StringVar()

    frame1 = Frame(master, height = 2, bd = 1, relief = SUNKEN)
    frame1.pack(fill = X, expand = True)


        
        
        

    L1 = Label(frame1, text = "initial point", width = 8)
    L1.pack(fill = X, side = LEFT)

    E1 = Entry(frame1, bd = 5, textvariable = xy )
    E1.pack(fill = X, side = LEFT, expand = True)

    L3 = Label(frame1, text = "step size", width = 8)
    L3.pack(fill = X, side = LEFT)

    E3 = Entry(frame1, bd = 5, textvariable = increment)
    E3.pack(fill = X, side = LEFT, expand = True)

    L4 = Label(frame1, text = "number of iterations", width = 21)
    L4.pack(fill = X, side = LEFT)

    E4 = Entry(frame1, bd = 5, textvariable = iterations)
    E4.pack(fill = X, side = LEFT, expand = True)


    frame2 = Frame(master, height = 2, bd = 1, relief = SUNKEN)
    frame2.pack(fill = X, expand = True)

    L5 = Label(frame2, text = "f'(x) = ", width = 8)
    L5.pack(fill = X, side = LEFT)

    E5 = Entry(frame2, bd = 5, textvariable = fprimex)
    E5.pack(fill = X, side = LEFT, expand = True)


    frame3 = Frame(master, height = 2, bd = 1, relief = SUNKEN)
    frame3.pack(fill = X,  expand = True)

    L6 = Label(frame3, text = "f(x) = ", width = 8)
    L6.pack(fill = X, side = LEFT)

    E6 = Entry(frame3, bd = 5, textvariable = fx)
    E6.pack(fill = X, side = LEFT, expand = True)


    frame4 = Frame(master, height = 2, bd = 1, relief = SUNKEN)
    frame4.pack(fill = X, expand = True)

    frame5 = Frame(frame4, height = 2, bd = 1, relief = SUNKEN)
    frame5.pack(fill = X, side = LEFT, expand = True)

    B1 = Button(frame5, text = "RK2A", bg = 'blue', fg = 'white', height = 3, command = order2a)
    B1.pack(fill = BOTH,side = TOP, expand = True)

    B2 = Button(frame5, text = "RK2B", bg = 'blue', fg = 'white', height = 3, command = order2b)
    B2.pack(fill = BOTH,side = TOP, expand = True)

    B3 = Button(frame5, text = "RK2C", bg = 'blue', fg = 'white', height = 3, command = order2c)
    B3.pack(fill = BOTH,side = TOP, expand = True)

    B4 = Button(frame5, text = "RK3", bg = 'blue', fg = 'white', height = 3, command = order3)
    B4.pack(fill = BOTH,side = TOP, expand = True)

    B5 = Button(frame5, text = "RK4", bg = 'blue', fg = 'white', height = 3, command = order4)
    B5.pack(fill = BOTH,side = TOP, expand = True)

    B6 = Button(frame5, text = "RK5",bg = 'blue', fg = 'white', height = 3, command = order5)
    B6.pack(fill = BOTH,side = TOP, expand = True)

    B7 = Button(frame5, text = "RKF45", bg = 'blue', fg = 'white', height = 3, command = orderf45)
    B7.pack(fill = BOTH,side = TOP, expand = True)

    B8 = Button(frame5, text = "plot", bg = 'white', fg = 'blue', height = 3, command = plot)
    B8.pack(fill = BOTH,side = TOP, expand = True)

    B9 = Button(frame5, text = "show plot", bg = 'white', fg = 'blue',  height = 3, command = show)
    B9.pack(fill = BOTH,side = TOP, expand = True)

    frame6 = Frame(frame4, height = 2, bd = 1, relief = SUNKEN)
    frame6.pack(fill = X, side = RIGHT, expand = True)

    outputspace = tkst.ScrolledText(frame6, wrap = 'word', width = 70, height = 31, bg = 'white')
    outputspace.pack(fill = 'both', expand = True)



    master.mainloop()

if __name__=='__main__':
    GUI()
