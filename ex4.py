# Considerando a expressão: AX + BX + C = 1 .
# Faça um algoritmo que receba 3 valores inteiros A, B, e C e calcule o valor de X . 
# Dados os valores caso A e B possuam valor 0 e C seja diferente de 1 imprimir “solução impossível”.

def calcule_x(A, B, C):
    if A == 0 and B == 0 and C != 1:
        print("solução impossível")
    else:
        x = (1 - C) / (A + B)
        print("O valor de x é: ", x)


calcule_x(10, 5, -14)
calcule_x(0, 0, 20)