import random
import time

def bubble_sort(v):
    
    fim = len(v)
    
    while fim > 0:
        
        i = 0
        #Percorrendo o vetor de 0 até fim i = 0, vai incrementando para comparar com fim
        while i < fim-1:
            if v[i] > v[i+1]: # Se o valor atual do meu vetor for maior que o proximo valor do meu vetor
                #Realizando a troca da posição atual pela proxima
                temp = v[i] #Troca as posições. Pego o valor atual e guardo em temp
                v[i] = v[i+1] #Pego o valor do proximo valor e coloco na casa atual
                v[i+1] = temp  #Valor que estava na casa atual que foi guardado em temp é trocado e colocado no proximo valor
                print(v)
            i += 1
        fim -= 1
        
vetor = list(range(0,5))
random.shuffle(vetor)

print(vetor)#Imprimindo vetor desordenado

antes = time.time()
bubble_sort(vetor)#Ordenando Vetor
depois = time.time()
total = (depois - antes)*1000

print(" O tempo total foi: %0.2f ms" % total)