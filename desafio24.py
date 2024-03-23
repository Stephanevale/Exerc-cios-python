n1 = float(input('Digite um número: '))
n2 = float(input('Digite outro número: '))
operacao = input('Digite qual operação será realizada (+,-,* ou /): ')

if operacao == '+':
    print('A soma entre os números {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1+n2))
if operacao == '-':
    print('A subtração entre os números {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1 - n2))

if operacao == '*':
    print('A multiplicação entre os números {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1 * n2))
if operacao == '/':
    print('A divisão entre os números {:.0f} e {:.0f} é {:.0f}'.format(n1, n2, n1 / n2))
