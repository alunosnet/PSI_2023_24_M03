# Problema da reciclagem
def PontosAtribuidos(papel,plastico,vidro,pilhas):
    pontos = papel * 0.75
    pontos += plastico * 0.50
    pontos += vidro * 0.25
    pontos += pilhas
    return pontos

print("João:")
j_papel=int(input("Papel:"))
j_plastico=int(input("Plastico:"))
j_vidro=int(input("Vidro:"))
j_pilhas=int(input("Pilhas:"))

print("Joana:")
j2_papel=int(input("Papel:"))
j2_plastico=int(input("Plastico:"))
j2_vidro=int(input("Vidro:"))
j2_pilhas=int(input("Pilhas:"))

pontos_joao=PontosAtribuidos(j_papel,j_plastico,j_vidro,j_pilhas)
pontos_joana=PontosAtribuidos(j2_papel,j2_plastico,j2_vidro,j2_pilhas)

print("Pontos joão:",pontos_joao)
print("Pontos joana:",pontos_joana)

if pontos_joao>pontos_joana:
    print("João")
elif pontos_joao<pontos_joana:
    print("Joana")
else:
    if j_plastico>j2_plastico:
        print("João")
    elif j2_plastico>j_plastico:
        print("Joana")
    else:
        if j_vidro>j2_vidro:
            print("João")
        elif j2_vidro>j_vidro:
            print("Joana")
        else:
            if j_papel>j2_papel:
                print("João")
            elif j2_papel>j_papel:
                print("Joana")
            else:
                if j_pilhas>j2_pilhas:
                    print("João")
                elif j2_pilhas>j_pilhas:
                    print("Joana")
                else:
                    print("Empate")
