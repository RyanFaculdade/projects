#Exercício 1 – Somando elementos de uma lista
#Dada a lista numeros = [10, 20, 30, 40, 50], 
#use um laço for para calcular e exibir a soma de todos os elementos.

lista_numero = [10, 20, 30, 40, 50]
soma = 0

for i in lista_numero:
    
    #print(i) Da certo
    #print(lista_numero[2]) Da certo
    #print(lista_numero[i]) Da **errado**
    # A var "i" em 0, tem o valor de 10, e o "i" em 1 tem o valor de 20, e nao de 1 como em C

    soma += i

print(soma)