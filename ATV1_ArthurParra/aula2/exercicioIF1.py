nome1 = input("Informe o nome da primeira pessoa: ")
peso1 = float(input("Agora, informe o peso da primeira pessoa: "))
nome2 = input("Informe o nome da segunda pessoa: ")
peso2 = float(input("Agora, informe o peso da segunda pessoa: "))

if peso1 == peso2:
    print(f"{nome1} e {nome2} possuem o mesmo peso, que legal!")
else:
    if peso1 > peso2:
        print(f"{nome1} é mais pesado(a) que {nome2}, tendo {peso1:.2f}kg.")
    else:
        print(f"{nome2} é mais pesado(a) do que {nome1}, tendo {peso2:.2f}kg")