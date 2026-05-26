#EXEMPLO UTILIZANDO COMANDO IF

qnt = int(input("Digite a quantidade de um produto:"))
valor = float(input("Digite o preco do produto: "))

if qnt > 10:
    valortotal = (valor * qnt) -10
    print(f"O desconto é de R$10, o valor a pagar é de R${valortotal:.2f}")
elif qnt == 10:
    valortotal = valor * qnt
    print(f"Nao ha desconto, o valor a pagar é {valortotal:.2f}")
else:
    valortotal = (valor * qnt) -5
    print(f"O desconto é de R$5, o valor a pagar é de R${valortotal:.2f}")

