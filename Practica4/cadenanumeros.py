B = 1

while B <=1 :
    try:
        numero = int(input("Introduce un numero entero: "))
        
        if numero < 0:
            print("Solo se permiten numeros mayores a 0.")
        else:
            Valor = ", ".join(str(i) for i in range(numero, -1,-1))
            print("Resultados desde", numero, "hasta 0 es: ", Valor)
    
    except ValueError:
        print("Ingresaste un valor que no es un numero negativo.")
    finally:
        print("Realmente lo infinito no tiene Fin???")