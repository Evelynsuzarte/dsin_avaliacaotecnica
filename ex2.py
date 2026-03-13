#Faça um algoritmo que receba 4 valores inteiros A, B, C e D. 
# Dados os valores, se B for maior do que C e se D for maior do que A,
#  e a soma de C com D for maior que a soma de A e B, e ainda, se ambos, 
# C e D forem positivos e A for par, escrever a mensagem "Valores aceitos", 
# se não escrever "Valores não aceitos"

def calculo_valores(A,B,C,D):
    if (B > C and D > A) and (C + D > A + B) and (C > 0 and D > 0) and (A%2 == 0):
        print ("Valores aceitos")
    else:
        print ("Valores não aceitos")

calculo_valores(2,6,4,8)
calculo_valores(3,6,4,8)