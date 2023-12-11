"""9. Crie uma função que conte o número de vogais em uma string."""
import sys

def Vogais(palavra):

    #percorrer pelas posições das letras
    #for posicao in range(len(palavra)):
    #    if palavra[posicao] in "aeiouAEIOU":
    contar = 0
    for letra in palavra:
        if letra in "aeiouAEIOU":
            contar = contar + 1
    print(contar)

def main():
    if len(sys.argv)!=2:
        palavra=input("Insira uma palavra:")
    else:
        palavra=sys.argv[1]

    Vogais(palavra)

if __name__=="__main__":
    main()