# Escreva um programa que faça a impressão de um título formatado e centralizado. 
# O sistema vai receber o título desejado, separado em 2 partes, sendo uma superior
#  e outra inferior e deve devolver um título formato e centralizado

def quadro(parte1, parte2):
    largura_texto = max(len(parte1), len(parte2))
    largura_total = largura_texto + 8    #texto de maior tamanho + bordas
    
    print("|" * largura_total)
    print("||" + " " * (largura_total - 4) + "||")     
    print("||" + parte1.center(largura_total - 4) + "||")
    print("||" + parte2.center(largura_total - 4) + "||")
    print("||" + " " * (largura_total - 4) + "||")
    print("|" * largura_total)


quadro("DSIN", "TECNOLOGIA DA INFORMAÇÃO")
quadro("Python", "Algoritmos e Estruturas de Dados")
quadro("Evelyn", "Suzarte Fernandes")