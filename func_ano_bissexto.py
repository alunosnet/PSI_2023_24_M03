"""Função que devolve True ou False se o ano é bissexto ou não
"""
def ano_bissexto(ano):
    if (ano % 400 == 0) or (ano % 4 == 0 and ano % 100 != 0):
        return True
    else:
        return False
print(ano_bissexto(2000)) #bissexto
print(ano_bissexto(1600)) #bissexto
print(ano_bissexto(2016)) #bissexto
print(ano_bissexto(1900)) #não é
if ano_bissexto(2000)==True:
    print("Bissexto")
else:
    print("Não é bissexto")