try:
  num = int(input('Digite um número: '))
  res = 10 / num
except ValueError:   # A função except ja tem valores pré-definidos 
  print('Erro: Entrada inválida!')
except ZeroDivisionError:
  print("Erro: Divisão por zero.")
except Exception:
  print("Erro inesperado.")

##-------------------------------

try:
  resultado = 10 / 0
except ZeroDivisionError as erro:
    # 'erro' contém a mensagem técnica
    print(f"Log técnico: {erro}")
    print("Ops! Algo deu errado.")
    
##-------------------------------

try:
    n = int(input("Número: "))
except ValueError:
    print("Erro de conversão.")
else:
    #Executa apenas se não houver erro
    dobro = n * 2
    print(f"Sucesso! O dobro é {dobro}")

##-------------------------------

##Execeções mais frequentes:
##    ValueError: Quando valor da variável está errado. 'abc' como inteiro ou 10.83 como inteiro.
##    TypeError: Quando uma operação é aplicada com objetivos incompativeis. string + inteiro
##    IndexError: Quando tenta acessar algo que está fora dos limites. Acessar o valor 50 de uma lista que so possui 10 valores
##    KeyError: Quando uma chave de dicionário não é encontrada.

##-------------------------------

while True:
    try:
        idade = int(input("Sua idade: "))
        if idade < 0:
            raise ValueError("Negativa")
    except ValueError:
        print("Entrada inválida!")
    else:
        print("Idade registrada.")
        break
    
-------------------------------
