#Exercício 7 – Soma dos elementos de uma matriz
#Usando a matriz do exercício anterior, calcule e exiba a soma de todos 
#os seus elementos usando laços for aninhados.

matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
soma = 0

for i in matriz:
    for j in i:
        soma += j

print(soma)