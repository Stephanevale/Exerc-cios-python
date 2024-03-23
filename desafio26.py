kw = float(input('Qual a quantidade de kwh da energia consumida: '))
instalacao = input('Qual o tipo de instalação? (residencial(r)/ comercial(c)/ industrial(i)): ')

if instalacao == 'r':
    if kw <= 500:
        valor = kw * 0.4
    else:
        valor = kw * 0.65
elif instalacao == 'c':
    if kw <= 1000:
        valor = kw * 0.55
    else:
        valor = kw * 0.60
elif instalacao == 'i':
    if kw <= 5000:
        valor = kw * 0.55
    else:
        valor = kw * 0.60

print('O valor a ser pago será de R$%5.2f' %valor)


