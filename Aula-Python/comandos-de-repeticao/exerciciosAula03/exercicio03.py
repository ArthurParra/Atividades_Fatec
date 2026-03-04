import os
os.system('cls')

print("**************** CÁLCULO DE GRANDEZAS ELÉTRICAS **********")
opc = int(input("\n 1 - Tensão (em Volt) \n 2 - Resistência (em Ohm) \n 3 - Corrente (em Ampére) \n 4 - Sair \n********************************************************* \n Escolha a opção desejada: "))

match opc:
    case 1:
        print("Você escolheu a opção Tensão (em Volt) \n")
        r = float(input("Informe o valor de R 'Resistência': \n"))
        i = float(input("Informe o valor de i 'Corrente' \n"))
        tensao = r * i
        print(f"O calculo de Tensão é igual a: {tensao}")
    case 2:
        print("Você escolheu a opção Resistência (em Ohm) \n")
        u = float(input("Informe o valor de U 'Tensão': \n"))
        i = float(input("Informe o valor de i 'Corrente' \n"))
        resist = u / i
        print(f"O calculo da Resistência é igual a: {resist}")
    case 3:
        print("Você escolheu a opção Corrente (em Ampére) \n")
        u = float(input("Informe o valor de U 'Tensão': \n"))
        r = float(input("Informe o valor de R 'Resistência': \n"))
        corrente = u / r
        print(f"O calculo da Corrente é igual a: {corrente}")
    case 4:
        exit
    case _:
        print("Operação Invalida!!")
