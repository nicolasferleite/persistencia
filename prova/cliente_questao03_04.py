import httpx

BASE_URL = "http://127.0.0.1:8000"

def listar_alunos():
    resp = httpx.get(f"{BASE_URL}/alunos")
    print(resp.json())

def obter_aluno(id):
    resp = httpx.get(f"{BASE_URL}/alunos/{id}")
    return resp.json()
    
def cadastrar_ou_atualizar_aluno(aluno):
    resp = httpx.post(
        f"{BASE_URL}/alunos",
        json={"nome": aluno.get("nome"), "nota": aluno.get("nota")}
    )
    print(resp.json())