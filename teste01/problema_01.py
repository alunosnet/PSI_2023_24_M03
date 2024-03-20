"""
01 - Faça um programa que use uma função que receba como parâmetro o tempo obtido numa prova
em segundos e retorne como valores de saída os minutos e segundos a que esse tempo
corresponde. No programa deve depois ser escrito como output o tempo no formato MM:SS. A
string deve ter sempre 5 caracteres
"""

def converter_tempo(segundos):
    # quantos minutos utilizando divisão inteira
    #minutos = segundos // 60
    minutos = int(segundos / 60)
    segundos_restantes = segundos % 60
    if minutos<10:
        tempo_devolver = "0"
    tempo_devolver += str(minutos) + ":"
    if segundos_restantes<10:
        tempo_devolver += "0"
    tempo_devolver += str(segundos_restantes)
    return tempo_devolver

def main():
    tempo = int(input("Quantos segundos?"))

    tempo_formatado = converter_tempo(tempo)

    print(tempo_formatado)

if __name__=="__main__":
    main()