import pandas as pd

dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "WebCam", "Headset"],
    "Categoria": ["Periferico", "Periferico", "Video", "Video", "Audio"],
    "Preço": [80, 120, 900, 250, 300],
    "Quantidade": [10, 8, 4, 6, 5]
}

# # Criar Dataframe
df = pd.DataFrame(dados)

# #exibir dataframe
print(df)

# #exibir shape
print(df.shape)

# #exibir info
print(df.info())

# #exibir describe
print(df.describe())

# #selecionar apenas Produto e Preço
print(df[["Produto", "Preço"]])

# #selecionar os dois primeiros produtos
print(df.iloc[0:2])

# #encontrar o produto mais caro
print(df.iloc[df["Preço"].idxmax()])

print(df["Preço"].idxmax)
