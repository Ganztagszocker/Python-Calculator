import os
import sys

sys.set_int_max_str_digits(0)

version = "1.1.0"
prevResult = 0
operationList = ["Addition", "Subtraction","Multiplikation" ,"Division", "Potenz", "Mod", "ggT"]
firstMenuCall = True

cmd = 'mode 120,30'
os.system(cmd)

cmd = 'color b'
os.system(cmd)

def Addition(zahl1, zahl2):
    result = zahl1 + zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Subtraction(zahl1,zahl2):
    result = zahl1 - zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Multiplikation(zahl1, zahl2):
    result = zahl1 * zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Division(zahl1, zahl2):
    if(zahl2 == 0):
        print(f"Error: Zero Division" "\n")
        Menu()
        return
    result = zahl1 / zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Potenz(zahl1, zahl2):
    result = zahl1 ** zahl2
    global prevResult
    prevResult = result
    result_str = str(result)
    if len(result_str) > 1000:
        print(f"Result has: {len(result_str)} Stellen, \n Mod nutzen?: \n [y/n]" )

        userInput = str(input())

        match userInput:
            case "y":
                print(f"Mod?: ...")
                divisor = int(input())
                Mod(result, divisor)
                return result

            case "n":
                print(result)
                return result
        
    else:
            print(f"Result: \n {result} ")
            return result
    print(result)

def Mod(zahl1,zahl2):
    if(zahl2 == 0):
        print(f"Error: Zero Division" "\n")
        Menu()
        return
    result = zahl1 % zahl2
    result2 = zahl1 // zahl2
    global prevResult
    prevResult = result

    result2_str = str(result2)
    if len(result2_str) > 1000:
        print(f"Häufigkeit has: {len(result2_str)} Stellen, \n Print anyways?: \n [y/n]" )
        userInput = str(input())
        match userInput:
            case "y":
                print(f"Result: {result2}")

            case "n":
                print(f"Rest: {result}")
                return
    else:
        print(f" \n Rest: {result} \n Häufigkeit: {result2}")
    return result

def ggT(zahl1, zahl2):
    a = zahl1
    b = zahl2
    while True:
        r = a % b
        if r == 0:
            result = b
            print(f" \n Result: {result}")
            return result
        a = b
        b = r

def Start():
    print("------------------------------------------------------------------------------------------------------------------------")
    print(f" GTT CALC Version: {version}, made by Ganztagszocker")
    print("------------------------------------------------------------------------------------------------------------------------")
    print()
    Menu()

def Menu():
    
    global firstMenuCall
    if firstMenuCall == True:
        print("----------------------------------------------------------------------------------------------------------------------")
        firstMenuCall = False
    for index, operation in enumerate(operationList):
        print(f"{index+1} : {operation} ")

    userInput = int(input())

    match userInput:
        case 1:
            print("Summand 1: ...")
            zahl1 = int(input())
            print("Summand 2: ...")
            zahl2 = int(input())
            Addition(zahl1, zahl2)
        
        case 2:
            print("Minuend:...")
            zahl1 = int(input())
            print("Subtrahend:...")
            zahl2 = int(input())
            Subtraction(zahl1, zahl2)

        case 3:
            print("Faktor 1:...")
            zahl1 = int(input())
            print("Faktor 2:...")
            zahl2 = int(input())
            Multiplikation(zahl1, zahl2)

        case 4:
            print("Divident:...")
            zahl1 = int(input())
            print("Divisor:...")
            zahl2 = int(input())
            Division(zahl1, zahl2)

        case 5:
            print("Base:...")
            zahl1 = int(input())
            print("Potenz:...")
            zahl2 = int(input())
            Potenz(zahl1, zahl2)

        case 6:
            print("Divident:...")
            zahl1 = int(input())
            print("Divisor:...")
            zahl2 = int(input())
            Mod(zahl1, zahl2)

        case 7:
            print("Zahl 1:...")
            zahl1 = int(input())
            print("Zahl 2:...")
            zahl2 = int(input())
            ggT(zahl1, zahl2)
    Menu()
        
Start()
