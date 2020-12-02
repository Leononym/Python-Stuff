# TODO:
# Levelsystem:
#   Es werden immer 5 Aufgaben gestellt. Dann wird das Level erhöht,
#   d.h. die Zahlen, aus denen die Aufgaben gestellt werden, werden immer komplizierter.
#   Das Spiel endet, wenn man länger als 1 Minute braucht. Wer schafft es ins höchste Level?
# Levelerweiterung:
#   Pro falsche Aufgabe gibt es fünf Strafsekunden.
#   Wenn man inkl der Strafsekunden über eine Minute kommt, hat man nicht verloren,
#   kommt aber nicht ins nächste Level, sondern muss das aktuelle Level noch einmal spielen.

from random import randint
import time

correct = 0
false = 0
answers = []
amount = input("Wie viele Aufgaben?\n-->")

while str(type(amount)) != "<class 'int'>":
    try:
        amount = int(amount)
    except:
        amount = input("\x1b[0;31;49mUngültige Eingabe!\x1b[0m\nBitte gebe eine Zahl an!\n-->")

if amount > 32:
    amount = 32
    print("Aufgabenanzahl wurde auf 32 gesetzt.")
elif amount < 1:
    amount = 1
    print("Aufgabenanzahl wurde auf 1 gesetzt.")

print("\x1b[0;34;48mAchtung!\x1b[0m"
      f"\nDu bekommst gleich {amount} Aufgaben gestellt."
      "\nDies können normale Kopfrechenaufgaben sein(plus, minus und mal) oder einfache Potenz- und Wurzelaufgaben.\n\n\n")


class Tasks:
    def __init__(self):
        pass

    tasks = {}

    def generate_tasks(self, amount=10):
        while len(self.tasks) != amount:
            x = randint(0, 2)
            if x == 0:
                # Wurzeln
                solution = randint(0, 8)
                n = randint(1, 5)
                answer = solution ** n
                while answer > 256:
                    n -= 1
                    answer = solution ** n
                task = f"Die {n}-te Wurzel aus {solution ** n}:"
                self.tasks[task] = solution
            elif x == 1:
                # Potenzrechnung
                solution = randint(0, 8)
                n = randint(1, 5)
                answer = solution ** n
                while answer > 256:
                    n -= 1
                    answer = solution ** n
                task = f"{solution} hoch {n}:"
                self.tasks[task] = solution ** n
            else:
                # kopfrechenaufgaben
                rechenart = randint(0, 2)
                if rechenart == 0:
                    # plus
                    a = randint(0, 512)
                    b = randint(0, 512)
                    task = f"{a} + {b}:"
                    self.tasks[task] = a + b
                elif rechenart == 1:
                    # minus
                    a = randint(0, 512)
                    b = randint(0, 512)
                    task = f"{a} - {b}:"
                    self.tasks[task] = a - b
                else:
                    # mal
                    a = randint(0, 32)
                    b = randint(0, 32)
                    task = f"{a} * {b}:"
                    self.tasks[task] = a * b


aufgabe = Tasks()
aufgabe.generate_tasks(amount)

start = time.time()

for i in aufgabe.tasks:
    answer = input(i)
    if int(answer) == int(aufgabe.tasks[i]):
        correct += 1
        answers.append("\x1b[0;32;49m" + str(i) + " = " + str(aufgabe.tasks[i]) + "\x1b[0m")
        print("\x1b[0;32;49m\tRichtig!\x1b[0m")
    else:
        answers.append("\x1b[0;31;49m" + str(i) + " = " + str(answer) + "\x1b[0m" + " --> " + "\x1b[0;32;49m" + str(
            i) + " = " + str(aufgabe.tasks[i]) + "\x1b[0m")
        false += 1
        print("\x1b[0;31;49m\tFalsch!\x1b[0m")

time = time.time() - start

print(f"\nDu brauchtest {round(time, 3)} Sekunden um {amount} Aufgaben zu beantworten.\n"
      f"Davon waren {correct} Aufgaben richtig und {false} Aufgaben falsch!\n"
      f"\nAlle Aufgaben mit Lösungen:")
for i in answers:
    print(i)
