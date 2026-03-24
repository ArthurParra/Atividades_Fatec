alt1 = float(input("Digite a altura da 1º pessoa: "))
alt2 = float(input("Digite a altura da 2º pessoa: "))
alt3 = float(input("Digite a altura da 3º pessoa: "))

if alt1 > alt2 and alt1 > alt3:
    maior = alt1
    if alt2 > alt3:
        mediana = alt2
        menor = alt3
    else:
        mediana = alt3
        menor = alt2
elif alt2 > alt1 and alt2 > alt3:
    maior = alt2
    if alt1 > alt3:
        mediana = alt1
        menor = alt3
    else:
        mediana = alt3
        menor = alt1
else:
    maior = alt3
    if alt1 > alt2:
        mediana = alt1
        menor = alt2
    else:
        mediana = alt2
        menor = alt1

print(f"A maior altura é: {maior}")
print(f"A media dentre as alturas é: {mediana}")
print(f"A menor altura é: {menor}")
print("Fim do programa :)")