import random
import time
#Quicksort variante Lomuto (pivo esquerda)
#v = vetor, #p = posição inicial r = posição final
def quicksort(v, p, r):
    #condição de parada    
    if p < r:
        q = particionar(v, p, r)
        quicksort(v, p, q-1)#Pivotar a esquerda (ordenar os elementos menores que o pivo)
        quicksort(v, q+1, r)#Pivotar a direita (ordenar os elementos maiores que o pivo)

def particionar(v, p, r):
    x = v[p]#Escolhendo o Pivô (é o primeiro elemento da esquerda)
    i = p #destino final do pivo (posição)
    j = i + 1 # Contador para percorrer o restante do vetor

    while j <= r: #R representa a ultima posição do vetor  "virtual" contendo todos os elementos compara posição de j com r
        if v[j] < x: #se valor de j é menor que valor x
            i += 1 #Aqui detectou-se um elemento menor que o pivo, incrementa i
            trocar(v, i, j) 
        j += 1 #passa para o proximo elemento

    trocar(v, p, i)#trocando posição inicial

    return i #posição final do pivo

#trocar(v, i, j) o valor de i vai ser passado pra n e o valor de j vai ser passado pra m
#trocar(v, p, i) Assim como o valor de p vai ser passado para n e o valor de i passado para m
def trocar(v, n, m):
    temp = v[n]
    v[n] = v[m]
    v[m] = temp


vetor = list(range(0,1000))
random.shuffle(vetor)
print(vetor)
antes = time.time()
quicksort(vetor, 0, len(vetor)-1)
depois = time.time()
total = (depois - antes) * 1000 #Conversão para ms
print(vetor)
print("O tempo total foi: %0.2f ms" % total)