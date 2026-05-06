#Contando vogais em uma frase
#Escreva um programa que leia uma frase do usuário e use um laço for 
#para contar quantas vogais (a, e, i, o, u) ela possui, desconsiderando diferenças
#entre maiúsculas e minúsculas.

print('Digite uma frase para verificar numero de vogais')
frase = input()
numero_vogal = 0

for i in frase.lower():
    if i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u':
        numero_vogal += 1

if numero_vogal < 0:
    print('Erro, a frase tem numero de vogais negativas')
elif numero_vogal == 1:
    print(f'A frase tem {numero_vogal} vogal')
else: 
    print(f'A frase tem {numero_vogal} vogais')