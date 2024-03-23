x = 1
soma = 0
deposito = float(input('Qual o valor do depósito?: '))
taxa = float(input('Qual o valor da taxa de juros?: '))
c = deposito * (taxa/100)
while x <=24:
    soma = soma + c
    x = x + 1
    print('o valor do juros ao mês é de: %5.2f' %(soma + deposito))
print('o valor da total é %5.2f' %soma)
