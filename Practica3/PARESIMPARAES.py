#Programa que solicita al usuario un numero entero y muestre por pantalla si es par o impar
B = 1


while B <= 1:
    try:
        numero = int(input("Introduce un numero entero: "))
    
        if  numero % 2 == 0:
            print(numero, "ingresaste un numero par.")
        else:
            print(numero, "ingresaste un numero impar.")
    except ValueError:
        print("Error: Se ingreso una un valor que no es numero entero.")
    finally:
        print("Siguelo intentando :) ")
        
