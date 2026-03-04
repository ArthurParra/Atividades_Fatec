num = float(input("DIgite o numero: "))
expoente = float(input("Digite o expoente: "))
#Potencia utilizando o operador

pot = num ** expoente
#Potencia utilizando a funcao math

pote = pow(num, expoente)#"pow" vem de Power

print(f"O resultado da potencia 'pot' é: {pot}")
print(f"O resultado da potencia 'pote' é: {pote}")