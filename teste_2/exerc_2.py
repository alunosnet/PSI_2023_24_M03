"""
Resolução do teste de recuperação do Módulo 03
Exercício 02
"""
def Calcula_Media(CC,CP,CCR):
    return CC * 0.3 + CP * 0.4 + CCR * 0.3

def Verificar(nota):
    if nota>=10:
        return "Aluno aprovado"
    return "Aluno reprovado"

def main():
    cc = int(input("Nota CC: "))
    cp = int(input("Nota CP: "))
    ccr = int(input("Nota CCR: "))
    nota = Calcula_Media(cc,cp,ccr)
    print(f"Média: {nota}")
    print(Verificar(nota))

if __name__=='__main__':
    main()