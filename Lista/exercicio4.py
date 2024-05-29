from Node import Node
from ListaSE import ListaSE

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

# Função para fundir duas listas duplamente encadeadas ordenadas
def merge_lists(head1, head2):
    # Nó dummy para facilitar a fusão
    dummy = Node(0)
    tail = dummy

    # Percorrer ambas as listas
    while head1 and head2:
        if head1.value < head2.value:
            tail.next = head1
            head1.prev = tail
            head1 = head1.next
        else:
            tail.next = head2
            head2.prev = tail
            head2 = head2.next
        tail = tail.next

    # Anexar a lista restante
    if head1:
        tail.next = head1
        head1.prev = tail
    elif head2:
        tail.next = head2
        head2.prev = tail

    # Retornar a cabeça da lista fundida
    return dummy.next

# Função para imprimir a lista duplamente encadeada
def print_list(head):
    while head:
        print(head.value, end=" <-> ")
        head = head.next
    print("None")

# Exemplo de uso
# Criando duas listas duplamente encadeadas ordenadas
head1 = Node(1)
head1.next = Node(3)
head1.next.prev = head1
head1.next.next = Node(5)
head1.next.next.prev = head1.next

head2 = Node(2)
head2.next = Node(4)
head2.next.prev = head2
head2.next.next = Node(6)
head2.next.next.prev = head2.next

# Fundindo as listas
merged_head = merge_lists(head1, head2)

# Imprimindo a lista fundida
print_list(merged_head)
