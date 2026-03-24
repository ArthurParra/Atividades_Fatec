total = 0

while True:
    preco = float(input("Preço da mercadoria (0 para sair): R$ "))
    
    if preco == 0:
        break
    
    total += preco

print(f"Total da compra: R$ {total:.2f}")

dinheiro = float(input("Valor em dinheiro: R$ "))

troco = dinheiro - total

if troco >= 0:
    print(f"Troco: R$ {troco:.2f}")
else:
    print(f"Falta: R$ {abs(troco):.2f}")
