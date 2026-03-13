#Faça um algoritmo que calcule o salário líquido de um trabalhador em função da quantidade de horas por dia, 
#do preço da hora trabalhada e dos dias trabalhados no mês. Considerar um desconto de 3% sobre o salário bruto

def calculo_salario(qnt_horas, preco_horas, dias):
    salario_liquido = (qnt_horas*preco_horas) * dias
    salario_bruto = salario_liquido - ((3/100)*salario_liquido)
    return salario_bruto


qnt_horas = int(input("Digite a quantidade de horas trabalhadas: "))
preco_horas = float(input("Digite o preço da hora por dia: "))
dias = int(input("Digite os dias trabalhados no mês: "))

print("Seu salário liquido é de: %.2f" % calculo_salario(qnt_horas,preco_horas,dias))