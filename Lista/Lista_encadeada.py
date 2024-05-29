class Lista:
    class No:
        def __init__(self, valor, next=None):
            self.valor = valor
            self.next = next
            
    def __init__(self):
        self.__head = None
        self.__quantidade = 0 
        
    def __len__(self):
        return self.__quantidade
    
    def insert(self, posicao, valor):
        new_node = self.No(valor) #Instancia o novo no com seu valor
        self.__quantidade += 1
        
        if self.__head is None: #Se a cabeça é None significa que ainda nao temos um nó
            self.__head = new_node #Logo, cabeça recebe novo nó
            return #return aqui funciona igual um break
        #Inserir na cabeça (primeira posicao)
        if posicao <= 0:
            new_node.next = self.__head # O proximo elemento do novo nó recebe a antiga cabeça
            self.__head = new_node      # A cabeça agora recebe o novo nó
            return
       
        i = 0 # indice do elemento atual
        atual = self.__head
        #buscando o elemento anterior a posição que a gente quer inserir #
        # se temos 3 elementos e quero adicionar o 4 ei preciso chegar até o elemento 3
        #apenas o ultimo elemento terá o atual.next como None, entao sabemos onde adicionar
        while atual.next is not None and i < posicao - 1:
            atual  = atual.next
            i  += 1
        #Vai incrementar o i (indice do elemento atual) pra saber a posicao   
        #Vai sair do While quando encontrar o elemento com atual.next None (ultimo elemento da lista)
        
        new_node.next = atual.next
        atual.next = new_node
        
        
        
lista = Lista()

print(len(lista))

lista.insert(0,5) # lista.insert(posicao: 0, valor:5)
lista.insert(1,20)
lista.insert(2,15)
lista.insert(2,7)#Adicionando outro elemento na posicao 2, o que fará com que a lista saia de
                 # 5, 20, 15 para 5, 20, 7, 15
                 #A logica anterior faz com que o next do novo nó aponte para o next do atual
                 #E o next do atual recebe o novo nó
                 #fazendo com quue o 7 seja inserido entre o 20 e 15