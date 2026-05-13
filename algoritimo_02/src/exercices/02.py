#Faça uma cópia rasa usando .copy() e uma cópia profunda usando copy.deepcopy()
#Modifique: copia_rasa[0][0] = 99
#Exiba:
#matriz original
#cópia rasa
#cópia profunda
#Responda: O que aconteceu com a matriz original? Por quê?

import copy

matriz = [[1, 2], [3, 4]]
print(f'Matriz antes das copias{matriz}')

copia_rasa_matriz = matriz.copy()
copia_rasa_matriz[0][0] = 99

#copia_profunda_matriz = copy.deepcopy(matriz)
#copia_profunda_matriz[0][0] = 99


print(f'Matriz Original: {matriz}')
print(f'Copia rasa: {copia_rasa_matriz}')
#print(f'Copia profunda: {copia_profunda_matriz}')

# na copia profunda ele n mexe no original
# na copia rasa ele mexe na original

print('Resposta: Quando eu usei a funcao de copia rasa, ele mudou tambem a matriz original')
print('Mas quando copiei usando o metodo copia profundo, ele nao mexeu no original')
print('Por que a copia rasa usa os indicadores mutaveis da original')
print('Ja a copia profunda, copia TUDO de forma independente')