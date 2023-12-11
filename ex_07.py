"""7. Implemente uma função que verifique se uma string é um palíndromo. """
def Palindromo(palavra):
    invertida=""
    for letra in palavra:
        invertida = letra + invertida
    invertida=invertida.lower()
    palavra=palavra.lower()
    if palavra==invertida:
        print("É palíndromo")
    else:
        print("Não é palíndromo")

Palindromo("Ana")
Palindromo("casa")