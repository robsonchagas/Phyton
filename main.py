i = 1
while i <= 10:
    entrada = input("Informe um número: ")
    numero = float(entrada.replace(',', '.'))
    if numero > 0:
        print("O número é positivo")
    elif numero < 0:
        print("O número é negativo")
    else:
        print("O número é zero")
    i += 1