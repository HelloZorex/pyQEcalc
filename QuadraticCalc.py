from math import sqrt

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
    x = float(-num2/(2*num1))
    y = float((num1*x**2)+(num2*x)+num3)
    print(f" vertex = x: {x}, y: {y}")
    discriminant = num2**2-4*num1*num3
    if discriminant < 0:
        #imaginary number
        print(f" 0's = ({-num2} +- sqrt ({discriminant})) / {2*num1}")
    
    elif sqrt(discriminant).is_integer() == False:
        d01 = (2*num1)
        n01 = num2
        
        #find if square root is a prime number
        flag = False
        if discriminant > 1:
            for i in range(2, discriminant):
                if (discriminant % i) == 0:
                    flag = True
                    break
        if flag:
            #is not prime number
            #factor out squares from the square root
            num = discriminant
            factor_list = []
            for n in range(2, num):
                if num % n == 0:
                    factor_list.append(n)

            #check for any squares in the list
            square_list = []
            for n2 in factor_list:
                if sqrt(n2).is_integer() == True:
                    square_list.append(n2)

            if square_list:
                square_list.sort()
                sq01 = int(square_list[-1]**0.5)
                fraction_list = []
                for varNum in (-n01, sq01):
                    reducefract(varNum, d01, fraction_list)
                
                sq02 = int(discriminant/(square_list[-1]))
                c01 = int(fraction_list[0])
                d02 = int(fraction_list[1])
                c02 = int(fraction_list[2])
                d03 = int(fraction_list[3])
                
                #check if reduced numbers are integers
                if d02 == d03:
                    #both denominators are the same
                    if d02 == 1 or d02 == -1:
                        #denominator is 1
                        if c02 == 1 or c02 == -1:
                            #if number next to square root is 1 or -1 and denominator is 1 or -1, don't print it
                            print(f" 0's = {c01} + sqrt({sq02}) and {c01} - sqrt({sq02})")
                        else:
                            #if denominator is 1 or -1, don't print it
                            print(f" 0's = {c01} + {c02} sqrt({sq02}) and {c01} - {c02} sqrt({sq02})")
                    else:
                        #if denominator is not 1 or -1, print it
                        print(f" 0's = ({c01} + {c02} sqrt({sq02})) / {d02} and ({c01} - {c02} sqrt({sq02})) / {d02}")
                else:
                    #different denominators
                    if c01 == d02 or c01 == -d02:
                        if c02 == 1 or c02 == -1:                    
                            print(f" 0's = ({c01} + sqrt({sq02})) / {d03} and ({c01} - sqrt({sq02})) / {d03}")
                        else:
                            print(f" 0's = ({c01} + {c02} sqrt({sq02})) / {d03} and ({c01} - {c02} sqrt({sq02})) / {d03}")
                    else:
                        if c02 == 1 or c02 == -1:                    
                            print(f" 0's = ({c01} / {d02} + sqrt({sq02})) / {d03} and ({c01} / {d02} - sqrt({sq02})) / {d03}")
                        else:
                            print(f" 0's = ({c01} / {d02} + {c02} sqrt({sq02})) / {d03} and ({c01} / {d02} - {c02} sqrt({sq02})) / {d03}")
            
            if not square_list:
                y = 0
                while y < num:
                    factor_tree = []
                    for i in range(2, num):
                        if num % i == 0:    
                            num /= i
                            factor_tree.append(i)
                            y = 0
                        else:
                            y += 1
                fraction_list = []
                reducefract(-n01, d01, fraction_list)
                join_tree = ", ".join(map(str, factor_tree))
                print(f" ({fraction_list[0]} +- sqrt ({join_tree})) / {fraction_list[1]}")

        else:
            #is prime number
            print(discriminant, "is a prime number")
            print(f" (-{num2} +- sqrt ({discriminant})) / {2*num1}")
        
    elif sqrt(discriminant).is_integer() == True:
        #perfect square
        add = (-num2 + (discriminant)**0.5)/(2*num1)
        subtract = (-num2 - (discriminant)**0.5)/(2*num1)
        print(f" 0's = {add, subtract}")
    
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
    standardsolution(num1, num2, num3)

def vertex(num1, num2, num3):
    print(f"{num1}(x-{num2})^2+{num3}\n vertex = x: {num2}, y: {num3}")
    #print("not finished yet")
    coef1 = (num2+num2)*num1
    coef2 = ((num2*num2)*num1)+num3
    #print(coef1)
    #print(coef2)
    standardsolution(num1, coef1, coef2)
    
def zeros(num1, mvar, num2, nvar, num3):
    binom1 = num1*(nvar*mvar)
    binom2 = num1*((nvar*num2)+(num3*mvar))
    binom3 = num1*(num3*num2)
    standardsolution(binom1, binom2, binom3)

selection()


#for t1 in range(1, 10):
#    for t2 in range(1, 10):
#        for t3 in range(1, 10):
#            vertex(t1, t2, t3)

#error_list = [num1, num2, num3, factor_list, square_list, fraction_list]
#errorlog(error_list)
