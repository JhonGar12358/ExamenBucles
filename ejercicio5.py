# Ejercicio 5: Cálculo de Impuesto sobre la Renta
# Pide al usuario que ingrese su salario anual. Calcula el impuesto sobre la renta de acuerdo con las siguientes reglas:
# Si el salario es menor o igual a $10,000, no se aplica impuesto.
# Si el salario es mayor de $10,000 pero menor o igual a $50,000, se aplica un 10% de impuesto.
# Si el salario es mayor de $50,000 pero menor o igual a $100,000, se aplica un 20% de impuesto.
# Si el salario es mayor de $100,000, se aplica un 30% de impuesto.



def tax(salario):
    if salario <= 10000:
        paga= print('no paga impuesto')

    elif salario > 10000 and salario <= 50000:
        impuesto = (salario*10)/100
        paga = print('su impuesto es el 10% de su salario, debe pagar:',  impuesto)

    elif salario > 50000 and salario <= 100000:
        impuesto = (salario*20)/100
        paga = print('su impuesto es el 20% de su salario, debe pagar:', impuesto)

    elif salario > 100000:
        impuesto = (salario*30/100)
        paga = print('su impuesto es el 30% de su salario, debe pagar:',  impuesto)

salario = int(input('ingrese su salario anual: '))

tax(salario)

