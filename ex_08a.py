import ex_08
import sys

#Ler os valores dos parâmetros da linha de comandos
if len(sys.argv)!=3:
    print("Erro! Tem de indicar 2 valores. Por exemplo: python ex_08a.py 10 5")
    sys.exit()

n1 = int(sys.argv[1])
n2 = int(sys.argv[2])

#calcular e mostrar o MDC
ex_08.MDC(n1,n2)