value = 0
import random
end = False
while end == False:
    dice = int(input("Choose one of the dices bellow! \n <1> d6 \n <2> d16 \n <3> d20 \n <4> d100 \n <5> Create your own dice! \n <6> End Program \n"))
    if dice == 1:
        value = random.randint(1,6)
        print("The result is...", value)
    elif dice == 2:
        value = random.randint(1,16)
        print("The result is...", value)
    elif dice == 3:
        value = random.randint(1,20)
        print("The result is...", value)
    elif dice == 4:
        value = random.randint(1,100)
        print("The result is...", value)
    elif dice == 5:
        Min = int(input("Insira o número mínimo do seu dado \n"))
        Max = int(input("Insira o número máximo do seu dado \n"))
        if Min >= Max:
            print("Error 0, minimum number is greater than the maximum")
        else:
            value = random.randint(Min, Max)
            print("The result is...", value)
    elif dice >= 6 or dice <= 0:
        print("Error: 1, invalid number")
