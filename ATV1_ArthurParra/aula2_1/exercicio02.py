indice = int(input("Digite o índice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Índice aceitável.")
    case 3 | 4 | 5:
        print("Suspender atividades do Grupo 1.")
    case 6 | 7:
        print("Suspender atividades do Grupo 1 e Grupo 2.")
    case 8 | 9 | 10:
        print("Suspender atividades de todos os grupos.")
    case _:
        print("Índice inválido.")