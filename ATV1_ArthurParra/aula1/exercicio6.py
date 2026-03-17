sal_mes = float(input("Informe seu salário mensal: "))
porc = float(input("Informe a porcentagem de aumento: "))

novo_sal = (sal_mes*porc)/100 + sal_mes

print(f"Seu aumento de salário foi de: {novo_sal:.2f}")