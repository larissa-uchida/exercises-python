# Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, o programa deve perguntar ao aluno a resposta de cada questão e ao final comparar com o gabarito da prova e assim calcular o total de acertos e a nota (atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem respondido informar:
# Maior e Menor Acerto;
# Total de Alunos que utilizaram o sistema;
# A Média das Notas da Turma.
# Gabarito da Prova:

# 01 - A
# 02 - B
# 03 - C
# 04 - D
# 05 - E
# 06 - E
# 07 - D
# 08 - C
# 09 - B
# 10 - A
# Após concluir isto você poderia incrementar o programa permitindo que o professor digite o gabarito da prova antes dos alunos usarem o programa.

def verifica_nota():
    print('---------------------------------------------------- \n      Digite a resposta de acordo com a questão. \n----------------------------------------------------')
    inicio = 1
    acertos = 0
    lista = []
    outro = 'sim'
    usuario = input('Usuário Atual: Professor ou Aluno? ')
    primeira_questao = 'a'
    segunda_questao = 'b' 
    terceira_questao = 'c' 
    quarta_questao = 'd' 
    quinta_questao = 'e' 
    sexta_questao = 'e'
    setima_questao = 'd' 
    oitava_questao = 'c' 
    nona_questao = 'b' 
    decima_questao = 'a'
    if usuario in 'professor, Professor':
        gabarito = input('Deseja atribuir novas respostas ao gabarito (Sim ou Não)? ')
        if gabarito in 'sim, Sim':
            primeira_questao = input('Questão 01: ')
            segunda_questao = input('Questão 02: ')
            terceira_questao = input('Questão 03: ')
            quarta_questao = input('Questão 04: ')
            quinta_questao = input('Questão 05: ')
            sexta_questao = input('Questão 06: ')
            setima_questao = input('Questão 07: ')
            oitava_questao = input('Questão 08: ')
            nona_questao = input('Questão 09: ')
            decima_questao = input('Questão 10: ')
        
    while outro == 'sim' or outro == 'Sim':
        primeira = input('Questão 01: ')
        while primeira != 'a' and primeira != 'b' and primeira != 'c' and primeira != 'd' and primeira != 'e':
            primeira = input('Resposta Inválida. Digite novamente: ')
        if primeira == primeira_questao:
            acertos += 1
        segunda = input('Questão 02: ')
        while segunda != 'a' and segunda != 'b' and segunda != 'c' and segunda != 'd' and segunda != 'e':
            segunda = input('Resposta Inválida. Digite novamente: ')
        if segunda == segunda_questao:
            acertos += 1
        terceira = input('Questão 03: ')
        while terceira != 'a' and terceira != 'b' and terceira != 'c' and terceira != 'd' and terceira != 'e':
            terceira = input('Resposta Inválida. Digite novamente: ')
        if terceira == terceira_questao:
            acertos += 1
        quarta = input('Questão 04: ')
        while quarta != 'a' and quarta != 'b' and quarta != 'c' and quarta != 'd' and quarta != 'e':
            quarta = input('Resposta Inválida. Digite novamente: ')
        if quarta == quarta_questao:
            acertos += 1
        quinta = input('Questão 05: ')
        while quinta != 'a' and quinta != 'b' and quinta != 'c' and quinta != 'd' and quinta != 'e':
            quinta = input('Resposta Inválida. Digite novamente: ')
        if quinta == quinta_questao:
            acertos += 1
        sexta = input('Questão 06: ')
        while sexta != 'a' and sexta != 'b' and sexta != 'c' and sexta != 'd' and sexta != 'e':
            sexta = input('Resposta Inválida. Digite novamente: ')
        if sexta == sexta_questao:
            acertos += 1
        setima = input('Questão 07: ')
        while setima != 'a' and setima != 'b' and setima != 'c' and setima != 'd' and setima != 'e':
            setima = input('Resposta Inválida. Digite novamente: ')
        if setima == setima_questao:
            acertos += 1
        oitava = input('Questão 08: ')
        while oitava != 'a' and oitava != 'b' and oitava != 'c' and oitava != 'd' and oitava != 'e':
            oitava = input('Resposta Inválida. Digite novamente: ')
        if oitava == oitava_questao:
            acertos += 1
        nona = input('Questão 09: ')
        while nona != 'a' and nona != 'b' and nona != 'c' and nona != 'd' and nona != 'e':
            nona = input('Resposta Inválida. Digite novamente: ')
        if nona == nona_questao:
            acertos += 1
        decima = input('Questão 10: ')
        while decima != 'a' and decima != 'b' and decima != 'c' and decima != 'd' and decima != 'e':
            decima = input('Resposta Inválida. Digite novamente: ')
        if decima == decima_questao:
            acertos += 1
        lista.append(acertos)
        acertos = 0
        print('----------------------------------------------------')
        outro = input('Outro Aluno utilizará o Sistema (Sim ou Não)? ')
        while outro != 'Sim' and outro != 'sim' and outro != 'Não' and outro != 'não' and outro != 'nao' and outro != 'Nao':
            outro = input('Resposta Inválida. Responda apenas com "Sim" ou "Não": ')
        print('----------------------------------------------------')
        if outro in 'Não, não, nao, Nao':
            maior = max(lista)
            menor = min(lista)
            alunos = len(lista)
            media = sum(lista)/alunos
            print(f'                 Resumo da Prova: \n---------------------------------------------------- \nA maior nota foi {maior}. \nA menor nota foi {menor}. \n{alunos} aluno(s) utilizaram o sistema. \nA média da turma foi de {media}.')
        print('----------------------------------------------------')
        mostrar = input('Deseja visualizar o Gabarito (Sim ou Não)? ')
        if mostrar in 'sim, Sim, SIM':
            print('---------------------------------------------------- \n                Gabarito da Prova: \n----------------------------------------------------')
            print(f'Questão 01: {primeira_questao} \nQuestão 02: {segunda_questao} \nQuestão 03: {terceira_questao} \nQuestão 04: {quarta_questao} \nQuestão 05: {quinta_questao} \nQuestão 06: {sexta_questao} \nQuestão 07: {setima_questao} \nQuestão 08: {oitava_questao} \nQuestão 09: {nona_questao} \nQuestão 10: {decima_questao} \n----------------------------------------------------') 
verifica_nota()