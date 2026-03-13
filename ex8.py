# Elabore um algoritmo que construa uma matriz quadrada de tamanho N em formato de caracol. 

import numpy as np

def caracol(n):
    matriz = np.zeros((n, n))

    num = n        

    topo = 0
    baixo = n - 1
    esquerda = 0
    direita = n - 1

    while topo <= baixo and esquerda <= direita:
        for i in range(esquerda, direita + 1):
            matriz[topo][i] = num
            num += n
        topo += 1

       
        for i in range(topo, baixo + 1):
            matriz[i][direita] = num
            num += n
        direita -= 1

        for i in range(direita, esquerda - 1, -1):
            matriz[baixo][i] = num
            num += n
        baixo -= 1

        for i in range(baixo, topo - 1, -1):
            matriz[i][esquerda] = num
            num += n
        esquerda += 1

    print(matriz)

caracol(5)
caracol(2)
caracol(10)