"""
02 - Faça um programa em Python que use uma função para determinar o signo a que uma pessoa
pertence. A função deve receber como parâmetros 2 valores inteiros correspondentes ao dia e ao
mês da data de nascimento do utilizador. Deve depois devolver o nome do signo correspondente
para o programa. Preveja a hipótese de a pessoa ter dado valores incorretos para a sua data de
nascimento. Nesse caso a função deve retornar uma mensagem de erro com o texto “data
incorreta)"""

def signo(dia, mes):
    if (mes == 3 and dia >= 21) or (mes == 4 and dia <= 19):
        return "Áries"
    elif (mes == 4 and dia >= 20) or (mes == 5 and dia <= 20):
        return "Touro"
    elif (mes == 5 and dia >= 21) or (mes == 6 and dia <= 20):
        return "Gémeos"
    elif (mes == 6 and dia >= 21) or (mes == 7 and dia <= 22):
        return "Câncer"
    elif (mes == 7 and dia >= 23) or (mes == 8 and dia <= 22):
        return "Leão"
    elif (mes == 8 and dia >= 23) or (mes == 9 and dia <= 22):
        return "Virgem"
    elif (mes == 9 and dia >= 23) or (mes == 10 and dia <= 22):
        return "Libra"
    elif (mes == 10 and dia >= 23) or (mes == 11 and dia <= 21):
        return "Escorpião"
    elif (mes == 11 and dia >= 22) or (mes == 12 and dia <= 21):
        return "Sagitário"
    elif (mes == 12 and dia >= 22) or (mes == 1 and dia <= 19):
        return "Capricórnio"
    elif (mes == 1 and dia >= 20) or (mes == 2 and dia <= 18):
        return "Aquário"
    elif (mes == 2 and dia >= 19) or (mes == 3 and dia <= 20):
        return "Peixes"
    else:
        return "data incorreta"

def main():
    dia = int(input("Digite o dia de nascimento: "))
    mes = int(input("Digite o mês de nascimento: "))

    print(signo(dia, mes))


if __name__ == "__main__":
    main()