import ast
from math import sqrt

with open("strdict.txt") as f:
    data = f.read()

sd = ast.literal_eval(data)

def strdict(key):
    return "0's = " + eval("f"+sd[key])

def errorlog(errorlist):
    fileWrite = open("quadraticErrorLog", "a")
    for item in errorlist:    
        fileWrite.write(f" {item}")
    fileWrite.close()

def reducefract(varNum, d01, fraction_list):
    def gcd(varNum, d01):
        while d01 != 0:
            t = d01
            d01 = varNum%d01
            varNum = t
        return varNum

    assert d01!=0, "integer division by zero"
    assert isinstance(d01, int), "must be int"
    assert isinstance(varNum, int), "must be int"
    greatest=gcd(varNum,d01)
    varNum/=greatest
    d01/=greatest
    fraction_list.append(int(varNum))
    fraction_list.append(int(d01))

def standardsolution(num1, num2, num3):
    global xCoord, yCoord
    global num01, num02, num03
    global c01, c02, d02, d03, f01, f02, sq02, j01
    global add, subtract, strVar, disc
    num01, num02, num03 = num1, num2, num3
    xCoord = float(round((-num2/(2*num1)), 2))
    yCoord = float(round(((num1*xCoord**2)+(num2*xCoord)+num3), 2))
    #print(f" vertex = x: {xCoord}, y: {yCoord}")
    disc = num2**2-4*num1*num3
    if disc < 0:
        #imaginary number
        strVar = strdict("1")
        return strVar
    
    elif sqrt(disc).is_integer() == False:
        d01 = (2*num1)
        
        #find if square root is a prime number
        flag = False
        if disc > 1:
            for nV01 in range(2, disc):
                if (disc % nV01) == 0:
                    flag = True
                    break
        if flag:
            #is not prime number
            factor_list = [nV02 for nV02 in range(2, disc) if disc % nV02 == 0]
            square_list = [nV03 for nV03 in factor_list if sqrt(nV03).is_integer() == True]

            if square_list:
                square_list.sort()
                sq01 = int(square_list[-1]**0.5)
                fraction_list = []
                for varNum in (-num2, sq01):
                    reducefract(varNum, d01, fraction_list)
                
                sq02 = int(disc/(square_list[-1]))
                c01, d02, c02, d03 = list(map(int, fraction_list))
                
                #check if reduced numbers are integers
                if d02 == d03:
                    #both denominators are the same
                    if d02 == 1 or d02 == -1:
                        #denominator is 1
                        if c02 == 1 or c02 == -1:
                            #if number next to square root is 1 or -1 and denominator is 1 or -1, don't print it
                            strVar = strdict("2")
                            return strVar
                        else:
                            #if denominator is 1 or -1, don't print it
                            strVar = strdict("3")
                            return strVar
                    else:
                        #if denominator is not 1 or -1, print it
                        strVar = strdict("4")
                        return strVar
                else:
                    #different denominators
                    if c01 == d02 or c01 == -d02:
                        if c02 == 1 or c02 == -1:                    
                            strVar = strdict("5")
                            return strVar
                        else:
                            strVar = strdict("6")
                            return strVar
                    else:
                        if c02 == 1 or c02 == -1:
                            strVar = strdict("7")
                            return strVar
                        else:
                            strVar = strdict("8")
                            return strVar

            if not square_list:
                null_01 = 0
                while null_01 < disc:
                    factor_tree = []
                    for nV04 in range(2, disc):
                        if disc % nV04 == 0:    
                            disc /= nV04
                            factor_tree.append(nV04)
                            null_01 = 0
                        else:
                            null_01 += 1
                fraction_list = []
                reducefract(-num2, d01, fraction_list)
                join_tree = ", ".join(map(str, factor_tree))
                f01 , f02, j01 = fraction_list[0], fraction_list[1], join_tree
                strVar = strdict("9")
                return strVar

        else:
            #is prime number
            strVar = strdict("10")
            return strVar

    elif sqrt(disc).is_integer() == True:
        #perfect square
        add = (-num2 + (disc)**0.5)/(2*num1)
        subtract = (-num2 - (disc)**0.5)/(2*num1)
        strVar = strdict("11")
        return strVar

    else:
        print("undefined")
        error_list = [num1, num2, num3, "\n"]
        errorlog(error_list)

def selection():
    while True:
        print("Commands:")
        print("Standard (1), Vertex (2), 0's (3), Exit (4):")
        select = input("1, 2, 3, or 4?: ")
        if select == "1":
            num1, num2, num3 = list(map(int, input("a, b, c for ax^2+bx+c: ").split(", ")))
            standard(num1, num2, num3)
        elif select == "2":
            num1, num2, num3 = list(map(int, input("a, h, k for a(x-h)^2+k: ").split(", ")))
            vertex(num1, num2, num3)
        elif select == "3":
            #add inputs for numbers before x variables. Example: (x-5)(5x+2)
            num1, mvar, num2, nvar, num3 = list(map(int, input("a, m, b, n, c for a(mx+b)(nx+c): ").split(", ")))
            zeros(num1, mvar, num2, nvar, num3)
        elif select == "4" or select == "exit" or select == "Exit":
            print("exiting...")
            break
        else:
            print("not a valid input")

def standard(num1, num2, num3):
    #print the correct signs with the corresponding variables
    print(f"{num1}x^2+{num2}x+{num3}")
    print(standardsolution(num1, num2, num3))

def vertex(num1, num2, num3):
    print(f"{num1}(x-{num2})^2+{num3}\n vertex = x: {num2}, y: {num3}")
    #print("not finished yet")
    coef1 = (num2+num2)*num1
    coef2 = ((num2*num2)*num1)+num3
    print(standardsolution(num1, coef1, coef2))
    
def zeros(num1, mvar, num2, nvar, num3):
    binom1 = num1*(nvar*mvar)
    binom2 = num1*((nvar*num2)+(num3*mvar))
    binom3 = num1*(num3*num2)
    print(standardsolution(binom1, binom2, binom3))


# selection()

#for t1 in range(1, 10):
#    for t2 in range(1, 10):
#        for t3 in range(1, 10):
#            standardsolution(t1, t2, t3)

#error_list = [num1, num2, num3, factor_list, square_list, fraction_list]
#errorlog(error_list)