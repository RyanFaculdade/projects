#Tabuada completa com validação
#Solicite um número inteiro positivo ao usuário. 
#Caso ele digite um número negativo, peça novamente até que seja válido. 
#Em seguida, exiba a tabuada desse número de 1 a 10 usando for.

while True:
    print('Digite um numero inteiro para ver a tabuada dele')
    numero = int(input())
    if numero > 0:
        break

print(f'A tabuada do {numero} é:')

for i in range(1, 10 + 1):
    print(f'{numero} x {i} = {numero  * i}')