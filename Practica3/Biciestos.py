A = 1
while A <= 1:
    try:
        año = int(input("Introduce un año: "))
        
        if (año % 4 == 0 and año % 100 != 0) or (año % 400 ==0):
            print("es un año bisiesto" )
        else:
            print("no es un año bisiesto" )
    except ValueError:
        print("Error: Introduce un numero entero")