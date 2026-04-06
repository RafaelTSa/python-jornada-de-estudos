media = float(input("Média do aluno: "))

if media >= 7.0:
    print("Passou direto!")
elif (media >= 4.0) and (media < 7.0):
    print("Recuperação.")
else:
    print("Reprovou direto.")