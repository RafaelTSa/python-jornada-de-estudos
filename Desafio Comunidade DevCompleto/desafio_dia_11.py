# Desafio 21 dias - Comunidade dev completo
# Dia 11 - missão: 
# Explorar entrada e saída de dados.
# Criar um script que leia dados do usuário e mostre um relatório ou mensagem dinâmica.

print("-" *20)
print("Olá bem vindo!")
print("-" *20)

print("Qual é o seu nome?")
nome = input(">>> ")
print("Olá", nome,'!')
print("-" *20)
print("Tem interesse em tecnologia?")
tecnologia = input ("[S/N]").upper()
print("-" *20)
if tecnologia == "S":
    print("Qual área você quer seguir?")
    print("-" *20)
    print("Back-End [1]")
    print("Front-End [2]")
    print("Dados [3]")
    print("QA [4]")
    print("Fullstack [5]")
    print("-" *20)
    area = input(">>> ")
    print("-" *20)
    if area == "1":
        print("Seu futuro como Back-end pode estar aqui!")
    elif area == "2":
        print("Seu futuro como Front-end pode estar aqui!")
    elif area == "3":
        print("Seu futuro como Dados pode estar aqui!")
    elif area == "4":
        print("Seu futuro como QA pode estar aqui!")
    elif area == "5":
        print("Seu futuro como Fullstack pode estar aqui!")
elif tecnologia == "N":
    print("-" *60)
    print("Você ja ouviu falar sobre a comunidade Dev Completo?")
    print("-" *60)
    print("Sim [1]")
    print("Não [2]")
    print("-" *30)
    comunidade = input(">>> ")
    print("-" *30)
    if comunidade == "1":
        print("Tá esperando o que pra entrar?")
        print("-" *30)
    elif comunidade == "2":
        print("Serio? tá esperando o que?")
        print("-" *30)
