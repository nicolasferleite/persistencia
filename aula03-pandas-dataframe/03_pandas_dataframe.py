import pandas as pd

alunos_df = pd.read_csv("./arquivos/alunos.csv")

# criar uma nova coluna

def situacao_aluno(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota < 4:
        return "Reprovado"
    else:
        return "Recuperação"
    
alunos_df["Situação"] = alunos_df["Nota"].apply(situacao_aluno)
print(alunos_df)

