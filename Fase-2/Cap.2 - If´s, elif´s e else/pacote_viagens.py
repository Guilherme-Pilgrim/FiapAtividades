categoria = input('Bem vindo a AirLines Magic'
                  '\nEm nossa companhia temos as seguintes categorias de assentos'
                  '\n1 - Econômica'
                  '\n2 - Executiva'
                  '\n3 - Primeira Classe'
                  '\nDigite o número correspondente a categoria desejada: ')
valor_bruto = float(input('Por favor, digite o valor do pacote de viagens: '))
quant_viajentes = int(input('Qual a quantidade de viajantes? '))

match categoria:
    case '1':
        print('Você selecionou a classe Econômica.\n')
        if quant_viajentes >= 4:
            valor_liq = valor_bruto * 0.95
            desc = valor_bruto * 0.05
            print(f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                  f'\nO valor médio por viajante fica {valor_liq/quant_viajentes}.')
        elif quant_viajentes ==3:
            valor_liq = valor_bruto * 0.96
            desc = valor_bruto * 0.04
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        elif quant_viajentes == 2:
            valor_liq = valor_bruto * 0.97
            desc = valor_bruto * 0.03
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        else:
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, não tem desconto.')
    case '2':
        print('Você selecionou a classe Executiva.\n')
        if quant_viajentes >= 4:
            valor_liq = valor_bruto * 0.92
            desc = valor_bruto * 0.08
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        elif quant_viajentes == 3:
            valor_liq = valor_bruto * 0.93
            desc = valor_bruto * 0.07
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        elif quant_viajentes == 2:
            valor_liq = valor_bruto * 0.95
            desc = valor_bruto * 0.05
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        else:
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, não tem desconto.')
    case '3':
        print('Você selecionou a Primeira classe.\n')
        if quant_viajentes >= 4:
            valor_liq = valor_bruto * 0.80
            desc = valor_bruto * 0.20
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        elif quant_viajentes == 3:
            valor_liq = valor_bruto * 0.85
            desc = valor_bruto * 0.15
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        elif quant_viajentes == 2:
            valor_liq = valor_bruto * 0.90
            desc = valor_bruto * 0.10
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, teve um desconto de {desc} reais, ficando no valor de {valor_liq}.'
                f'\nO valor médio por viajante fica {valor_liq / quant_viajentes}.')
        else:
            print(
                f'Sua viajem, no valor de {valor_bruto} reais, não tem desconto.')