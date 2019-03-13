#Teste de mecânicas
#Versão: Beta
#Author: Erick Melo

#---------Bibliotecas importadas-----------
import pygame
import math
from time import sleep
from random import randint
#----------Algumas variaveis importantes de Armas, danos e vida do personagem-------
espada = randint(7,9)
arco = randint(1,3)
cajado = randint(3,16)
punho = randint(3,12)
hp = int
mana = int

#-------Variaveis usadas para simular o HP dos monstros-------
orc = 9
dragon = 15
cavaleiro = 10
goblin = 7

#-------Variaveis usadas para simular o dano dos monstros-------
n1 = randint(3,6)
n2 = randint(5,8)
n3 = randint(7,12)
#------------Personagens--------------------
gm='(Jogo): '
unknow='(???): '
art='(Arthur): '

#---------Classe-----------------
classe=str
#------Teste de apresentação e um possível combate atribuindo primeiro valor a variavel de ação----------
arma = int(input('{}Olá aventureiro, qual arma você tem mais aptidão para manejar? 1- Espada | 2- Arco | 3- Cajado '.format(gm)))
sleep(2)
print('Vejamos que tipo de guerreiro você é...')
if arma==1:
    arma=espada
    classe='Espadachim'
    hp= 17
    mana= 4
    sleep(2)
    print('As espadas não dependem de mana e nem de flechas, logo nunca te deixão na mão. Boa escolha!')
    sleep(3)
    print('Você é certamente um Espadachim!')
    print('Você possuí ({} HP) e ({} SP)'.format(hp,mana))
elif arma==2:
    arma=arco
    classe='Arqueiro'
    hp= 12
    mana= 6
    sleep(2)
    print('Uma das mais antigas ferramentas de caça. Use bem suas flechas, elas podem ser letais!')
    sleep(3)
    print('Parece que temos um Arqueiro aqui, hein?')
    print('Você possuí ({} HP) e ({} SP)'.format(hp,mana))
elif arma==3:
    arma = cajado
    classe='Mago'
    hp=8
    mana=13
    sleep(2)
    print('Uma das armas mais difíceis de serem dominadas. Interessante! Magias são extremamente poderosas')
    sleep(3)
    print('Claramente você é um Mago!')
    print('Você possuí ({} HP) e ({} SP)'.format(hp,mana))
else:
    arma = punho
    classe = 'Monge'
    hp = 16
    mana = 6
    sleep(3)
    print('Não usa armas? Corajoso você!')
    sleep(2)
    print('Com toda essa coragem e aparentemente se recusa pegar em armas, você deve ser um Monge. Faz tempo que não vejo um!')
    print('Você possuí ({} HP) e ({} SP)'.format(hp,mana))
sleep(4)
acao = int(input('Você está caminhando e avista um Orc({} HP), o quê você faz?  1- Atacar | 2- Fugir | 3- Fingir de morto '.format(orc)))
sleep(1)
if acao == 2:
    print ('Você corre que nem uma mocinha mas consegue manter o traseiro a salvo!')
elif acao == 3:
    print ('Tu tenta dar um migué no bixo mas ele tá esperto e te come na porrada')
elif acao == 1 :
    print('Você causou {} de dano no Orc! '.format(arma))
    print('O Orc está com {} de vida.'.format(orc-arma))
    sleep(1)
    print('Argh...')
    sleep(1)
    if orc-arma<=0:
        print('Está morto')
        sleep(1)
        print('Uau, você realmente é bem forte!')
    if orc-arma>=0:
        print('Esta vivo')
        sleep(1)
        print('É melhor se preparar...')
        sleep(2)
        print('Agora é a vez do inimigo, você está com ({} HP)'.format(hp))
        sleep(2)
        print('O Orc saca seu machado e lhe atinge, causando {} de dano'.format(n1))
        print('Você está com ({} HP)'.format(hp-n1))
else:
    print('Isso não é uma opção válida. Digite um número entre 1 e 3')
        


