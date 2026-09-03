import pandas as pd
import matplotlib.pyplot as plt

dados = {
    "Produto": ["Switch2", "XBOX-One", "PlayStation5"],
    "Preço" : ["4499.00", "1000.00", "4599.90"],
    "Quantidade": [5, 10, 7]
}

df = pd.DataFrame(dados)

plt.plot(
    df["Preço"], df["Quantidade"],
    
    color= "#36013F"
)

plt.title("Preço x Quantidade")
plt.xlabel("Preço")
plt.ylabel("Quantidade")

plt.show()

