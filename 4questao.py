#4° Faça um programa que informe quantas placas de vibranium serão necessárias para revestir o muro.
#O muro tem 100m x 4m
#As placas são de 2mx2m

muro_area = 100*4
placa_area = 2*2

print("A quantidade de placas nescessarias pra o muro são: ", muro_area/placa_area)
print("A quantidade de placas nescessarias pra o muro são: ", (100*4)/(2*2)) #qual sera que é o melhor?
print("A quantidade de placas nescessarias pra o muro são: ", 400/4) #p.s aparentemente a diferença é minima, mas se for um programa gigante talvez seja melhor este 3° metodo

#rodando com o comando time no terminal
#-------------1 modo---------------
#real    0.01s
#user    0.01s
#sys     0.00s
#cpu     96%


#-------------2 modo---------------
#real    0.01s
#user    0.01s
#sys     0.00s
#cpu     95%

#-------------3 modo---------------
#real    0.01s
#user    0.01s
#sys     0.00s
#cpu     88%