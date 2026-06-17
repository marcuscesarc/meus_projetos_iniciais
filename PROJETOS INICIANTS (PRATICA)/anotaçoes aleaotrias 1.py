print ("Bem-Vindo ao Assistente de Aprovação!")

NOTA1 = float(input("Digite a Primeira Nota: "))
NOTA2 = float(input("Digite a Segunda Nota: "))
PRESENCA = float(input("Digite o número de vezes que o aluno compareceu: "))
print ("AVISO: É CONTABILIZADO AS 4 SEMANAS E 5 DIAS CORRIDOS DURANTE O MÊS, OU SEJA, O TOTAL SERIA 20 DIAS AO MÊS")
TOTAL_AULAS = float(input("Digite o total de aulas: "))


MEDIA = (NOTA1 + NOTA2) / 2
FREQ = (PRESENCA / TOTAL_AULAS) * 100

print(f"MÉDIA: {MEDIA:.1f}")
print(f"Frequência: {FREQ:.1f}%")


if MEDIA >= 7.0 and FREQ >= 0.75 * 100:
	print("Este Aluno foi APROVADO!")
elif MEDIA >= 5.0 and FREQ >= 0.75 * 100:
	print("Este Aluno está em Recuperação...")
else:
	print("Este Aluno está REPROVADO!")