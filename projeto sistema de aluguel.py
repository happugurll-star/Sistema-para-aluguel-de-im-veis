def locatário():
    while True:
        print('Você escolheu cadastrar um imóvel')
        nome = input('Nome completo do proprietário: ').upper()
        local= input('Local:')
        orçamento= int(input('Valor: R$'))
        qunt_pessoas = int(input('Quantidade de pessoas:'))
        dados = [nome, local, orçamento, qunt_pessoas]

        imovel:{ 'proprietário' :nome,
                  'local':local,
                  'orçamento': orçamento,
                  'capacidade':qunt_pessoas }

        imoveis.append(imovel)
        global imoveis
        print(f'{dados}')
        l= (str(input('Deseja cadastrar mais algum estabelecimento?Responda Sim ou Não ').capitalize()))
        if l == 'Não':
            print('Obrigado por cadastrar seu imóvel conosco')
            break

def inquilino():
    print('Você decidiu alugar um imóvel')
    nome = input('Nome completo: ').upper()
    local= input('Local: ')
    orçamento= int(input('Valor:   R$'))
    qunt_pessoas = int(input('Quantidade de pessoas:'))
    dados = [nome, local, orçamento, qunt_pessoas ]
    print(f'{dados}')
    print('Obrigada por buscar no nosso banco de dados,vamos exibir os resultados compatíveis com seu interesse')

    return {'nome':local,
            'local':local,
            'orçamento':orçamento,
            'capacidade':qunt_pessoas }

def funcionario():
    global reservas
    funcionarios_da_empresa= ['Kate', 'Anthony']
    nome= input('Nome completo: ').capitalize()
    if nome not in funcionarios_da_empresa:
        print('NENHUM FUNCIONÁRIO COM ESTE NOME ESTÁ CADASTRADO')
        return
    while True:
            escolha = input('Você deseja...'
                            '[1]Verificar histórico de reservas'
                            ' [2]Adicionar novo funcionário'
                            '[3]Sair')
            if escolha == '1':
                if len(reservas) == 0:
                    print('SEM HISTÓRICO DE RESERVAS')
                else:
                    print('HISTÓRICO DE RESERVAS')
                    for i,reservas in enumerate(reservas, start=1):
                        print(f'Nome:{reservas[0]},Local:{reservas[1]},'
                              f'Orçamento{reservas[2]},capacidade de pessoas{reservas[3]}')
                sair = input('Deseja sair?').capitalize()
                if sair == 'Sim':
                    break
            elif escolha == '2':
                novo_funcionário=input('Nome completo: ').capitalize()
                funcionarios_da_empresa.append(novo_funcionário)
                print(f'{funcionarios_da_empresa}')
            else:
                break

def filtrar_imoveis():
    compativeis = []
    for imovel in imóveis:
        if (imovel['local']==inquilino['local'] and
        imovel['orçamento'] >= inquilino['valor'] and
        imovel['capacidade'] == inquilino['pessoas']):
            compativeis.append(imovel)
    return compativeis

def mostrar_compativeis(lista):
    for i,imovel in enumerate(lista,1) : #enumerate passa pela lista inteira
        print( f"{i},Proprietário - {imovel['proprietário']} " ,
               f"local - {imovel['local']}",
               f"valor - {imovel['valor']}",
               f"capadidade de pessoas - {imovel['capacidade']}") #corelação com o dicionario do locatario





#Sistema principal
reservas = []
imóveis = []
while True:
    print('Bem vindo ao sistema de alugéis,escolha o próximo passo a seguir:'
          '[1]Cadastrar um imóvel'
          '[2]Alugar um imóvel'
          '[3]Funcionário da empresa'
          '[4]SAIR')
    escolha = str(input('       ')).strip()
    if escolha == '1':
        locatário()
    elif escolha == '2':
        dados = inquilino() #recebe dados do inquilino
        reservas.append(dados) #salva no histórico
    elif escolha == '3':
        funcionario()
    elif escolha == '4':
        break