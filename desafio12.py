salário = int(input('Digite o valor do salário: '))
aumento = int(input('Digite o valor do aumento em porcentagem: '))
s = (salário * aumento )/ 100
print('A quantidade de aumento será de: %5.2f reais' %(s))
print('O valor do salário atualizado será: %5.2f reais' %(s + salário))
