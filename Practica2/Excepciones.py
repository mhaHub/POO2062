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