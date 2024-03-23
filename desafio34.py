pontos = 0
questao = 1
while questao <=3:
    resposta = input('Resposta da questão %d: ' %questao)
    if questao == 1 and resposta == "a" or "A":
        pontos = pontos + 1
    if questao == 2 and resposta == "b" or "B":
        pontos = pontos +1
    if questao == 3 and resposta == 'd' or 'D':
        pontos = pontos +1
        questao +=1
    print('O aluno fez %d ponto(s)'%pontos)