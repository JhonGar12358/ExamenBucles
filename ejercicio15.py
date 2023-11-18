# Desarrolla un programa que solicite al usuario ingresar un número y luego genere un patrón de asteriscos. 
# Si el número es par, el patrón debe ser una serie de asteriscos en una fila. Si el número es impar, 
# el patrón debe ser una serie de asteriscos en múltiples filas. 
# Utiliza un bucle "for" y condicionales "if" para lograr esto.

def asteriscos(numero):
    
    if numero % 2 == 0:
        print("*"*numero)
    else:
        for i in range(numero):
            print("*" * (i+ 1))

numero = int(input("Ingrese un numero: "))

asteriscos(numero)