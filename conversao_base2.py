"""Programa que utiliza uma função para converte um nº de base 2 para base 10"""
def ConverterBase10(ValorBinario):
    soma = 0
    expoente = len(ValorBinario)-1
    for posicao in range(len(ValorBinario)):
        if ValorBinario[posicao]=="1":
            soma = soma + 2 ** expoente
        expoente = expoente - 1
    return soma

base10=ConverterBase10("1011")
print(base10)