categoria = input("Digite a categoria (A/B/C): ").upper()
salario = float(input("Digite o salário: "))

if categoria == "A":
    aumento = salario * 0.10
elif categoria == "B":
    aumento = salario * 0.15
elif categoria == "C":
    aumento = salario * 0.25
else:
    aumento = 0

novo_salario = salario + aumento

print(f"Salário atual: R$ {salario:.2f}")
print(f"Salário com aumento: R$ {novo_salario:.2f}")
