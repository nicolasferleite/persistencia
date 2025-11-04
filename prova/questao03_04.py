from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

alunos_df = pd.DataFrame(columns=["id", "nome", "nota"])
ultimo_id = 0

class Aluno(BaseModel):
    nome: str
    nota: float
    
# pega todos os alunos
@app.get("/alunos")
def listar_alunos():
    return alunos_df.to_dict(orient="records")

# pega um aluno específico, pelo seu id
@app.get("/alunos/{id}")
def obter_aluno(id: int):
    aluno = alunos_df[alunos_df["id"] == id]
    if aluno.empty:
        raise HTTPException(status_code=404, detail="Aluno não encontrado")
    return aluno.to_dict(orient="records")[0]


@app.post("/alunos")
def cadastrar_ou_atualizar_aluno(aluno: Aluno):
    global alunos_df, ultimo_id

    # verifica se o aluno já existe pelo nome
    existe = alunos_df["nome"].str.lower().eq(aluno.nome.lower()).any()

    if existe:
        # atualiza nota do aluno existente
        alunos_df.loc[
            alunos_df["nome"].str.lower() == aluno.nome.lower(), "nota"
        ] = aluno.nota
        aluno_atualizado = alunos_df[
            alunos_df["nome"].str.lower() == aluno.nome.lower()
        ].to_dict(orient="records")[0]
        return {"mensagem": "Aluno atualizado com sucesso", "dados": aluno_atualizado}

    else:
        # cria novo aluno
        ultimo_id += 1
        novo_aluno = {"id": ultimo_id, "nome": aluno.nome, "nota": aluno.nota}
        alunos_df = pd.concat([alunos_df, pd.DataFrame([novo_aluno])], ignore_index=True)
        return {"mensagem": "Aluno cadastrado com sucesso", "dados": novo_aluno}