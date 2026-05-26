op = int(input("Digite a opcao:\n 1- Calculo perimetro\n 2- Calculo area\n 3- Sair\n "))

match op:
    case 1:
        #exemplo 1 - leitura de dados e conversão de valores
        ladoA = float(input("Digite o lado A do retangulo: "))
        ladoB = float(input("Digite o lado B do retangulo: "))

        calculo = 2 * ladoA + 2 * ladoB
        #para converter o resultado com dois numeros decimais {:.2f}
        print(f"O resultado do perimetro é {calculo:.2f}")

    case 2:
        ladoA = float(input("Digite o lado A do retangulo: "))
        ladoB = float(input("Digite o lado B do retangulo: "))

        calculo = ladoA * ladoB
        print(f"O resultado da area é {calculo:.2f}")
    
    case 3:
        exit
    
    case _:
        print("Opcao invalida")
        