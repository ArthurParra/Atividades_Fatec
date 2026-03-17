altura = float(input("Informe sua altura: "))
sexo = input("Informe seu sexo: \n M - Masculino F - Feminino")

if sexo.upper() == "M":
    peso = (72.7*altura)-58
    print(f"Seu sexo é masculino, peso ideal é: {peso:.2f}")
else:
    if sexo.upper() == "F":
        peso = (62.1*altura)-44.7
        print(f"Seu sexo é feminino, peso ideal é: {peso:.2f}")
    else: 
        print("operação invalida meu campeão, tenta denovo.")