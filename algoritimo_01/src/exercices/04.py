#Filtrando números ímpares
#Dada a lista valores = [8, 15, 22, 7, 30, 13, 18, 5, 27, 34], 
#use um laço for para criar uma nova lista contendo apenas os números ímpares. 
#Ao final, exiba a nova lista.

lista_numero = [8, 15, 22, 7, 30, 13, 18, 5, 27, 34, 3, 7]
lista_impares = []

for i in lista_numero:
    if i % 2 != 0:
        lista_impares.append(i)

print(lista_impares)
