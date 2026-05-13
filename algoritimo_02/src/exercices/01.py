#Parte 1 — Matrizes
#Crie uma matriz 3x3 contendo números inteiros digitados pelo usuário.
#Requisitos:Utilize listas aninhadas. Use a criação correta com list comprehension.
#Exiba:
#a matriz completa;
#a soma de cada linha;
#a soma da diagonal principal.

matriz = [[0 for _ in range(3)] for _ in range(3)]

for i in range(3):              #linha
    for j in range(3):          #coluna
        matriz[i][j] = int(input())

for i in matriz: # Printa a matriz de forma mais bonita
    print(i)

soma = 0

for linha in matriz:
    for i in linha:
        soma += i
    print(f'soma da linha {linha} = {soma}')
    soma = 0

soma_diagonal = 0
for i in range(3):
    soma_diagonal += matriz[i][i]
print(soma_diagonal)
