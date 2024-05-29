def eh_palindromo(s: str) -> bool:

    s = s.replace(" ", "").lower()

    def verifica_palindromo(inicio: int, fim: int) -> bool:
        # Caso base
        if inicio >= fim:
            return True
        if s[inicio] == s[fim]:
            return verifica_palindromo(inicio + 1, fim - 1)
        else:
            return False

    return verifica_palindromo(0, len(s) - 1)

string_usuario = input("Digite uma string para verificar se é um palíndromo: ")
resultado = eh_palindromo(string_usuario)
if resultado:
    print(f"{string_usuario} é um palíndromo.")
else:
    print(f"{string_usuario} não é um palíndromo.")
