def fatorial(numero):
    if numero == 1:
        return 1
    
    return numero * fatorial(numero-1)

def fatorial_for(numero):
    resultado = 1

    for i in range(1, numero + 1):
        resultado = resultado * i

    return resultado