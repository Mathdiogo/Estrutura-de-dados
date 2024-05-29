from Node import Node
from Fila import Fila

def preencher_fila(fila_principal):
    print("Insira até 10 elementos na fila (digite 'sair' para terminar):")
    contador = 0
    while contador < 10:
        entrada = input("Elemento: ")
        if entrada.lower() == 'sair':
            break
        fila_principal.push(entrada)
        contador += 1

def intercalar_fila(fila_principal):
    if fila_principal.is_empty():  
        return

    # tamanho da fila principal
    tamanho = 0
    fila_temporaria = Fila()
    while not fila_principal.is_empty():
        fila_temporaria.push(fila_principal.pop())
        tamanho += 1

    # Verificar se é par
    if tamanho % 2 != 0:
        return

    # Colocar os elementos de volta na fila principal
    for _ in range(tamanho // 2):
        fila_principal.push(fila_temporaria.pop())

    # Intercalar os elementos da fila temporária com a fila principal
    for _ in range(tamanho // 2):
        elemento_frente = fila_principal.pop()
        elemento_meio = fila_temporaria.pop()
        fila_principal.push(elemento_frente)
        fila_principal.push(elemento_meio)

fila_principal = Fila()
preencher_fila(fila_principal)
intercalar_fila(fila_principal)

# Imprimir a fila reorganizada
while not fila_principal.is_empty():
    print(fila_principal.pop(), end=' ')
