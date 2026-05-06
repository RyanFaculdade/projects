def manipular_lista(lista): 
    lista.append("novo_item") 
    lista[0] = "alterado" 
    return lista 

def identificar_numero_na_lista(lista: list):
    tamanho_lista = len(lista)
    apenas_numeros = []

    for i in range(tamanho_lista):
        if type(lista[i]) is int:
            apenas_numeros.append(lista[i])
        
    print(apenas_numeros)


    
if __name__ == '__main__':
    print('É uma lib')
