from Fila import Fila
from Pilha import Pilha

def inverte_fila(dados_fila):
    # Create an empty auxiliary queue
    Pilha_auxiliar = Pilha()

    # Remove elements from the original queue and insert them into the auxiliary queue
    while not dados_fila.is_empty():
        elemento = dados_fila.pop()
        Pilha_auxiliar.push(elemento)

    # Reinsert elements from the auxiliary queue back into the original queue
    while not Pilha_auxiliar.is_empty():
        elemento = Pilha_auxiliar.pop()
        dados_fila.push(elemento)

# Example usage
if __name__ == "__main__":
    # Create a sample queue with elements 1 to 5
    fila_original = Fila()
    for i in range(1, 6):
        fila_original.push(i)

    # Invert the order of elements in the queue
    inverte_fila(fila_original)

    # Print the inverted queue
    while not fila_original.is_empty():
        print(fila_original.pop())
        