
print('Sejam Bem-vindos ao QUIZ FODA!')
resposta_usuario = input("Você gostaria de Começar? (S/N)").upper()
print (resposta_usuario)

if resposta_usuario == "S":
    print('Começando... \n Vamos Lá!')
else:
    print("Ok, nos vemos na próxima!")
    exit()

pontos = 0

print("Que ano Markow lançou seu primeiro single?\n A) 2019 \n B) 2020 \n C) 2021 \n D) 2023")
resposta_pergunta1 = input("Essa é sua Resposta: ").upper()

while True:
    resposta_pergunta1 = input("Sua resposta (A/B/C/D): ").upper().strip()
    if resposta_pergunta1 in ["A", "B", "C", "D"]:
        break
    print("Resposta inválida! Digite apenas A, B, C ou D.")

if resposta_pergunta1 == "A":
    print("Acertou!!! Você realmente é um fã!")
    pontos = pontos + 1
    print(f"Final do Quiz, seus pontos são: {pontos}/1 ")
    
else:
    print("Errou por pouco, vamos tentar novamente?")


    

