version = "1.0.0"
prevResult = 0
operationList = ["Addition", "Subtraction","Multiplikation" ,"Division", "Potenz", "Mod", "ggT"]

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
    result = zahl1 / zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Potenz(zahl1,zahl2):
    result = zahl1**zahl2
    global prevResult
    prevResult = result
    print(f" Result:  \n {result} ")
    return result

def Mod(zahl1,zahl2):
    result = zahl1 % zahl2
    result2 = zahl1 // zahl2
    global prevResult
    prevResult = result
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
    print(F"Error: ggT")
    return result

def Start():
    print("-------------------------------------------------------------------------------------------------------------------------")
    print(f" GTT CALC Version: {version}, made by Ganztagszocker")
    print("-------------------------------------------------------------------------------------------------------------------------")
    print()
    Menu()

def Menu():
    print("--------------------------------------------------------------------------------------------------------------------------")
    for index, operation in enumerate(operationList):
        print(f"{index} : {operation} ")

    userInput = int(input())

    match userInput:
        case 0:
            print("Summand 1: ...")
            zahl1 = int(input())
            print("Summand 2: ...")
            zahl2 = int(input())
            Addition(zahl1, zahl2)
        
        case 1:
            print("Minuend:...")
            zahl1 = int(input())
            print("Subtrahend:...")
            zahl2 = int(input())
            Subtraction(zahl1, zahl2)

        case 2:
            print("Faktor 1:...")
            zahl1 = int(input())
            print("Faktor 2:...")
            zahl2 = int(input())
            Multiplikation(zahl1, zahl2)

        case 3:
            print("Divident:...")
            zahl1 = int(input())
            print("Divisor:...")
            zahl2 = int(input())
            Division(zahl1, zahl2)

        case 4:
            print("Base:...")
            zahl1 = int(input())
            print("Potenz:...")
            zahl2 = int(input())
            Potenz(zahl1, zahl2)

        case 5:
            print("Divident:...")
            zahl1 = int(input())
            print("Divisor:...")
            zahl2 = int(input())
            Mod(zahl1, zahl2)

        case 6:
            print("Zahl 1:...")
            zahl1 = int(input())
            print("Zahl 2:...")
            zahl2 = int(input())
            ggT(zahl1, zahl2)
    Menu()
        
Start()
