import threading
import time

saldo = 1000

lock = threading.Lock()

def adicionar():
    global saldo

    lock.acquire()

    valor = saldo
    time.sleep(1)

    valor = valor + 500
    saldo = valor

    print("Thread A -> saldo:", saldo)

    lock.release()

def remover():
    global saldo

    lock.acquire()

    valor = saldo
    time.sleep(1)

    valor = valor - 200
    saldo = valor

    print("Thread B -> saldo:", saldo)

    lock.release()

t1 = threading.Thread(target=adicionar)
t2 = threading.Thread(target=remover)

t1.start()
t2.start()

t1.join()
t2.join()

print("Saldo final:", saldo)