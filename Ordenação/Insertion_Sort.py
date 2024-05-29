import random
import time

def insertion_sort(v):
    i = 1 
    while i < len(v):
        temp = v[i]
        trocou = False
        j = i-1
        while j >=0 and v[j] > temp: #comparar os elementos anteriores com meu elemento atual (temp)
            v[j+1] = v[j] #"Empurrando a posição de j para frente"
            trocou = True
            j -= 1
        if trocou:
            v[j+1] = temp
        
        i += 1
    
    
vetor = list(range(0,5))
random.shuffle(vetor)
antes = time.time()
insertion_sort(vetor)
depois = time.time()
total = (depois - antes)*1000

print(vetor)

print("O tempo total foi: %0.2f ms" % total)