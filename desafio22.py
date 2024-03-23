distancia = float(input('Quantos KM deseja percorrer?: '))

if distancia <= 200:
    print('O valor da passagem será de: R${:5.2f}'.format(distancia * 0.5))

else:
    print('O valor da passagem será de: R${:5.2f}'.format(distancia * 0.45))