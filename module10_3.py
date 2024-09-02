import threading
import time
import random


class Bank:

    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        minimum_ = 50
        maximum_ = 500
        for i in range(100):
            addition = random.randint(minimum_, maximum_)
            self.balance = self.balance + addition
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            print(f"Пополнение: {addition}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        minimum_ = 50
        maximum_ = 500
        for j in range(100):
            subtraction = random.randint(minimum_, maximum_)
            print(f"Запрос на {subtraction}")
            if subtraction <= self.balance:
                self.balance = self.balance - subtraction
                print(f"Снятие: {subtraction}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()
            time.sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')
