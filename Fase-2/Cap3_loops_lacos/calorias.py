''' 
Você deve elaborar um algoritmo implementado em Python em que o usuário 
informe quantos alimentos consumiu naquele dia e depois possa informar o número 
de calorias de cada um dos alimentos. Como não estudamos listas neste capítulo, 
você não deve se preocupar em armazenar todas as calorias digitadas, mas deve 
exibir o total de calorias no final. 
'''

total_alimentos = 0
total_calorias = 0.0

while True:
    alimentos = int(input('Quantos alimentos você comeu nesta refeição (ou 0 para encerrar): '))
    if alimentos == 0:
        break  # Encerra o loop se o usuário digitar 0
    total_alimentos += alimentos
    calorias = float(input('Quantas calorias você ingeriu nesta refeição: '))
    total_calorias += calorias

if total_alimentos > 0:
    media_calorias = total_calorias / total_alimentos
    print(f"\nVocê comeu um total de {total_alimentos} alimentos e ingeriu {total_calorias:.2f} calorias.")
    print(f"Isso dá uma média de {media_calorias:.2f} calorias por alimento.")
else:
    print("\nVocê não consumiu nenhum alimento hoje.")
