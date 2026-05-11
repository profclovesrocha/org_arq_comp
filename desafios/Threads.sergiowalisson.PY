import threading

saldo = 1000
lock = threading.Lock()

def adicionar():
    global saldo
    with lock:
        saldo += 500

def remover():
    global saldo
    with lock:
        saldo -= 200

t1 = threading.Thread(target=adicionar)
t2 = threading.Thread(target=remover)

t1.start()
t2.start()

t1.join()
t2.join()

print(saldo)