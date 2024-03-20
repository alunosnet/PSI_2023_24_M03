"""
Resolução do teste de recuperação do Módulo 03
Exercício 01
"""
def Calcular_Preco(preco,divisa):
    #converter para a nova divisa
    #Brasil
    if divisa=='r' or divisa=='R':
        novo_preco = preco * 4.05
        novo_preco = novo_preco * 1.1
    elif divisa=='D' or divisa=='d':
        novo_preco = preco * 1.23
        novo_preco = novo_preco * 1.1
    elif divisa=='l' or divisa=='L':
        novo_preco = preco * 0.89
    else:
        novo_preco = preco * 4.67
    
    return f"{novo_preco:.2f}"

def NomeMoeda(divisa):
    if divisa=='r' or divisa=='R':
        return "Reais [Brasil]"
    elif divisa=='d' or divisa=='D':
        return "Dólares [EUA]"
    elif divisa=='l' or divisa=='L':
        return 'Libras Esterlinas [UK]'
    else:
        return 'Liras Turcas [Turquia]'

def MostraTaxas():
    print("Brasil - 4,05 Reais")
    print("EUA - 1,23 Dólares")
    print("UK - 0,89 Libras Esterlinas")
    print("Turquia - 4,67 Liras Turcas")

def main():
    op=input("Consultar Taxas (S/N)? ")
    if op=='s' or op=='S':
        MostraTaxas()
    preco = float(input("Preço em euros: "))
    divisa = input("Divisa (R,D,L,T)? ")
    mensagem = Calcular_Preco(preco,divisa) + " " + NomeMoeda(divisa)
    print(mensagem)

if __name__=="__main__":
    main()