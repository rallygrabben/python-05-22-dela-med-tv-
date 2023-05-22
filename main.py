import os

def printTitle():
    os.system('cls')
    title = print("----------------------------------Is Dividable by 2----------------------------------")

printTitle()

inputNumber = input("\n\tInput a Number:")

if (int(inputNumber) % 2 == 0):
    printTitle()
    
    print(f"\n\t{inputNumber} is dividable by 2")
else:
    print(f"\n\t{inputNumber} is NOT divisible by 2\n\n")

