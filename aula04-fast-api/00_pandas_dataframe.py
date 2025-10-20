import pandas as pd

alunos_dic = {
    "Nome" : ("Nicolas"),
    "Idade" : ("20"),
    "IRA" : (8.0433)
}

alunos_df = pd.DataFrame({alunos_dic})
print(alunos_df)