d =float(input('Quantos dias: '))
h = float(input('Quantas horas: '))
m = float(input('Quantos minutos: '))
s = float(input('Quantos segundos: '))
calculo = d * 86400
calculo1 = h * 3600
calculo2 = m * 60
ss = (calculo + calculo1 + calculo2)
print('O valor tem {:5.2f} segundos'.format(ss))