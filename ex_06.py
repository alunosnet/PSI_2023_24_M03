"""6. Faça uma função que calcule a distância entre dois pontos no plano cartesiano."""
import math

def DistanciaDoisPontos(x1,y1,x2,y2):
    cateto1 = x2 - x1
    cateto2 = y2 - y1
    distancia = math.sqrt(cateto1**2 + cateto2**2)
    print(distancia)

def main():
    DistanciaDoisPontos(x1=1,x2=2,y1=4,y2=6)

if __name__=="__main__":
    main()
