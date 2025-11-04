with open("dados_alunos.txt", "r", encoding="utf-8") as file:
    linhas = file.readlines()

nomes = []
notas = []

for linha in linhas:
    linha = linha.strip()
    if linha:
        nome, curso, nota = linha.split("#")
        nomes.append(nome)
        notas.append(float(nota))

media = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

indice_maior = notas.index(maior_nota)
indice_menor = notas.index(menor_nota)

print(f"Média da turma: {media:.2f}")
print(f"Maior nota: {maior_nota} ({nomes[indice_maior]})")
print(f"Menor nota: {menor_nota} ({nomes[indice_menor]})")