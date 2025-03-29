idade = int(input("por favor, digite sua idade: "))
bpm = int(input("Por favor, agora digite sua frequência cardíaca (BPM): "))

if idade >= 60:
    if bpm > 60:
        print('Sua frequência cardíaca está acima do normal.')
    elif bpm < 50:
        print('Sua frequência cardíaca está abaixo do normal')
    else:
        print('Sua frequência cardíaca está normal!')
elif idade >= 18:
    if bpm > 80:
        print('Sua frequência cardíaca está acima do normal.')
    elif bpm < 70:
        print('Sua frequência cardíaca está abaixo do normal')
    else:
        print('Sua frequência cardíaca está normal!')
elif idade >= 8:
    if bpm > 100:
        print('Sua frequência cardíaca está acima do normal.')
    elif bpm < 80:
        print('Sua frequência cardíaca está abaixo do normal')
    else:
        print('Sua frequência cardíaca está normal!')
else:
    if bpm > 140:
        print('Sua frequência cardíaca está acima do normal.')
    elif bpm < 120:
        print('Sua frequência cardíaca está abaixo do normal')
    else:
        print('Sua frequência cardíaca está normal!')