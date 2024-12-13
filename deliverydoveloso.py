import os

def exibir_nome_do_programa():
    print('𝑨𝒑𝒑 𝑫𝒆𝒍𝒊𝒗𝒆𝒓𝒚 𝒅𝒐 𝑽𝒆𝒍𝒐𝒔𝒐\n')

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    os.system('cls')
    print('Finalizando o App\n')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        print('Cadastrar restaurantes')
    elif opcao_escolhida == 2:
        print('Listar restaurantes')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()
        print('Encerrando o programa')

def main()
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__'
    main()