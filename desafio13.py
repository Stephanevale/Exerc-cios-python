m = float(input('Qual o valor da mercadoria?: '))
d = float(input('Qual o valor do desconto?: '))
o = (m - d) / 100
print('O valor do desconto será de: %5.2f reais' %o)
print('O valor a ser pago será de: %5.2f reais' %(m - o))