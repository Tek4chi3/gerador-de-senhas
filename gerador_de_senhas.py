#Gerador de senhas

import string
from random import randint,choice
senha=[]
senha3=[]
print('='*40)
print('[1] Senha apenas com números')
print('[2] Senha apenas com letras')
print('[3] Senha com números e letras')
print('='*40)
escolha=int(input('Digite sua escolha:'))
caracteres=int(input('Digite quantos caracteres sua senha terá:'))
if escolha==1:
    while len(senha)!=caracteres:
        senha.append(randint(0,9))
        if len(senha)==caracteres:
            print('Sua senha é:',end=' ')
            for c in range(0,len(senha)):
                print(senha[c],end='')
            break
if escolha==2:
    while len(senha)!=caracteres:
        senha.append(chr(randint(ord('a'), ord('z'))))
        if len(senha)==caracteres:
            print('Sua senha é:',end=' ')
            for c in range(0,len(senha)):
                print(senha[c],end='')
            break
if escolha==3:
    while len(senha)!=caracteres:
        senha3.append(chr(randint(ord('a'), ord('z'))))
        senha3.append(randint(0, 9))
        senha.append(choice(senha3))
        senha3.clear()
        if len(senha)==caracteres:
            print('Sua senha é:',end=' ')
            for c in range(0,len(senha)):
                print(senha[c],end='')
            break
