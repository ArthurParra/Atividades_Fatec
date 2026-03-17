num1 = float(input("Digite um numero: "))
num2 = float(input("Digite o segundo numero: "))


if num1 == num2:
    print("Os números são iguais.")
else:
    print("Operação invalida")
    if num1 > num2:
        divis = num1 / num2
        print(f"O resultado da divisão entre {num1} e {num2} é = {divis:.2f}")
    else:
        divis = num2 / num1
        print(f"O resultado da divisão entre {num2} e {num1} é = {divis:.2f}")

    