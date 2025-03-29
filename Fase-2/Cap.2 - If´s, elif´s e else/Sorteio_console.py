playstation = 0
xbox = 0
nintendo = 0

voto_1 = input('Digite qual video game o membro 1 escolhe:Playstation - Xbox - Nintendo. R: ')
voto_2 = input('Digite qual video game o membro 2 escolhe:Playstation - Xbox - Nintendo. R: ')
voto_3 = input('Digite qual video game o membro 3 escolhe:Playstation - Xbox - Nintendo. R: ')
voto_4 = input('Digite qual video game o membro 4 escolhe:Playstation - Xbox - Nintendo. R: ')
voto_5 = input('Digite qual video game o membro 5 escolhe:Playstation - Xbox - Nintendo. R: ')

if voto_1.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_1.upper() == 'XBOX':
    xbox = xbox + 1
elif voto_1.upper() == "NINTENDO":
    nintendo = nintendo + 1

if voto_2.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_2.upper() == 'XBOX':
    xbox = xbox + 1
elif voto_2.upper() == "NINTENDO":
    nintendo = nintendo + 1

if voto_3.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_3.upper() == 'XBOX':
    xbox = xbox + 1
elif voto_3.upper() == "NINTENDO":
    nintendo = nintendo + 1

if voto_4.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_4.upper() == 'XBOX':
    xbox = xbox + 1
elif voto_4.upper() == "NINTENDO":
    nintendo = nintendo + 1

if voto_5.upper() == "PLAYSTATION":
    playstation = playstation + 1
elif voto_5.upper() == 'XBOX':
    xbox = xbox + 1
elif voto_5.upper() == "NINTENDO":
    nintendo = nintendo + 1

print(f'PLaystation = {playstation}'
      f'\nXbox = {xbox}'
      f'\nNintendo = {nintendo}')

if playstation > xbox and playstation > nintendo:
    print("O vídeo game escolhido foi o Playstation!")
elif nintendo > xbox and nintendo > playstation:
    print("O vídeo game escolhido foi o Nintendo!")
elif xbox > nintendo and xbox > playstation:
    print("O vídeo game escolhido foi o Xbox!")
