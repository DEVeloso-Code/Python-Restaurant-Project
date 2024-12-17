# Exercício 1: Solicite ao usuário que insira um número e, em seguida, use uma estrutura if else para determinar se o número é par ou ímpar.

    # Solicita ao usuário um número
    numero = int(input("Digite um número: "))

    # Verifica se o número é par ou ímpar
    if numero % 2 == 0:
        print(f"O número {numero} é par.")
    else:
        print(f"O número {numero} é ímpar.")

# Exercício 2: Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

    # Solicita a idade ao usuário
    idade = int(input("Digite sua idade: "))
    
    # Verifica a faixa etária
    if 0 <= idade <= 12:
        print("Você é uma criança!")
    elif 13 <= idade <= 18:
        print("Você é um adolescente!")
    else:
        print("Você é um adulto!")

