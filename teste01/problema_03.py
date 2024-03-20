"""
03 - Faz um programa que use uma função para imprimir o valor acumulado anualmente num depósito
a prazo. A função deve receber como parâmetros o valor a depositar, a taxa de juro anual líquida
(TANL) e o número de anos que vai manter o deposito. Deve depois imprimir os valores que são
capitalizados anualmente, ano a ano. No final a função deve devolver o valor ganho no deposito
para fazer o output no programa."""

def deposito(valor, tanl, anos):
    total_juros = 0
    saldo_atual = valor

    for ano in range(1, anos + 1):
        juros = saldo_atual * (tanl / 100)
        saldo_atual += juros
        total_juros += juros
        print(f"Ano {ano}: Valor acumulado = {saldo_atual:.2f}")

    return total_juros

def main():
    valor_depositado = float(input("Digite o valor a depositar: "))
    taxa_anual = float(input("Digite a taxa de juro anual líquida (TANL) em %: "))
    num_anos = int(input("Digite o número de anos do depósito: "))

    juros_ganhos = deposito(valor_depositado, taxa_anual, num_anos)
    print(f"Ganhou: {juros_ganhos:.2f}")

if __name__ == "__main__":
    main()
