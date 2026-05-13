# Rayanne da Silva Lima de França - 01908958
# Orientador: Clovis Rocha


import threading
import time

saldo = 1000
tranca = threading.Lock()

def atualizar_saldo(valor):
  global saldo
  with tranca:
    atual = saldo
    saldo = atual + valor

t1 = threading. Thread(target= atualizar_saldo,args = (500, ))
t2 = threading. Thread(target= atualizar_saldo,args = (-200, ))

t1.start()
t2.start()

t1.join()
t2.join()

print(f"Saldo final: {saldo}")
