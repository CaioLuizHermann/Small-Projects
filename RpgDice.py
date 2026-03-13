value = 0
import random
dice = input(int("Choose one of the dices bellow! \n <1> d6 \n <2> d16 \n <3> d20 \n <4> d100 \n <5> create your own dice!"))
if dice == 1:
    value = random.randint(1,6)
    print("The result is...", valor)
elif dice == 2:
    value = random.randint(1,16)
    print("The result is...", valor)
elif dice == 3:
    value = random.randint(1,20)
    print("The result is...", valor)
elif dice == 4:
    value = random.randint(1,100)
    print("The result is...", valor)
elif dice == 5:
    Min = input(int("Insira o número mínimo do seu dado \n"))
    Max = input(int("Insira o número máximo do seu dado \n"))
    value = random.randint(Min, Max)
    print("The result is...", valor)
elif dice >= 6 or dice <= 0:
    print("Error, invalid number")