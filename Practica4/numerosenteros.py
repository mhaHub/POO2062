B = 1

while B <= 1:
    try:
        numero = int(input("Introduce un numero entero: "))
        
        if numero <= 10:
            print("El numero debe ser mayor a 10")
        else:
            impares = [str(i) for i in range(2, numero + 1) if i % 2 != 0]
            resultado = ", ".join(impares)
            print("Los numero impares desde 2 hasta", numero, "son: ")
            print(resultado)
    except ValueError:
        print("Ingresaste un valor que no es un numero entero.")
    finally:
        print("Los numero pares e impares son familia???")
            