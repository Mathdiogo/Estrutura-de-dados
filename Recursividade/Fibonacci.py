#SEQUENCIA DE FIBONACCI: 0 1  1  2  3  5  8  13  21  34  55  89 ...
#              posições:   1º 2º 3º 4º 5º 6º  7º  8º  9º 10º 11º...

def fibonacci(posicao):
    if posicao <=1: #caso base
        return posicao
    else:
        return fibonacci(posicao-1) + fibonacci(posicao-2)
a = int(input("Digite a posição: "))
res = fibonacci(a)
print("NA %dº posicção, o valor fibonacci é: \033[1;33m %d" % (a,res))
            