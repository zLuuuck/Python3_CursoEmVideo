enunciado ='''
Melhore o jogo do DESAFIO 28 onde o computador vai 
“pensar” em um número entre 0 e 10. Só que agora o 
jogador vai tentar adivinhar até acertar, mostrando 
no final quantos palpites foram necessários para vencer.
'''

from random import randint

computador = randint(0, 10)
print('Eu sou o computador... ')
print('Acabei de pensar em um número de 0 a 10.')
print('Será que você consegue adivinhar?')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador > computador:
            print('Menos... Tente novamente.')
        elif jogador < computador:
            print('Mais... Tente novamente.')
print(f'Acertou! Você fez {palpite} palpites!')
