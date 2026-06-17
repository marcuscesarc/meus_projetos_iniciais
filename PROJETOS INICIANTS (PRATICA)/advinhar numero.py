import random

print("E que tal uma aposta? Eu irei escolher um numero, tente advinhar!")

while True:
    choice_number = input("Digite um número limite para o desafio: ")
    if choice_number.isdigit():
        choice_number = int(choice_number)
        break
    else:
        print("OPA OPA AMIGAO, o valor não é um numero! Tente novamente.")

random_number = random.randint(0, choice_number)

while True:
    escolha_usuario = input("Advinhe o numero: ")

    if not escolha_usuario.isdigit():
        print("Valor não é um numero, tente novamente.")
        continue

    escolha_usuario = int(escolha_usuario)

    if escolha_usuario < random_number:
        print("Muito baixo! Tente um número maior.")
    elif escolha_usuario > random_number:
        print("Muito alto! Tente um número menor.")
    else:
        print(f"PARABÉNS! Você acertou! O número era {random_number}.")
        break
 

