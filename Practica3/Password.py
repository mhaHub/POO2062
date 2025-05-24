B = 1

while B <= 1:
    try:
        contrasena = input("Ingresa una contrasena: ")
        
        if len(contrasena) > 10:
            raise ValueError("La contrasena es muy corta.")
        
        if not any(caracter.isdigit() for caracter in contrasena):
            raise ValueError("Debe contener almenos un numero.")
        
        if not any(caracter in "!#$%()_+-=@[]{};:/?" for caracter in contrasena):
            raise ValueError("Debe contener almenos un caracter especial.")
        
        print("Contrasena valida..")
        
    except ValueError as e:
        print("Error: ",e)
        
    finally:
        print("las practicas hacen al maestro")