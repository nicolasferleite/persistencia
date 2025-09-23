import pandas as pd

"""
Crie um DataFrame com os seguintes dados:

Nome	Idade	Cidade
Ana	    23	    São Paulo
Bruno	30	    Rio de Janeiro
Carlos	27	    Curitiba
Diana	22	    Belo Horizonte

- Exibir apenas a coluna "Nome"
- Exibir as colunas "Nome" e "Cidade"

"""

dados = {
    "Nome": ["Ana", "Bruno", "Carlos", "Diana"],
    "Idade": [23,30,27,22],
    "Cidade": ["São Paulo", "Rio de Janeiro", "Curitiba", "Belo Horizonte"]
}

df = pd.DataFrame(dados)

print(df["Nome"])
print(df[["Nome", "Cidade"]])