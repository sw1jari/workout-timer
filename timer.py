from time import sleep
import os

#TODO: Implement this in another language that can run natively on android lmaooo

class Timer:
    def __init__(self, sets=0, set_time=0, supersets=0, set_rest_time=0, super_rest_time=0):
        self.sets = sets
        self.set_time = set_time
        self.supersets = supersets
        self.set_rest_time = set_rest_time
        self.super_rest_time = super_rest_time

    def setup(self):
        if not self.sets:
            self.sets = int(input("How many sets do you want to do? "))
        if not self.set_time:
            self.set_time = int(input("How long do you want your sets to be? "))
        if not self.set_rest_time:
            self.set_rest_time = int(input("How much rest between sets do you want? "))
        if not self.supersets:
            self.supersets = int(input("How many supersets do you want to do? "))
        if not self.super_rest_time:
            self.super_rest_time = int(input("How much rest between supersets do you want? "))

    def run(self):
        input("Press ENTER to start.")
        for x in range(self.supersets):
            if x > 0:
                self.countdown(self.super_rest_time, "Time for superset rest")
            for i in range(3):
                self.countdown(5, f"Starting set {i + 1} of {self.sets} in 5s")
                self.countdown(self.set_time, "Go!")
                self.countdown(self.set_rest_time, "Time to rest")
        input("All done!\nPress ENTER to quit.")

    def statusbar(self):
        print(f"\rSets: {self.sets}        Set time (s): {self.set_time}        Supersets: {self.supersets}        "
              f"Set rest time (s): {self.set_rest_time}        Superset rest time (s): {self.super_rest_time}")

    def countdown(self, seconds, message):
        if seconds is None:
            return
        for s in range(seconds):
            clear()
            self.statusbar()
            print(message)
            print(s + 1)
            sleep(1)

def regular(sets=0, set_time=0, supersets=0, set_rest_time=0, super_rest_time=0):
    timer = Timer(sets, set_time, supersets, set_rest_time, super_rest_time)
    timer.run()

def seluyanov():
    set_time = int(input("How long do you want your sets to be? (30-50s) "))
    supersets = int(input("How many supersets do you want to do? (1-3)|(4-9) "))
    timer = Timer(3, set_time, supersets, set_time, 600)
    timer.setup()
    timer.run()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu():
    choice = input("What kind of training do you want to do? (regular, seluyanov, abs) ")
    if choice == 'seluyanov':
        seluyanov()
    elif choice == 'regular':
        regular()
    elif choice == 'abs':
        regular(8, 60, 1, 3, None)

menu()
