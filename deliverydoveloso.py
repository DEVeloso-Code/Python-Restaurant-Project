print('𝑨𝒑𝒑 𝑫𝒆𝒍𝒊𝒗𝒆𝒓𝒚 𝒅𝒐 𝑽𝒆𝒍𝒐𝒔𝒐\n')

print('1. Cadastrar restaurante')
print('2. Listar restaurante')
print('3. Ativar restaurante')
print('4. Sair\n')

opcao_escolhida = int(input('Escolha uma opção: '))
print(f'Você escolheu a opção {opcao_escolhida}')

if opcao_escolhida == 1:
    print('Cadastrar restaurantes')
elif opcao_escolhida == 2:
    print('Listar restaurantes')
elif opcao_escolhida == 3:
    print('Ativar restaurante')
else:
    print('Encerrando o programa')