import sys
def main():
    dsumadd = 0
    sumadd = 0
    num = int(input("Number: "))
    while num <= 0:
        num = int(input("Number: "))
    add1 = num
    while add1 > 0:
        lastdigit = add1 % 10
        sumadd += lastdigit
        add1 //= 100
    add2 = num // 10
    while add2 > 0:
        lastdigit2 = add2 % 10
        doubledigit = lastdigit2 * 2
        if doubledigit > 9:
            together = doubledigit % 10 + 1
            dsumadd += together
        else:
            dsumadd += doubledigit
        add2 //= 100
    fsum = dsumadd + sumadd
    if fsum % 10 != 0:
        print ("INVALID")
    else:
        if ((num >= 340000000000000 and num <= 349999999999999) or (num >= 370000000000000 and num <= 379999999999999)):
            print ("AMEX")
        elif ((num >= 5100000000000000 and num <= 5599999999999999)):
            print ("MASTERCARD")
        elif ((num >= 4000000000000 and num <= 4999999999999) or (num >= 4000000000000000 and num <= 4999999999999999)):
            print ("VISA")
        else:
            print ("INVALID")
    
    
main()