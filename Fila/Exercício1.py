from Fila import Fila

def inverte_fila(dados_fila):
    # Crie uma fila auxiliar vazia
    fila_auxiliar = Fila()

    # Remova os elementos da fila original e insira-os na fila auxiliar
    while not dados_fila.is_empty():
        elemento = dados_fila.pop()
        fila_auxiliar.push(elemento)

    # Reinsira os elementos da fila auxiliar de volta na fila original
    while not fila_auxiliar.is_empty():
        elemento = fila_auxiliar.pop()
        dados_fila.push(elemento)

# Exemplo de uso
if __name__ == "__main__":
    # Crie uma fila de exemplo com elementos de 1 a 5
    fila_original = Fila()
    for i in range(1, 6):
        fila_original.push(i)

    # Inverta a ordem dos elementos na fila
    inverte_fila(fila_original)

    # Imprima a fila invertida
    while not fila_original.is_empty():
        print(fila_original.pop())
