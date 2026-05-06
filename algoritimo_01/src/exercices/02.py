#Exercício 2 – Exibindo o dobro com validação
#Crie uma lista vazia. Peça ao usuário que digite 5 números inteiros e armazene-os na lista.
#Em seguida, use um laço for para exibir o dobro de cada número.

lista_numero = []

print('Digite 5 numeros para calcular o dobro de cada um deles')

i = 0
while i < 5:

    numero_digitado = int(input('Digite aqui:'))
    lista_numero.append(numero_digitado)
    i += 1

for i in lista_numero:
    print(f'O dobro de {i} é {i * 2}')


# .append adiciona um item ao final da lista
# o for no python funciona diferente do for em C, aonde i é o proprio valor da lista_numero
# (x, y, z, ..., n)
# e não no lugar aonde se encontra o valor (0, 1, 2, ..., n)