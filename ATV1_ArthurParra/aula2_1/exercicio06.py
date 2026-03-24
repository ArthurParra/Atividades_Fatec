peso = float(input("Digite o peso na Terra: "))
planeta = int(input("Digite o número do planeta (1-5): "))

if planeta == 1:
    gravidade = 0.37
elif planeta == 2:
    gravidade = 0.88
elif planeta == 3:
    gravidade = 0.38
elif planeta == 4:
    gravidade = 2.64
elif planeta == 5:
    gravidade = 1.15
else:
    gravidade = 1

peso_planeta = peso * gravidade

print(f"Peso na Terra: {peso:.2f}")
print(f"Peso no planeta: {peso_planeta:.2f}")