km = float(input('Quantos km foram percorridos?: '))
d = int(input('Quantos dias o carro foi alugado?: '))

o = (0.15 * km) + (d * 60)

print('O valor a ser pago será: %5.2f reais' %(o))