# simular o levantamento de dinheiro
# cada levantamento custa 0.75
# só pode levantar multiplos de 5

def Levantamento(valor,saldo):
    if valor%5!=0:
        print("Transação cancelada")
        return saldo
    if saldo<valor+0.75:
        print("Transação cancelada")
        return saldo
    else:
        return saldo-valor-0.75
    
saldo=Levantamento(21,150)
print(saldo)