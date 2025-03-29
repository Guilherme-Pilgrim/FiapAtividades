rm = input('Por favor, digite seu RM: ')
idade = int(input('Por favor, digite sua idade: '))

if idade >= 18:
    print("\nSua participação foi autorizada, aluno de RM {}.".format(rm))
    print('Mais instruções serão enviadas ao seu email cadastrado na FIAP!')
else:
    autorizado = input("\nVocê possui autorização dos responsáveis para participar? S - SIM ou N - NÃO ")
    if autorizado.lower() == "s":
        print("\nSua participação foi autorizada, aluno de RM {}.".format(rm))
        print('Mais instruções serão enviadas ao seu email cadastrado na FIAP!')
    else:
        print("\nSua párticipação não foi autorizada por causa da sua idade.")
