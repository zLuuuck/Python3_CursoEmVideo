enunciado ='''
Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo 
que ele foi multado. A multa vai custar R$7,00 por cada 
Km acima do limite.
'''

vel = int(input('Qual a velocidade atual do carro? '))

if vel > 80:
    print('Você foi multado!')
    multa = (vel - 80) * 7
    print(f'Deverá pagar uma multa de R${multa:.2f}!')
else:
    print('Tenha um bom dia! Dirija com segurança!')
