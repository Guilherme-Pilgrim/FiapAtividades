'''Observando o mercado de educação infantil, você e sua equipe decidem 
criar um aplicativo por meio do qual as crianças aprendam a controlar os seus gastos.  
Como forma de validar um protótipo, foi solicitado que você crie um script 
simples, em que o usuário deve informar QUANTAS TRANSAÇÕES financeiras 
realizou ao longo de um dia e, na sequência, deve informar o VALOR DE CADA UMA 
das transações que realizou. 
Seu programa deverá exibir, ao final, o valor total gasto pelo usuário, bem como 
a média do valor de cada transação. '''

print("Olá, seja bem-vindo ao nosso aplicativo de controle financeiro!")
quant_transacoes = int(input('Quantas transações você fez hoje? '))
total = 0.0

for i in range(quant_transacoes):
    valor = float(input(f'Informe o valor fa transação n.{i+1}: '))
    total += valor
    
media = total / quant_transacoes
print(f'Você fez {quant_transacoes} transações e gastou um total de R$ {total:.2f}.')
print(f'A média de cada transação foi de R$ {media:.2f}.')