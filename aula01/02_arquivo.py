with open ("./arquivos/02_alunos.txt", "r") as file:
    linha = file.readline()
    while(linha):
        print(linha.strip())
        linha = file.readline()