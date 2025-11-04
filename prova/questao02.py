import pandas as pd

series = pd.Series([12000, 17500, 14300, 16000, 19500], index = ["Luca Brasi","Peter Clemenza","Sal Tessio", "Tom Hagen", "Michael Corleone"])

total_arrecadado = series.sum()
print(f"Total arrecadado na semana: {total_arrecadado}")

media_receitas = series.mean()
print(f"Média das receitas: {media_receitas: .2f}")

maior_associonado_nome = series.idxmax()
print(f"Nome do maior associado: {maior_associonado_nome}")

series = series[series > media_receitas]
print(series)