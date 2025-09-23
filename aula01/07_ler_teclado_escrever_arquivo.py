import sys

linha = sys.stdin.readline()

while linha != "exit":
    with open ("./arquivos/07_saida3.txt", "a", encoding="utf-8") as file:
        file.write(linha)
    linha = sys.stdin.readline()