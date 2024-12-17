# Solicite ao usuário um número e verifique se é positivo, negativo ou zero

try:
    numero = int(input("Insira um número: "))

    # Verifica se o número é positivo ou negativo
    if numero > 0:
        print("Esse número é positivo")
    elif numero < 0:
        print("Esse número é negativo")
    else:
        print("Esse número é zero")

except ValueError:
    print("Por favor, insira um número válido.")


# Solicite ao usuário um número e verifique se é divisível por 2

try:
    numero = int(input("Insira um número: "))

    # Verifica se o número é divisível por 2
    if numero % 2 == 0:
        print("Esse número é divisível por 2")
    else:
        print("Esse número não é divisível por 2")

except ValueError:
    print("Por favor, insira um número válido.")
             