#2° formula para peso idea

import math

while True:
    try:                                        #tenta converter para inteiro
        sexo = int(input("Digite 1 para feminino e 2 para masculino: "))
        altura = float(input("Digite sua altura: "))
        math.sqrt(sexo), math.sqrt(altura)        #se a raiz quadrada der erro é porque o numero é negativo
        break
    except ValueError: #se retornar ValueError é porque o usuario não digitou um numero
        print("Digite apenas numeros")

if (sexo == 1):
    print("Seu peso ideal é: ",(62.1 * altura) - 44.7)
elif (sexo == 2):
    print("Seu peso ideal é: ",(72.2 * altura) - 58)
else:
    print("Digite apenas 1 ou 2")