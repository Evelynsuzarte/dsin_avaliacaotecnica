#  Construa um algoritmo que recebe um número inteiro positivo N e gere uma sequência de números inteiros positivos, 
# de 1 a N. O algoritmo deverá avaliar cada número dessa sequência da seguinte forma: ● Caso seja um número perfeito, 
# imprimir a mensagem “numero perfeito“; ● Caso seja um múltiplo de 3, imprimir “multiplo de 3”; ● Caso seja um múltiplo
#  de 5, imprimir “multiplo de 5”; ● Caso seja um número com a raiz quadrada inteira, imprimir “raiz inteira”

import math

def sequencia(n):
    if n < 0:
        print("Não é possível mostrar a sequência")
    else:
        for i in range(1, n):
            valido = False

            # verificar número perfeito
            soma_divisores = 0
            for j in range(1, i):
                if i % j == 0:
                    soma_divisores += j

            if soma_divisores == i:
                print(i, "- é um numero perfeito")
                valido = True

            # múltiplo de 3
            if i % 3 == 0:
                print(i, "- é um múltiplo de 3")
                valido = True

            # múltiplo de 5
            if i % 5 == 0:
                print(i, "- é um múltiplo de 5") 
                valido = True
            
            # raiz quadrada inteira
            if math.sqrt(i).is_integer():
                print(i, "- é raiz inteira")
                valido = True
            
            if valido == False :
                print (i, "- não entra em nenhuma condição")


sequencia(10)
sequencia(-1)