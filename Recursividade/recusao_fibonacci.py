#Exercício função recursiva - Fibonacci
# Sequencia Fibonacci: 0 1 1 2 3 5 8 13 21 34 55 89...
#           Posições:    1 2 3 4 5 6  7  8  9  10 11...

def fibonacci(posicao):
    if posicao <=1:
        return posicao
    else:
        return fibonacci(posicao-1) + fibonacci(posicao-2)
    
a = int(input("Digite o valor da posição fibonacci"))
resultado = fibonacci(a)
print("Na %d posição o valor é" %(a, resultado))