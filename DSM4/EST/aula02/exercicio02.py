import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "Headset"],
    "Categoria": ["Periferico", "Periferico", "Video", "Video", "Audio"],
    "Preço": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

df = pd.DataFrame(dados)

df["Val_total"] = df["Preço"] * df["Quantidade"]

#qual produto possui o maior valor em estoque?
print(df.iloc[df["Val_total"].idxmax()])

#qual possui o menor valor em estoque?
print(df.iloc[df["Val_total"].idxmin()])

#qual é o valor total de todo o estoque?

print(df["Val_total"])