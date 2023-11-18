# Escribe un programa que utilice bucles "for" para imprimir el siguiente patrón de asteriscos:
# *
# **
# ***
# ****
# *****

n = 5


def asteriscos(n):
    
    for i in range(1, n + 1):
        for j in range(i):
            print('* ', end='')
        print()

asteriscos(n)