# exemplo de estrutura condicional IF 
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

# comando IF - atente-se aos espaçamentos
if media >= 6.0:
    print(f"Aluno aprovado com {media:.2f} de média")
elif media > 5.0 and media < 6.0: # and é o mesmo que operador &&
    print(f"Aluno de exame com {media:.2f} de média")
else:
    print(f"Aluno reprovado com {media:.2f} de média")

# if = se | elif = se não, se | else = se não