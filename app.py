print("Olá bem vindo ao sistema de pesquisas da TudoWeb!")

excelente = 0
ruim = 0

for i in range (50):
    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))
    opinião = int(input('Digite sua opinião: \n1 - EXCELENTE \n2 - BOM  \n3 - RUIM\n '))
    if opinião == 1:
        excelente = excelente + 1
    elif opinião == 3:
        ruim = ruim + 1

print("Quantidade de respostas EXCELENTE:", excelente )
print("Quantidade de respostas RUIM:", ruim )