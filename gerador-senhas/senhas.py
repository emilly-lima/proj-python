import random


num = random.randint(0, 9)
letra = random.choice(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'])
caractere = random.choice(['!', '#', '$', '%', '&', '(', ')', '*', '+'])

senha = inter(str(num) + str(letra) + str(caractere))
print("Senha gerada: ", senha)