import random

num_sec = random.randint(0, 10)

print("Adivinhe o número de 0 a 10! Você pode ter 3 tentativas.")	
for i in range(3):
    palpite = int(input("Qual seu palpite?\n""R: "))

    if palpite == num_sec:
        print("Parabéns, você acertou!\n")
        break
    elif palpite > num_sec:
        print("É menor. Tente novamente.\n")
    elif palpite < num_sec:
        print("É maior. Tente novamente.\n")
    else:
        print("Tente novamente")