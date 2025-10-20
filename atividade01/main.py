from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

produtos_df = pd.DataFrame(columns=["id", "nome", "categoria", "preco"])
ultimo_id = 0

class Produto(BaseModel):
    nome: str
    categoria: str
    preco: float
    
@app.get("/produtos")
def listar_produtos():
    return produtos_df.to_dict(orient="records")

@app.get("/produtos/{id}")
def obter_produto(id: int):
    produto = produtos_df[produtos_df["id"] == id]
    if produto.empty:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    return produto.to_dict(orient="records")[0]

@app.post("/produtos")
def cadastrar_produto(produto: Produto):
    global ultimo_id, produtos_df
    ultimo_id += 1
    novo_produto = {
        "id": ultimo_id,
        "nome": produto.nome,
        "categoria": produto.categoria,
        "preco": produto.preco
    }
    produtos_df = pd.concat([produtos_df, pd.DataFrame([novo_produto])], ignore_index=True)
    return novo_produto

@app.put("/produtos/{id}")
def atualizar_produto(id: int, produto: Produto):
    global produtos_df
    if id not in produtos_df["id"].values:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    produtos_df.loc[produtos_df["id"] == id, ["nome", "categoria", "preco"]] = [
        produto.nome, produto.categoria, produto.preco
    ]
    return produtos_df[produtos_df["id"] == id].to_dict(orient="records")[0]

@app.delete("/produtos/{id}")
def apagar_produto(id: int):
    global produtos_df
    if id not in produtos_df["id"].values:
        raise HTTPException(status_code=404, detail="Produto não encontrado")
    indices_para_apagar = produtos_df[produtos_df["id"] == id].index
    produtos_df = produtos_df.drop(indices_para_apagar).reset_index(drop=True)
    return {"mensagem": "Produto removido com sucesso"}
