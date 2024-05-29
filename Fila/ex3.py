'''
Dada uma fila com um número par de elementos,
reorganiza-a de modo que a segunda metade esteja com a primeira metade

Escreva uma função que recebe uma Fila contendo  um número par de elementos.
A função deve reorganizar a fila de forma que o primeiro elemento seja seguido pelo elemento do meio,
seguido pelo segundo elemento , pelo prizimo elemento depois do do meio e assim por diante...
Exemplo: 
Fila = 1, 2, 3, 4, 5, 6
Fila_reorgranizada = 1, 4, 2, 5, 3, 6
'''


from Fila import Fila

def reorganiza_fila(fila_principal):
    # Crio 2 filas para armazenar cada metade dos elementos recebidos
    fila1metade = Fila()
    fila2metade = Fila()

    # Aqui eu crio um contador que pode contar o número de elementos existentes
    count = fila_principal.size()

    # Verificando se o número de elementos é par
    if count % 2 == 0:
        # Aqui eu enfileiro apenas metade dos elementos
        for _ in range(count // 2):
            fila1metade.push(fila_principal.pop())

        # Aqui eu enfileiro a outra metade dos elementos
        for _ in range(count // 2):
            fila2metade.push(fila_principal.pop())

        # Aqui eu desenfileiro alternadamente das duas filas e enfileiro na fila reorganizada
        #Criei uma lista para guardar os desenfileiramentos de fila1metade e fila2metade
        #criei com o nome fila sabendo que é uma lista para facilitar ja que o exercicio pede a filar reorganizada
        fila_reorganizada = []
        while not fila1metade.is_empty() and not fila2metade.is_empty():
            fila_reorganizada.append(fila1metade.pop())
            fila_reorganizada.append(fila2metade.pop())
         #Imprima a lista reorganizada e a original
        print("Fila principal: ", fila_principal)
        print("Fila reorganizada: ", fila_reorganizada)
    else:
        print("O numero de elemtos não é par, insira um numero par de elementos")

# Solicite ao usuário que insira um número par
n = int(input("Digite um valor par de elementos da fila: "))



# Verifique se o número inserido é par
if n % 2 != 0:
    print("O número inserido não é par. Por favor, insira um número par.")
else:
    # Crie uma fila e enfileire os elementos
    fila_principal = Fila()
    for i in range(1, n+1):
        fila_principal.push(str(i))

    # Chame a função com a fila como argumento
    reorganiza_fila(fila_principal)
    