from Fila import Fila

'''def gerador_numeros_binarios(self):
    
    def __init__():
        
        n = int(input("Digite o valor de n: "))
        fila = Fila()
        fila.push('1')
        
        for i in range(n):'''
        
def gerar_numeros_binarios(n):
    fila = Fila()
    fila.push('1')

    for i in range(n):
        numero_binario = fila.pop()
        print(numero_binario)

        fila.push(numero_binario + '0')
        fila.push(numero_binario + '1')

n = int(input("Digite o valor de n: "))
gerar_numeros_binarios(n)

            
                
                
        