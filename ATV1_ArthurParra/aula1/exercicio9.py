votosbrancos = int(input("Votos brancos: "))
votosnulos = int(input("Votos nulos: "))
votosvalidos = int(input("Votos válidos: "))

totaleleitores = votosbrancos + votosnulos + votosvalidos

percbrancos = (votosbrancos * 100) / totaleleitores
percnulos = (votosnulos * 100) / totaleleitores
percvalidos = (votosvalidos * 100) / totaleleitores

print(f"Total: {totaleleitores}")
print(f"Brancos: {percbrancos:.2f}%")
print(f"Nulos: {percnulos:.2f}%")
print(f"Válidos: {percvalidos:.2f}%")
