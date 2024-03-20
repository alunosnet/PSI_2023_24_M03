def gerar_pares(limite):
    n = 0
    while n<=limite:
        yield n
        n += 2

def range_pt(limite,inicio=0,passo=1):
    n=inicio
    while n < limite:
        yield n
        n += passo


#for numero_par in gerar_pares(10):
#    print(numero_par)

for n in range_pt(10,2,2):
    print(n)