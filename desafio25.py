valor_da_casa = float(input('Qual o valor da casa?: R$ '))
salario = float(input('Qual o valor do salário?: R$ '))
anos = float(input('Quantos anos será paga a casa?: '))
mensalidade = (valor_da_casa / (anos * 12))
porcentagem = (salario * 30) / 100

if mensalidade < porcentagem:
    print('Aprovado')
else:
    print('Não Aprovado')