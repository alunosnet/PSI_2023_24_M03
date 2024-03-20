# Número perfeito

def NumeroPerfeito(n):
    soma = 0
    for i in range(1, n):
        if n % i == 0:
            soma += i
    if soma==n:
        return True
    else:
        return False
    
print(NumeroPerfeito(28))
print(NumeroPerfeito(11))