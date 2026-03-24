altura_parede = float(input("Altura da parede: "))
largura_parede = float(input("Largura da parede: "))
altura_azulejo = float(input("Altura do azulejo: "))
largura_azulejo = float(input("Largura do azulejo: "))

area_parede = altura_parede * largura_parede
area_azulejo = altura_azulejo * largura_azulejo

quantidade = area_parede / area_azulejo

print(f"Área da parede: {area_parede:.2f}")
print(f"Área do azulejo: {area_azulejo:.2f}")
print(f"Quantidade de azulejos: {quantidade:.0f}")
