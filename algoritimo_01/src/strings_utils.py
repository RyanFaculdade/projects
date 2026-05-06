def analisar_string(texto: str): 
    return { 
       'tamanho': len(texto), 
        'primeiro': texto[0], 
        'ultimo': texto[-1], 
        'maiusculo': texto.upper(), 
        'minusculo': texto.lower()
 }

def inverter_string(texto: str):
    tamanho_texto_positvo = len(texto)
    tamanho_texto_negativo = (len(texto) * (-1)) - 1
    texto_invertido = []
    
    #for i in range(tamanho_texto_positvo):

    #    texto_invertido.append(tamanho_texto_negativo)
    #    tamanho_texto_negativo -= 1
    #print(texto_invertido)



if __name__ == '__main__':
    print('É uma lib')
