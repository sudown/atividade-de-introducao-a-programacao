#9 Faça um programa que leia a temperatura da água e informe o estado da mesma.

while True:
    try:
        temp = float(input("Digite a temperatura da água: "))
        break
    except ValueError:
        print("Digite apenas números positvos")

if (temp > 100):
    print("A água está em estado gasoso")
elif (temp >= 0):
    print("A água está em estado liquido")
else:
    print("A água está em estado solido")