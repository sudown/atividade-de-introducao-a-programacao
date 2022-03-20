#10° – Faça um programa que leia dois números e informe o menor número.

while True:
    try:
        num1 = float(input("Digite um numero: "))
        num2 = float(input("Digite outro numero: "))
        break
    except ValueError:
        print("Digite apenas números")

if (num1 > num2):
    print("O maior numero é: ", num1)
elif (num2 > num1):
    print("O maior numero é: ", num2)
else:
    print("Os numeros são iguais")