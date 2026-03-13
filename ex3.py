# Faça um algoritmo que receba um valor inteiro. 
# Dado o valor, calcule o menor número de notas (cédulas) 
# possíveis no qual o valor pode ser decomposto. 
# As notas consideradas são de 200, 100, 50, 20, 10, 5, 2 e 1. 
# A seguir mostre o valor lido e a relação de notas necessárias. 



def cedulas(valor):
    print("Valor:", valor)

    print("%d nota(s) de R$200,00" % (valor // 200))
    valor = valor % 200

    print("%d nota(s) de R$100,00" % (valor // 100))
    valor = valor % 100

    print("%d nota(s) de R$50,00" % (valor // 50))
    valor = valor % 50

    print("%d nota(s) de R$20,00" % (valor // 20))
    valor = valor % 20

    print("%d nota(s) de R$10,00" % (valor // 10))
    valor = valor % 10

    print("%d nota(s) de R$5,00" % (valor // 5))
    valor = valor % 5

    print("%d nota(s) de R$2,00" % (valor // 2))
    valor = valor % 2

    print("%d nota(s) de R$1,00" % (valor // 1))


cedulas(777)