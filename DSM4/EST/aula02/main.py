import pandas as pd
 
dados = {
    "Produto": ["Mouse", "Teclado", "Monitor", "Gabinete"],
    "Preço": [80, 50, 800, 250],
    "Quantidade": [10, 50, 15, 25]
}
 
df = pd.DataFrame(dados)
 
df["Valor_total"] = df["Preço"] * df["Quantidade"]
 
print(df.sort_values("Valor_total"))
print(df[df["Quantidade"]<20])
print(df[[df["Quantidade"]<20 & df["Preço"]<300]])
 
import pandas as pd
df = pd.read_csv("dados.csv")
print(df)