'''
Com as classes Node e Pilha fornecidas na aula de teoria, vamos resolver o Exercício 1: Validador de Parênteses, utilizando esta estrutura de dado para verificar se uma string contendo apenas parênteses ( e ) está balanceada.

A classe Pilha já fornece os métodos necessários para manipular a pilha:
push para adicionar um elemento ao topo;
pop para remover o elemento do topo;
peek para observar o elemento do topo sem removê-lo;
is_empty para verificar se a pilha está vazia. Vamos utilizá-la para implementar a função de validação.

'''
from Pilha import Pilha









def validador_parenteses(string):
    
    pilha = Pilha()

    for char in string:
         #se o caracter for um parenteses aberto, empilha
        if char == "(":
            pilha.push(char)
        #se o caracter for um parenteses fechado
        elif char == ")":
            #se a pilha estiver vazia
            if pilha.is_empty():
                #nao tem caracter correspontendo "("
                return False
            #se não estiver vazia, desempilha o ultimo aprenteses aberto correspondente aberto
            pilha.pop()
    #Após percorrer toda a string, se a pilha estiver vazia, então
    #todos os parenteses abertos fechados corretamente
    return pilha.is_empty()


#Exemplo de uso

string = "((())"
resultado = validador_parenteses(string)
print(resultado)