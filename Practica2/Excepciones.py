#Manejo de Excepciones
#try:
    #numero = int(input("Introduce un numero: "))
    #resultado = 10 / numero

    #print("Resultado:", resultado)

#except ValueError:
    #print("Error: Se ingreso algo que no es un numero entero.")
#except ZeroDivisionError:
    #print("Error: Estas intentando dividir entre 0")
    
#Multiples Excepciones
try:
    resultado = 10 / 0
except(ZeroDivisionError, TypeError) as error:
    print(f"!Error! {error}")