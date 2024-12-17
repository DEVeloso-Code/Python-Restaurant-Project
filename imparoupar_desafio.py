# Exercício: Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

# Solicita ao usuário um número
numero = int(input("Digite um número: "))

# Verifica se o número é par ou ímpar
if numero % 2 == 0:
    print(f"O número {numero} é par.")
else:
    print(f"O número {numero} é ímpar.")
