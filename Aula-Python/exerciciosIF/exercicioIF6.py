num1 = float(input("Digite o primeiro número positivo: "))
num2 = float(input("Digite o segundo número positivo: "))

print("\nMENU")
print("1 - Média ponderada (pesos 2 e 3)")
print("2 - Quadrado da soma dos 2 números")
print("3 - Cubo do menor número")

opcao = int(input("Escolha uma opção: "))

if opcao == 1:
    media = (num1 * 2 + num2 * 3) / 5
    print("Média ponderada:", media)

elif opcao == 2:
    resultado = (num1 + num2) ** 2
    print("Quadrado da soma:", resultado)

elif opcao == 3:
    if num1 < num2:
        menor = num1
    else:
        menor = num2
    
    resultado = menor ** 3
    print("Cubo do menor número:", resultado)

else:
    print("Opção inválida")