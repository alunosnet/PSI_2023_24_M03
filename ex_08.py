"""8. Desenvolva uma função que encontre o máximo divisor comum (MDC) entre dois números"""
def MDC(n1,n2):
    if n1<n2:
        menor=n1
    else:
        menor=n2
    for i in range(menor,0,-1):
        if n1 % i ==0 and n2 % i ==0:
            print(i)
            return


