#6° faça um programa que leia três valores inteiros e informe se foram um triângulo retângulo.

import math

print("Diga me 3 angulos e eu direi se eles formam um triangulo retangulo")

angulo =["", "", ""]
while True:
    try:
        angulo[0] = int(input("Digite o valor do primerio angulo: "))
        angulo[1] = int(input("Digite o valor do segundo angulo: "))
        angulo[2] = int(input("Digite o valor do terceiro angulo: "))
        math.sqrt(angulo[0]), math.sqrt(angulo[1]), math.sqrt(angulo[2])
        break
    except ValueError:
        print("Digite apenas numeros inteiros positivos")

qnt_90 = 0
soma_angulos = 0
for i in angulo:
    soma_angulos = soma_angulos + i #incrementa a soma dos angulos
    if (i == 90):
        qnt_90 = qnt_90 + 1 #incrementa a quntidade de angulos retos

if (qnt_90 == 1 and soma_angulos == 180): #valida se e um triangulo
    print("Seu triangulo é retangulo")

else:
    print("Seu triangulo não é retangulo")