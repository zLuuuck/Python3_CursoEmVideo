enunciado ='''
Um professor quer sortear um dos seus quatro alunos 
para apagar o quadro. Faça um programa que ajude ele
lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
'''

import random

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno: '))
a4 = str(input('Quarto aluno: '))
lista = [a1, a2, a3, a4]
sorteado = random.choice(lista)
print(f'O aluno que vai limpar o quadro é o {sorteado} !')
