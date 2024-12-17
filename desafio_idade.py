# Exercício: Pergunte ao usuário sua idade e, com base nisso, use uma estrutura if elif else para classificar a idade em categorias de acordo com as seguintes condições:

try:
    idade = int(input("Digite sua idade: "))
    
    # Verifica a faixa etária
    if 0 <= idade <= 12:
        print("Você é uma criança!")
    elif 13 <= idade <= 18:
        print("Você é um adolescente!")
    else:
        print("Você é um adulto!")

except ValueError:
    print("Por favor, insira uma idade válida (um número inteiro).")
