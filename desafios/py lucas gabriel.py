import threading
import time

class Conta:
    def __init__(self):
        self.saldo = 1000

    def depositar(self, valor):
        saldo_atual = self.saldo
        time.sleep(0.1)  # simula atraso
        self.saldo = saldo_atual + valor

    def sacar(self, valor):
        saldo_atual = self.saldo
        time.sleep(0.1)  # simula atraso
        self.saldo = saldo_atual - valor


conta = Conta()

thread_a = threading.Thread(target=conta.depositar, args=(500,))
thread_b = threading.Thread(target=conta.sacar, args=(200,))

thread_a.start()
thread_b.start()

thread_a.join()
thread_b.join()

print(f"Saldo final: R${conta.saldo}")