from Node import Node
from ListaSE import ListaSE

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Função para adicionar um nó ao final de uma lista encadeada circular
def add_to_end(head, value):
    new_node = Node(value)
    if head is None:
        head = new_node
        head.next = head  # Faz a lista ser circular
    else:
        current = head
        while current.next != head:
            current = current.next
        current.next = new_node
        new_node.next = head
    return head

# Função para rotacionar a lista encadeada circular
def rotate_list(head, k):
    if head is None:
        return None

    # Encontrar o último nó e o tamanho da lista
    last = head
    size = 1
    while last.next != head:
        size += 1
        last = last.next

    # Ajustar k para garantir que está dentro do intervalo do tamanho da lista
    k = k % size

    # Se k for 0, não é necessário rotacionar
    if k == 0:
        return head

    # Encontrar o novo último nó após a rotação
    temp = head
    for i in range(size - k - 1):
        temp = temp.next
    new_head = temp.next

    # Rotacionar a lista
    temp.next = head
    last.next = new_head
    return new_head

# Exemplo de uso
head = Node(1)
head = add_to_end(head, 2)
head = add_to_end(head, 3)
head = add_to_end(head, 4)

# Rotacionar a lista em 2 posições
head = rotate_list(head, 2)

# Função para imprimir a lista encadeada circular
def print_list(head):
    if head is None:
        return
    print(head.value, end=" -> ")
    current = head.next
    while current != head:
        print(current.value, end=" -> ")
        current = current.next
    print("(volta ao início)")

# Imprimir a lista encadeada circular rotacionada
print_list(head)
