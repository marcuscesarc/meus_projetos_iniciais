import random

pontos_usuario = 0
pontos_pc = 0


opçoes = ["r", "t", "p"]


while True:
    escolha_usuario = input("Escolha R para Pedra, T para Tesoura e P para \nPapel, ou E para sair!").lower()


    if escolha_usuario == "E":
        break
    escolha_pc = random.randint(0,2)
# 0 para R, 1 para T e 2 para P
    opcao_pc = opçoes [escolha_pc]
    
    print("A Maquina escolheu:" + str(escolha_pc))


if escolha_usuario == opcao_pc:
    print("Empate")
elif escolha_usuario == "r" and opcao_pc == "t":
    print("You WIN!")
    pontos_usuario = pontos_usuario + 1

elif escolha_usuario == "p" and opcao_pc == "r":
    print("You WIN!")
    pontos_usuario = pontos_usuario + 1

elif escolha_usuario == "t" and opcao_pc == "p":
    print("You WIN!")
    pontos_usuario = pontos_usuario + 1

else:
    print("Loser!")
    pontos_pc = pontos_pc + 1


print("Sua pontuação:"+ pontos_usuario)
print("Pontuação do Computador:" + pontos_pc)

if pontos_pc > pontos_usuario:
    print("Derrota!")
elif pontos_pc == pontos_usuario:
    print("Vocês empataram!")
else:
    print("Você VENCEU!")

print ("Tchau!")




