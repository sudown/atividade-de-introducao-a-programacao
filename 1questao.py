#1° numeros

while True:
    try:                                        #tenta converter para inteiro
        num1 = int(input("Digite um número: "))
        num2 = int(input("Digite outro número: "))
        break
    except ValueError: #se retornar ValueError é porque o usuario não digitou um numero
        print("Digite apenas números")


if (num2 % 2 == 0): # verifica o resto da divisão se der 0 é par
    print("A soma da ", num1 + num2) #num2 sendo par soma se num1 e num2
else:
    print("A multiplicação da ", num1 * num2) # num2 impar multiplica se num1 e num2