cigarros = float(input('Quantos cigarros fuma por dia?: '))
anos = float(input('Quantos anos é fumante?: '))

multiplicacao_ano = anos * 365
cigarro_por_dia = multiplicacao_ano * cigarros
operacao = cigarro_por_dia * 10
o1 = 24*60
v = operacao / o1
print('Perderá %2.f dias de vida' %v)

