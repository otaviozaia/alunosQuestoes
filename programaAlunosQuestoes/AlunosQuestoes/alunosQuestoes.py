'''
#escrever em arquivo:
arq = open('csv.txt', 'w')
texto = """
Lista de Alunos
---
João da Silva
José Lima
Maria das Dores
"""
arq.write(texto)
arq.close()
'''
'''
#
arq = open('csv.txt', 'w')
texto = []
texto.append('Lista de Alunos\n')
texto.append('---\n')
texto.append('João da Silva\n')
texto.append('José Lima\n')
texto.append('Dias')
arq.writelines(texto)
arq.close()
'''
def lerQuestoes(arquivo):
    #le arquivo e transforma em lista
    lista = []
    arq = open(arquivo, 'r')#abre o arquivo e le
    texto = arq.readlines()#texto recebe cada linha do arquivo
    for linha in texto :#para cada linha do texto
        var = linha.split(',,')#var recebe a linha transformada em lista, elementos são dividos por ',,'
        for i in var:#para cada item em var
            if i == '\n':#se o item for uma quebra de linha (string \n)
                var.remove(i)#retire o \n da lista
        lista.append(var)#lista recebe var (linha transformada em lista)
    arq.close()#fecha o arquivo
    return lista
def lerAlunos(arquivo):
    #faz o mesmo de cima, para a lista de alunos
    alunos = []
    arq2 = open(arquivo, 'r')
    itens = arq2.readlines()
    for j in itens:
        varr = j.split(',,')
        for k in varr:
            if k == '\n':
                varr.remove(k)
        alunos.append(varr)
    arq2.close()
    return alunos
def getTurmas(lista):
    turmas = []
    aluno = lerAlunos(lista)
    for i in range(len(aluno)):
        if aluno[i][0] not in turmas:
            turmas.append(aluno[i][0])
    return turmas

def alunoQuestTurma(questions,alunos):
    questions = lerQuestoes(questions)
    alunos = lerAlunos(alunos)
    #cria dicionario que receberá lista com questões
    questoesTurma = {}
    for a in range(len(questions[0])):
        questoes = []
        for b in range(len(questions)):
            if b>0:
                questoes.append(questions[b][a])
            questoesTurma[questions[0][a]] = questoes
    dicAlunos = {}
    for i in range(len(alunos)):
        for k,v in questoesTurma.items():
            for caractere in k:
                if alunos[i][0][0] == caractere:
                     dicAlunos[alunos[i][2]] = [v,alunos[i][0]]
    return dicAlunos

def listaFinal(arquivo1,arquivo2):
    groups = getTurmas(arquivo2)
    listaFim = {}
    for g in groups:
        listaFim[g] = []
    alunoQuestoes = alunoQuestTurma(arquivo1,arquivo2)
    for i in groups:
        for k,v in alunoQuestoes.items():
            if i == v[1]:
                listaFim[v[1]].append({k:v})
    return listaFim

def inputs(arqv1,arqv2):
    students = lerAlunos(arqv2)
    base = listaFinal(arqv1,arqv2)
    group = getTurmas(arqv2)
    dicFinal = {}
    for g in group:
        dicFinal[g]={}
    while True:
        print('--------------------------------------------------------------')
        while True:
            turma = input('Informe a turma: ')
            if turma not in group:
                print('Turma Inválida!')
            else:
                break
        for i in base[turma]:
            for k,v in i.items():
                for std in range(len(students)):
                    if k==students[std][2]:
                        stu = students[std][1]
                        print('\n')
                        print('RA: ',k,'|| Aluno: ',stu,'|| Turma: ',turma)
                        print('--------------------------------------------------------------')
                        dicAluno = {}
                        for j in v[0]:
                            if j =='':
                                continue
                            else:
                                valor = input('{}:'.format(j))
                                if valor not in ['0','1','2','3']:
                                    print('Valor inválido! Não foi adicionado.')
                                    dicAluno[j]='VAZIO'
                                    print('\n')
                                else:                                    
                                    dicAluno[j]=valor
                                    print('\n')
                dicFinal[turma][k]=dicAluno
        print('\n')
        opcao = input('Nova turma? (S/N)')
        if opcao == 'N' or opcao == 'n':
            break
        elif opcao == 's' or opcao == 'S':
            continue            
    return dicFinal

res = inputs('csv.txt','alunos.txt')
planilha = input('Nomeie sua Planilha: ')
texto = []
for ee,ff in res.items():
    for jj,ll in ff.items():
        listinha = [ee,jj]
        for q,p in ll.items():
            listinha.append(q)
            listinha.append(p)
        texto.append(listinha) 

student = lerAlunos('alunos.txt')

for indx in range(len(texto)):
    for two in range(len(student)):
        if texto[indx][1] == student[two][2]:
            listaB = []
            for i1 in texto[indx][:2]:
                listaB.append(i1)
            listaB.append(student[two][1])
            for i2 in texto[indx][2:]:
                listaB.append(i2)                
            texto[indx] = listaB

import xlwt

book = xlwt.Workbook(encoding='utf-8')

sheet1 = book.add_sheet('Alunos e Questões')

for line in range(len(texto)):
    for colunm in range(len(texto[line])):
        sheet1.write(line,colunm,texto[line][colunm])

book.save('{}.xls'.format(planilha))

'''
para arquivo de texto:
res1 = str(res)
arqW = open('resultado.txt', 'w')#abre o arquivo que receberá o resultado
arqW.write(res1)#escreve a lista no arquivo
arqW.close()#fecha o arquivo

'''
