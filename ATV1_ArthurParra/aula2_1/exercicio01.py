import os
os.system('cls')

letra = input("Digite UMA unica letra: ").upper()

match letra:
    case "A" | "E" | "I" | "O" | "U":
        print("É uma vogal.")
    case "B" | "C" | "D" | "F" | "G" | "H" | "J" | "K" | "L" | "M" | "N" | "P" | "Q" | "R" | "S" | "T" | "V" | "W" | "X" | "Y" | "Z":
        print("É uma consoante.")
    case _:
        print("Não é uma letra válida.")

