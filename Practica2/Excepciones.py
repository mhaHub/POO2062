#1. Manejo de Excepciones
#try:
   # numero = int(input("Introduce un numero: "))
    #resultado = 10 / numero

    #print("Resultado:", resultado)

#except ValueError:
    #print("Error: Se ingreso algo que no es un numero entero.")
#except ZeroDivisionError:
    #print("Error: Estas intentando dividir entre 0")
    
#2. Multiples Excepciones
#try:
    #resultado = 10 / 0
#except(ZeroDivisionError, TypeError) as error:
    #print(f"!Error! {error}")

#3. Finally
try:
    numero = int(input("Introduce un numero: "))
    resultado = 10 / numero

    print("Resultado:", resultado)

except ValueError:
    print("Error: Se ingreso algo que no es un numero entero.")
except ZeroDivisionError:
    print("Error: Estas intentando dividir entre 0")
finally:
    print("Cerrando Programa...")
    
#Usar Raise

def validar_edad(edad):
    if edad < 0:
        raise ValueError("La edad no puede ser negativa")
    if edad < 18:
        raise ValueError("Debes ser mayor de edad")
    print("Edad válida")

try:
    edad = int(input("Ingrese su edad: "))
    validar_edad(edad)
except ValueError as e:
    print(f"Error: {e}")
else:
    print("Puedes continuar")