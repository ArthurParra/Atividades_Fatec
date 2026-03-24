preco = float(input("Preço do pão: R$ "))

for i in range(1, 51):
    if i % 2 == 0:
        total = i * preco
        print(f"{i} - R$ {total:.2f}")
