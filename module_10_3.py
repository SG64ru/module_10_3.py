
import threading
# from threading import Thread, Lock
import time
import random
# from random import randint


class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        i = 0

        while i < 100:
            self.depo = random.randint(50, 500)
            self.balance +=self.depo
            if self.balance >= 500 and self.lock.locked():
                self.lock.release
            print(f"Пополнение {self.depo}. Баланс :{self.balance}")
            time.sleep(0.001)
            i += 1
        # return self.balance

    def take(self):
        # self.depo_s = random.randint(50, 500)
        j = 0
        while j < 100:
            # j += 1
            self.depo_s = random.randint(50, 500)
            if self.depo_s >= self.balance:
                print(f"Запрос отклонен {self.depo_s}, недостаточно средств")
                # self.lock.acquire()
            # if self.depo_s <= self.balance:
            #     self.balance -= self.depo_s
            #     print(f"Снятие:{self.depo_s}. Баланс:{self.balance}")
            else:

                self.balance -= self.depo_s
                print(f"Снятие:{self.depo_s}. Баланс:{self.balance}")
                # print(f"Запрос отклонен {self.depo_s}, недостаточно средств")
                # self.lock.acquire()
                time.sleep(0.001)

            j += 1

            # return self.balance

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')



