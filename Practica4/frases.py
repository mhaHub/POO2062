B = 2

while B <= 2:
    try:
        frase = input("Introduce una frase: ")
        
        if any(char.isdigit() for char in frase):
            raise ValueError("Introduciste un numero")
            
        letra = input("Introduce una letra: ")
        
        if len(letra) != 1:
            print("Please, introduce solo una letra.")
        else:
            cantidad = frase.count(letra)
            print("La letra", letra, "aparece: ", cantidad)
    except ValueError as e:
        print("Error: ", e)