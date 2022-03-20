#8 – Faça um programa que leia o tipo de figura geométrica (retângulo, triângulo ou círculo) e informe a área da mesma. Obs: Cada figura tem uma forma específica para calcular a área.

import math

while True:
    try:
        opcao = int(input("Digite 1- para retangulo, 2- para triangulo, 3- para circulo e qualquer numero para sair: "))
        break
    except ValueError:
        print("Digite apenas numeros")


if opcao == 1:
    print("A área do retângulo é dada por base x altura")
    while True:
        try:
            altura = float(input("Digite a altura: "))
            largura = float(input("Digite a largura: "))
            math.sqrt(altura), math.sqrt(largura)
            break
        except ValueError:
            print("Digite apenas numeros positivos")
    
    area = altura * largura
    print(f"A area do seu retangulo é {area:,.2f}")


elif opcao == 2:
    print("A área do triângulo é dada por (base x altura) / 2")
    print("A área do retângulo é dada por base x altura")
    while True:
        try:
            base = float(input("Digite a base: "))
            altura = float(input("Digite a altura: "))
            math.sqrt(altura), math.sqrt(base)
            break
        except ValueError:
            print("Digite apenas numeros positivos")
    
    area = base * altura
    print(f"A area do seu triangulo é {area:,.2f}")


elif opcao == 3:
    print("A área do círculo é dada por 3.14 x raio^2")
    while True:
        try:
            raio = float(input("Digite o raio: "))
            math.sqrt(raio)
            break
        except ValueError:
            print("Digite apenas numeros positivos")
    
    area = 3.14 * (raio * raio)
    print(f"A area do seu circulo é {area:,.2f}")


else:
    print("tchau")