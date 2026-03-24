preco = float(input("Digite o preço total: "))
codigo = int(input("Forma de pagamento (1-À vista, 2-Débito, 3-Crédito): "))

if codigo == 1:
    desconto = preco * 0.15
elif codigo == 2:
    desconto = preco * 0.10
elif codigo == 3:
    desconto = preco * 0.05
else:
    desconto = 0

final = preco - desconto

print(f"Valor da compra: R$ {preco:.2f}")
print(f"Valor final: R$ {final:.2f}")
