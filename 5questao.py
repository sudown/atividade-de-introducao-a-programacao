#5° eleição naruto

import math

print("ELEIÇÃO")
while True:
    try:                                                            #tenta converter para inteiro
        votos_naruto = int(input("Digite os votos de Naruto: "))
        votos_sakura = int(input("Digite os votos de Sakura: "))
        votos_shin = int(input("Digite os votos de Shin: "))        
        votos_invalidos = int(input("Digite a soma dos votos brancos e mulos: ")) 
        math.sqrt(votos_naruto), math.sqrt(votos_sakura), math.sqrt(votos_shin), math.sqrt(votos_invalidos) 
        break
    except ValueError: #se retornar ValueError é porque o usuario não digitou um numero
        print("Digite apenas numeros inteiros e positivos")

soma_validos = votos_naruto + votos_sakura + votos_shin


if votos_invalidos < soma_validos:
    if (votos_naruto > votos_sakura) and (votos_naruto > votos_shin):
        print(f"Naruto venceu com {votos_naruto * 100 / soma_validos:.2f} % dos votos validos")
    elif(votos_sakura > votos_naruto) and (votos_sakura > votos_shin):
        print(f"Sakura venceu com {votos_sakura * 100 / soma_validos:.2f} % dos votos validos")   #Exibe o vencedor com porcentagem
    elif (votos_shin > votos_naruto) and (votos_shin > votos_sakura):
        print(f"Shin venceu com {votos_shin * 100 / soma_validos:.2f} % dos votos validos")
else:
    print ("Eleição invalida, votos invalidos maior que 50%")
