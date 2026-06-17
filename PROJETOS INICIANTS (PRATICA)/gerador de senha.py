import random
import string

def gerador_senhas(tamanho_senha = 8):
    letras_opcoes = string.ascii_letters
    numero_opcoes = string.digits
    pontos_opceos = string.punctuation
    options = letras_opcoes + numero_opcoes + pontos_opceos

    senha_usuario = ""
    for i in range (0, tamanho_senha):
        digit = random.choice(options)
        senha_usuario = senha_usuario + digit

    return senha_usuario
 #o "return" encerra a execuçao
    
escolha_usuario = input("Quanto digitos na senha?")

if escolha_usuario.isdigit():
    escolha_usuario = int(escolha_usuario)
else:
    print("Entrada Invalida")
    quit()

response = gerador_senhas(tamanho_senha = escolha_usuario)
print(f"Senha Gerada:\n{response}")



