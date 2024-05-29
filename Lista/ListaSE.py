from Node import Node

class ListaSE:
    def __init__(self):
        self.head = None #cabeça da lista
        
    def insert(self, data):
        #insere um nó no inicio da lista
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        
    def remove(self, data):
        #Remove um nó da lista pelo valor
        current = self.head
        prev = None
        while current is not None:
            if current.value == data:
                if prev:
                    prev.next = current.next
                else:
                    self.head = current.next
                return True #dado encontrado e demovido
            prev = current
            current = current.next
        return False #Dado nao encontrado
    
    def display(self):
        #Exibe os elementos da lista
        current = self.head
        while current:
            print(current.value, end= ' -> ')
            current = current.next
        print('None')