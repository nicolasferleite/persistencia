import pandas as pd

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [23,35,24,26],
    "Cidade": ["São Paulo", "Fortaleza", "Quixadá", "Cascavel"]
}

#nome_series = pd.Series(dados["Nome"]_
#print(nome_series)
#print(dados["Nome"])

df = pd.DataFrame(dados)
#print(df)

series = pd.Series(df["Idade"])
print(series)
print("maior", df["Idade"].max())