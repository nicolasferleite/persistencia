import httpx

BASE_URL = "http://127.0.0.1:8000"

def cadastrar_produto(produto):
    resp = httpx.post(
        f"{BASE_URL}/produtos",
        json = {"nome":produto.get("nome"),"categoria":produto.get("categoria"),"preco":produto.get("preco")}
    )
    return resp

def listar_produtos():
    resp = httpx.get(f"{BASE_URL}/produtos")
    print(resp.json())

def obter_produto(id):
    resp = httpx.get(f"{BASE_URL}/produtos/{id}")
    return resp.json()

def atualizar_produto(id, produto):
    resp = httpx.put(
        f"{BASE_URL}/produtos/{id}",
        json = {"nome":produto.get("nome"),"categoria":produto.get("categoria"),"preco":produto.get("preco")}
    )
    print(resp.json())

def apagar_produto(id):
    resp = httpx.delete(f"{BASE_URL}/produtos/{id}")
    return resp.json()