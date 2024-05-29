'''
Descrição:
Escreva uma função que recebe uma string como entrada.
Utilizando uma pilha, a função deve inverter a ordem dos caracteres da string.
A função deve retornar a string invertida
'''
from Pilha import Pilha

def inverte_string(string):
    pilha = Pilha()

    for char in string:
        pilha.push(char)

    inverte_string = ""  # Corrigido o nome da variável
    while not pilha.is_empty():  # Corrigido o uso da instância da classe
        inverte_string += pilha.pop()

    return inverte_string
#exemplo de uso:

input_string = "saida"
resultado = inverte_string(input_string)
print(resultado)



'''def inverte_string(string):
    
    pilha = Pilha()

    for char in string:
        pilha.push(char)

    interte_string = " "
    while not pilha.is_empty():
        inverte_string += Pilha.pop()
    
    return inverte_string'''
