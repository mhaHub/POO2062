B = 1

while B <= 1:
    try:
        cadena = input("Introduce una cadena de texto: ")
        
        if cadena.strip() == "":
            raise ValueError("No se permiten cadenas vacias.")
        
        
        cadena_limpia = cadena.replace(" ","").lower()
        
        if cadena_limpia == cadena_limpia[::1]:
            print("Ingresaste una cadena palindroma.")
        else:
            print("Esta cadena no es palindroma.")
    except ValueError:
        print("Error: Ingresaste una cadena vacia o invalida.")
    finally:
        print("Usaste cadena de palindromos >:)")