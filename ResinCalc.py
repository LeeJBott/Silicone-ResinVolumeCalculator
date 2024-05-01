import os
from time import sleep
# V=l×w×h
volume = 0

def calc():
    os.system("cls")
    print(f"The volume of your mould is approx: {volume} milileters.")
    sil_ratio = 100 / 105
    catalyst_ratio = 5 / 105
    silicone_needed = volume * sil_ratio
    catalyst_needed = volume * catalyst_ratio
    return print(f"Silicone Needed: {round(silicone_needed, 2)} - Catalyst Needed: {round(catalyst_needed, 2)}")

def info():
    os.system("cls")
    print("Raw Silicone: 100 Parts.\nCatalyst/Activator: 5 Parts")
    sleep(4)

def vol():
    os.system("cls")
    global volume
    print("First find the volume of your mould...")
    print("Make sure to leave room for model/casting object displacement!")
    side_A = float(input("Side A in cm: eg. '12.4': "))
    side_B = float(input("Side B in cm: "))
    side_C = float(input("Side C in cm: "))
    volume = side_A * side_B * side_C
    calc()
    
if __name__ == "__main__":
    print("Silicone Calculator")
    while True:
        print("1: Info\n2: Volume Finder/Calculator\n0: Exit: ")
        ask1 = int(input("> "))
        if ask1 == 1:
            info()
        elif ask1 == 2:
            vol()
        elif ask1 == 0:
            break
    print("Bye!")