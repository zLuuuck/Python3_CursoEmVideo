enunciado ='''
Desenvolva um programa que leia o comprimento 
de três retas e diga ao usuário se elas podem 
ou não formar um triângulo.
'''

txt = '''
─░▄█▀▄─▒██▄░▒█▌─░▄█▀▄─▒██░░░░▐██▒▄█▀▀█─░▄█▀▄─░▐█▀█▄▒▐█▀▀█▌▒▐█▀▀▄
░▐█▄▄▐█▒▐█▒█▒█░░▐█▄▄▐█▒██░░░─░█▌▒▀▀█▄▄░▐█▄▄▐█░▐█▌▐█▒▐█▄▒█▌▒▐█▒▐█
░▐█─░▐█▒██░▒██▌░▐█─░▐█▒██▄▄█░▐██▒█▄▄█▀░▐█─░▐█░▐█▄█▀▒▐██▄█▌▒▐█▀▄▄
                        ░▐█▀█▄░▐█▀▀
                        ░▐█▌▐█░▐█▀▀
                        ░▐█▄█▀░▐█▄▄
▒█▀█▀█▒▐█▀▀▄░▐██─░▄█▀▄─▒██▄░▒█▌░▐█▀▀▀─▒█▒█▒██░░░▒▐█▀▀█▌▒▄█▀▀█
░░▒█░░▒▐█▒▐█─░█▌░▐█▄▄▐█▒▐█▒█▒█░░▐█░▀█▌▒█▒█▒██░░░▒▐█▄▒█▌▒▀▀█▄▄
░▒▄█▄░▒▐█▀▄▄░▐██░▐█─░▐█▒██░▒██▌░▐██▄█▌▒▀▄▀▒██▄▄█▒▐██▄█▌▒█▄▄█▀
'''
print(txt)

r1 = float(input('Digite o 1° segmento: '))
r2 = float(input('Digite o 2° segmento: '))
r3 = float(input('Digite o 3° segmento: '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('pode ser um triângulo')
else:
    print('não é um triângulo')
