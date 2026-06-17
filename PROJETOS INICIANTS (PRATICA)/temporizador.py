import time

t = input("Digite o tempo (em segundos):")

if t.isdigit():
    t = int(t)
else:
    print("Entrada Invalida")
    exit()


while t:
    min, sec = divmod(t, 60)
    timer = "{:02d}:{:02d}".format(min,sec)
    print(timer, end="\r")
    time.sleep(1)
    t = t - 1

print("ACABOU O TEMPO!")
