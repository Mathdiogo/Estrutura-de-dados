# Configuração de Fila

class Node:
    def __init__(self, dado):
        self.value = dado # Conteudo do nó
        self.next = None # Ponteiro para o próximo nó
        self.prev = None # Ponteiro para o nó anterior

class Node:
    def __init__(self, dado):
        self.value = dado
        self.next = None
        self.prev = None

class ListaDuplamenteLigada:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self,value):
        #adiciona nó ao final da lista
        new_node = Node(value)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node


    def display(self):
        current = self.head
        while current:
            print(current.value, end=' <-> ' if current.next else '')
            current = current.next
        print()

    def remove(self, value):
# """Remove um nó da lista pelo valor."""
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return True # Nó encontrado e removido
            current = current.next
        return False # Nó não encontrado

    def length(self):
        current = self.head
        count = 0
        while True:
            count += 1
            if current == self.tail:
                break
            current = current.next
        return count
    
# Sort functions
def bubble_sort(lista, order):
    n = lista.length()
    for i in range(n):
        trocou = False
        current = lista.head
        while current != lista.tail:
            next_node = current.next
            if (order == 'C' and current.value > next_node.value) or (order == 'D' and current.value < next_node.value):
                current.value, next_node.value = next_node.value, current.value
                trocou = True
            current = current.next
        if not trocou:
            break
    return lista

def insertion_sort_1(lista, order):
    if order == 'C':
        # Crescente
        current = lista.head
        while current != lista.tail:
            next = current.next
            current = current.next

            while current != lista.head and current.prev.value > current.value:
                current.prev.value, current.value = current.value, current.prev.value

                current = current.prev
                # lista.display()
                # print(current.value)


        return lista
    else:
        # Decrescente
        current = lista.head
        while current != lista.tail:
            next = current.next
            current = current.next

            while current != lista.head and current.prev.value < current.value:
                current.prev.value, current.value = current.value, current.prev.value

                current = current.prev
                lista.display()
                # print(current.value)
        # return lista


def quick_sort(lista, order):

    pivot = lista.head.next
    left = lista.head
    right = lista.tail
    
    # Crescente
    if(order == 'C'):
        while left is not pivot:
            if left.value > right.value:
                left.value, right.value = right.value, left.value
            left = left.next
            
        while right is not pivot:
            if right.value < left.value:
                left.value, right.value = right.value, left.value
            right = right.prev
        
        if right is pivot and left is pivot:
            if left.next is None and right.prev is None:
                return lista
            quick_sort(left,order)
            quick_sort(right,order)
            
    
    else:
        while left is not pivot:
            if left.value < right.value:
                left.value, right.value = right.value, left.value
            left = left.next
            
        while right is not pivot:
            if right.value > left.value:
                left.value, right.value = right.value, left.value
            right = right.prev
        
        if right is pivot and left is pivot:
            if left.next is None and right.prev is None:
                return lista
            quick_sort(left,order)
            quick_sort(right,order)
             
    
    
    
    
    # print(pivot.value)
    # print(left.value)
    # print(right.value)

##APP
def getAscDesc():
        while True:
            asc_desc = input("Ordenar em ordem crescente (C) ou decrescente (D)? ").upper()
            if asc_desc == "C" or asc_desc == "D":
                return asc_desc
            else:
                print("Opção invalida")

lista = ListaDuplamenteLigada()
cont = True

while cont:
    while True:
        valor = input("Insira um numero para adicionar à lista: ")

        # Confirma se não é outro caracter alem de numero
        if valor.isnumeric() == False:
            print("Valor invalido, por favor insira um numero")
        else:
            break

    lista.insert(valor)
    while cont:
        op = input("Deseja adicionar mais um numero? (S/N): ")

        if op.lower() == 'n' or op.lower() == 's':
            # Verificar se está ente SIM ou NAO

            if op.lower() == 'n':
                if lista.length() <= 1:
                    print("A lista não possui numeros sufcientes para ordenar")
                else:
                    # Acessado apenas se a lista possuir numeros sufcientes
                    cont = False
            else:
                # sair do looping de verificação quando SIM
                break
        else:
            print("Opção invalida")



print("Lista atual: ")
lista.display()


while True:
    print("\n")
    print("Escolha a forma de ordenação: ")
    print("1. Bubble Sort")
    print("2. Insertion Sort")
    print("3. Quick Sort")
    ord = input("Digite o numero da escolha: ")

    if ord == '1':
        print(" Bubble Sort selecionado")
        ordType = getAscDesc()
        bubble_sort(lista,ordType)
        break
    elif ord == '2':
        print(" Insertion Sort selecionado")
        ordType = getAscDesc()
        insertion_sort_1(lista,ordType)
        break
    elif ord == '3':
        print(" Quick Sort selecionado")
        ordType = getAscDesc()
        quick_sort(lista,ordType)
        break
    else:
        print("Opção invalida. Selecione uma opção entre as disponiveis")

print("\n")
print("Lista Ordenada: ")
lista.display()


