#Sabendo da existência da nova placa Mercosul, e que um sistema precisa saber qual o tipo da placa em questão,
#  faça um algoritmo que receba uma placa e imprima qual o padrão da placa informada e a versão correspondente
#  da mesma placa no outro padrão. Considerações: A placa informada, deverá ser validada, aceitando somente 
# letras maiúsculas de A a Z (sem acentos), números positivos e estar no formato AAA9999 ou AAA9A99. Caso a 
# placa informada não cumpra esses critérios, o algoritmo deverá imprimir “formato inválido”

import re

def placa_conversao(placa):
    padrao_brasil = r"^[A-Z]{3}[0-9]{4}$"
    padrao_mercosul = r"^[A-Z]{3}[0-9][A-Z0-9][0-9]{2}$"

    if len(placa) != 7 or (not re.fullmatch(padrao_mercosul, placa) and not re.fullmatch(padrao_brasil, placa)):
        return "formato invalido"
    
    dict_mercosul = {
        "0": "A", "1": "B", "2": "C", "3": "D", "4": "E",
        "5": "F", "6": "G", "7": "H", "8": "I", "9": "J"
    }
    dict_brasil = {
        "A": "0", "B": "1", "C": "2", "D": "3", "E": "4",
        "F": "5", "G": "6", "H": "7", "I": "8", "J": "9"
    }

    # conversao de brasil para mercosul
    if re.fullmatch(padrao_brasil, placa):
        placa = placa[:4] + dict_mercosul[placa[4]] + placa[5:]
        return placa

    # conversao de mercosul para brasil
    elif re.fullmatch(padrao_mercosul, placa):
        placa = placa[:4] + dict_brasil[placa[4]] + placa[5:]
        return placa
    

print(placa_conversao("ab12345"))
print(placa_conversao("AB125"))
print("padrão brasil -> mercosul: ",placa_conversao("ABC1234"))
print("padrão mercosul -> brasil: ",placa_conversao("ABC1C34"))
