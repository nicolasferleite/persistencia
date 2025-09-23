import pandas as pd

alunos_df = pd.read_csv("./arquivos/alunos.csv")

nota_maxima = alunos_df["Nota"].max()
print("Nota máxima: ", nota_maxima)

# como pegar as caracteristicas do aluno que tem a nota maxima

aluno_nota_maxima = alunos_df[alunos_df["Nota"] == nota_maxima]
print(aluno_nota_maxima["Nome"])

media_notas = round(alunos_df["Nota"].mean(),2)
print(media_notas)

# pessoas que estao acima da media
print(alunos_df[alunos_df["Nota"] > media_notas])