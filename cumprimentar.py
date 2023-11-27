def cumprimentar():
    print("Bom dia")

def cumprimentarv2():
    nome = input("Qual o seu nome?")
    print(f"Bom dia {nome}")

def cumprimentarv3(nome):
    print(f"Bom dia {nome}")

def main():
    nome = input("Qual o seu nome?")
    cumprimentarv3(nome)
    print(nome)

if __name__=="__main__":
    main()