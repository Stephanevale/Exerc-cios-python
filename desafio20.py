salario = float(input('Qual o valor do salário: '))

base = salario
aumento = 0

if base > 1250:
    aumento = aumento + (base) * 0.10
    print('O aumento será de: R$%5.2f' % (aumento + base))

if base < 1250:
    aumento = aumento + (base) * 0.15
    print('O aumento será de: R$%5.2f' % (aumento + base))
