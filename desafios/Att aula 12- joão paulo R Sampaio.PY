import threading
import time
saldo = 1000


def adicionar():
    global saldo

valor = saldo
time.sleep(0.5)

valor += 500
saldo = valor 

print("Thread A adicionar R$500")   
print("saldo atual:", saldo)

def subtrair():
    global saldo

valor = saldo
time.sleep(0.5)

valor -= 200
saldo = valor 

print("Thread B Subtrair R$200")   
print("saldo atual:", saldo)
print("saldo final:", saldo)
        
        
Thread1 = threading.Thread(target=adicionar)
Thread2 = threading.Thread(target=subtrair)

Thread1.start()
Thread2.start()
Thread1.join()
Thread2.join()
