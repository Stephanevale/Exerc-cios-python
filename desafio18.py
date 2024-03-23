velocidade = float(input('Qual a velocidade do carro?:'))

if velocidade <= 80:
    print('Seu carro não foi multado')


if velocidade > 80:
    multa = (velocidade - 80) * 5
    print('Seu carro foi multado')
    print ('O valor a ser pago será: R$:{:.2f}'.format(multa))