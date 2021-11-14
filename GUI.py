import sys
import tkinter as tk
import QuadraticCalc as qc

sys.path.append(".")

root = tk.Tk()

def clear():
    buttons = root.grid_slaves()
    for cycle in buttons:
        cycle.destroy()

def exe1():
    aV = e01.get()
    bV = e02.get()
    cV = e03.get()
    aV, bV, cV = int(aV), int(bV), int(cV)
    qc.standardsolution(aV, bV, cV)
    xCoord = qc.xCoord
    yCoord = qc.xCoord
    strVar = qc.strVar
    ans1 = tk.Label(root, text=f"answer: x-intercept {xCoord}, y-intercept {yCoord}").grid(row=5, column=1)
    ans2 = tk.Label(root, text=f"{strVar}").grid(row=6, column=1)

def exe2():
    aV = e11.get()
    bV = e12.get()
    cV = e13.get()
    aV, bV, cV = int(aV), int(bV), int(cV)
    qc.vertex(aV, bV, cV)
    xCoord = qc.xCoord
    yCoord = qc.xCoord
    strVar = qc.strVar
    ans1 = tk.Label(root, text=f"answer: x-intercept {xCoord}, y-intercept {yCoord}").grid(row=5, column=1)
    ans2 = tk.Label(root, text=f"{strVar}").grid(row=6, column=1)

def exe3():
    aV = e21.get()
    mV = e22.get()
    bV = e23.get()
    nV = e24.get()
    cV = e25.get()
    aV, mV, bV, nV, cV = int(aV), int(mV), int(bV), int(nV), int(cV)
    qc.zeros(aV, mV, bV, nV, cV)
    xCoord = qc.xCoord
    yCoord = qc.xCoord
    strVar = qc.strVar
    ans1 = tk.Label(root, text=f"answer: x-intercept {xCoord}, y-intercept {yCoord}").grid(row=7, column=1)
    ans2 = tk.Label(root, text=f"{strVar}").grid(row=8, column=1)

def opt1():
    tk.Label(root, text="ax^2 + bx + c").grid(row=0, column=1)
    
    global e01, e02, e03
    
    e01 = tk.Entry(root)
    e02 = tk.Entry(root)
    e03 = tk.Entry(root)

    e01.grid(row=1, column=1)
    e02.grid(row=2, column=1)
    e03.grid(row=3, column=1)

    tk.Label(root, text="a: ").grid(row=1, column=0)
    tk.Label(root, text="b: ").grid(row=2, column=0)
    tk.Label(root, text="c: ").grid(row=3, column=0)

    tk.Button(root, text="Quit", command=quit).grid(row=4, column=0)
    tk.Button(root, text="Calculate", command=exe1).grid(row=4, column=1)

def opt2():
    tk.Label(root, text="a(x-h)^2 + k").grid(row=0, column=1)
    
    global e11, e12, e13
    
    e11 = tk.Entry(root)
    e12 = tk.Entry(root)
    e13 = tk.Entry(root)

    e11.grid(row=1, column=1)
    e12.grid(row=2, column=1)
    e13.grid(row=3, column=1)

    tk.Label(root, text="a: ").grid(row=1, column=0)
    tk.Label(root, text="h: ").grid(row=2, column=0)
    tk.Label(root, text="k: ").grid(row=3, column=0)

    tk.Button(root, text="Quit", command=quit).grid(row=4, column=0)
    tk.Button(root, text="Calculate", command=exe2).grid(row=4, column=1)

def opt3():
    tk.Label(root, text="a(mx+b)(nx+c)").grid(row=0, column=1)
    
    global e21, e22, e23, e24, e25

    e21 = tk.Entry(root)
    e22 = tk.Entry(root)
    e23 = tk.Entry(root)
    e24 = tk.Entry(root)
    e25 = tk.Entry(root)

    e21.grid(row=1, column=1)
    e22.grid(row=2, column=1)
    e23.grid(row=3, column=1)
    e24.grid(row=4, column=1)
    e25.grid(row=5, column=1)

    tk.Label(root, text="a: ").grid(row=1, column=0)
    tk.Label(root, text="m: ").grid(row=2, column=0)
    tk.Label(root, text="b: ").grid(row=3, column=0)
    tk.Label(root, text="n: ").grid(row=4, column=0)
    tk.Label(root, text="c: ").grid(row=5, column=0)

    tk.Button(root, text="Quit", command=quit).grid(row=6, column=0)
    tk.Button(root, text="Calculate", command=exe3).grid(row=6, column=1)

def selector():
    button1 = tk.Button(root, text="Standard", command=lambda:[clear(), opt1()])
    button1.grid(row=1, column=1)
    button2 = tk.Button(root, text="Vertex", command=lambda:[clear(), opt2()])
    button2.grid(row=2, column=1)
    button3 = tk.Button(root, text="0's", command=lambda:[clear(), opt3()])
    button3.grid(row=3, column=1)
    button4 = tk.Button(root, text="Quit", command=quit)
    button4.grid(row=4, column=1)

selector()

root.mainloop()
 