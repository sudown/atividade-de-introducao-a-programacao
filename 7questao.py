#Faça um programa que leia três valores inteiros. Informe se esses valores forma um triângulo. Caso forme, informe que tipo de triângulo foi formado: isósceles, equilátero ou escaleno.

import math

print("Diga me 3 arestas e eu direi se elas formam um triangulo isoceles, equilatero ou escaleno")

aresta = ["", "", ""]
while True:
    try:
        aresta[0] = int(input("Digite o valor da primeira aresta : "))
        aresta[1] = int(input("Digite o valor da segunda aresta: "))
        aresta[2] = int(input("Digite o valor da terceira aresta: "))
        math.sqrt(aresta[0]), math.sqrt(aresta[1]), math.sqrt(aresta[2])
        break
    except ValueError:
        print("Digite apenas numeros")

arestas_validas = 0
soma_arestas = aresta[0] + aresta[1] + aresta[2]
for i in aresta:
    if i <= (soma_arestas / 2): #verifica se um lado não é maior que a soma dos outros dois
        arestas_validas = arestas_validas + 1

arestas_iguais = len((set(aresta))) #exclui as repetições

#arestas_iguais = 0
#for i in range(3):
#    for j in range(3):                     estava tentando fazer na mao, mas ainda nãoconsegui
#        print(aresta[i],":",aresta[j])
#        if aresta[i] == aresta[j]:
#            arestas_iguais = arestas_iguais + 1


if (arestas_validas == 3 and arestas_iguais == 2): #se arestas_iguais == 2 quer dizer que tem dois numeros repetidos
    print("Seu triangulo é isoceles")

elif (arestas_validas == 3 and arestas_iguais == 1): #todas as arestas sao repetidas
    print("Seu triangulo é equilatero")

elif (arestas_validas == 3 and arestas_iguais == 3): #todas as arestas sao diferentes
    print("Seu triangulo é escaleno")
else:
    print("Nao é triangulo")