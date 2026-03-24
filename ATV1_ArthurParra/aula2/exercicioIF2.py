num = int(input("Digite um numero inteiro positivo: "))

if num %2 ==0:
    quadrado = num**2
    print(f"O número {num} é Par.")
    print(f"O quadrado de {num} é {quadrado}")
else:
    cubo = num**3
    print(f"O número {num} é Impar.")
    print(f"O cubo de {num} é {cubo}")
    