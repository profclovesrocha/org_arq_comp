#Aluno: Arthur José Arruda Pessoa Brandão
#Matricula: 01895179
#Turma: ADS(manhã)

import threading # aqui ele está utilizando o modúlo que trabalha com os threads

saldo = 1000
lock = threading.Lock() # é um bloqueador para que as threads não sejam executadas tudo de uma vez(da forma errada) e crashe um programa.

def lucro(): # criando a função adicionar() para que adicione(+=) 500
    global saldo# avisando que a variável é global, ou seja, ela está em todo programa.
    with lock: # pegando o bloqueio para que a função remover(), não interfira essa função
        saldo += 500

def gasto(): # criando a função remover() para remover(-=) 200.
    global saldo # avisando que a variável é global, ou seja, ela está em todo programa.
    with lock: # pegando o bloqueio para que a função adicionar, não interfira essa função
        saldo -= 200

t1 = threading.Thread(target=lucro) # tanto a t1 como t2, irão executar as threads
t2 = threading.Thread(target=gasto)

t1.start()#aqui é o ínicio da execução
t2.start()

t1.join()#eperando as threads terminar
t2.join()

print('\033[32mO seu saldo é igual a : R${}'.format(saldo))#fim da execução