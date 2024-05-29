def fatorial(n: int) -> int: #(n: int) -> int essa parte diz que n é um valor int e quero que
    #retorne um valor int tbm
    
    #caso base
    if n == 1:
        return 1
    #caso recursivo
    return n * fatorial(n - 1)

if __name__ == "__main__":
    fat5 = fatorial(5)
    print(fat5)