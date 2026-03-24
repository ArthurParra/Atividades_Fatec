produto = input("Descrição do produto: ")
quantidade = int(input("Quantidade: "))
preco = float(input("Preço unitário: "))

total = quantidade * preco

print(f"Produto: {produto}")
print(f"Total: {total:.2f}")
