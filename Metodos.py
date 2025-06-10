from operacoesbd import *



def ListarManifestacoes(conexão):
    consulta = 'select * from Manifestacoes'
    manifestacoes = listarBancoDados(conexão, consulta)
    if len(manifestacoes) == 0:
        print("Não existe nenhuma Manifestação para ser listada")
    else:
        print("Lista de Manifestações:")
        for item in manifestacoes:
            print("\n- Código da Manifestação:", item[0], "Titulo da Manifestação:", item[1], "Autor:", item[3],",Descrição:", item[2], ",Tipo da manifestação: ", item[4])


def listarporTipo(conexão):
    TipodeManifestacao = int(input("DIgite o tipo da manifestação para listar: 1-Para Elogio, 2- Para Reclamanção, 3- Para Sugestão: "))
    if TipodeManifestacao == 1:
        TipodeManifestacao = "Elogio"
    elif TipodeManifestacao == 2:
        TipodeManifestacao = "Reclamação"
    elif TipodeManifestacao == 3:
        TipodeManifestacao = "Sugestão"
    consulta = 'select * from manifestacoes where tipo like %s'
    dados = [TipodeManifestacao]
    manifestacoes = listarBancoDados(conexão, consulta, dados)
    if len(manifestacoes) == 0:
        print("Não existe manifestações para o tipo informado.")
    else:
        print("Manifestações encontradas:")
        for manifestacao in manifestacoes:
            print("- Título:",manifestacao[1], ",Descrição:",manifestacao[2], ",Autor:",manifestacao[3],",tipo",manifestacao[4])



def PesquisarManifestacao(conexão):
    codigo = input("Digite o código da manifestação ser pesquisado: ")
    consulta = 'select * from manifestacoes where codigo_manifestacao = %s'
    dados = [codigo]
    manifestacoes = listarBancoDados(conexão,consulta,dados)
    if len(manifestacoes) == 0:
        print("Não existe manifestações para o código informado.")
    else:
        print("Manifestação encontrada")
        print("-Titulo da manifestação:",manifestacoes[0][1],",Descrição:",manifestacoes[0][2],",Autor:",manifestacoes[0][3],",Tipo:",manifestacoes[0][4])
        
def quantidademanifestações(conexão):
    consulta = 'select count(*) from manifestacoes'
    quantidademanifestacoes = listarBancoDados(conexão, consulta)
    print('Existem', quantidademanifestacoes[0][0], 'manifestações!')

def CriarManifestacoes(conexão):
    TituloManifestacoes = input("Digite o titulo da manifestação:")
    DescricaoManifestacoes = input("Digite a descrição:")
    AutorManifestacoes = input("Qual o Autor:")
    codtipodemanifestacao = int(
        input("Digite o tipo da sua manifestação 1-Para Elogio, 2- Para Reclamanção, 3- Para Sugestão:"))
    if codtipodemanifestacao == 1:
        codtipodemanifestacao = "Elogio"
    elif codtipodemanifestacao == 2:
        codtipodemanifestacao = "Reclamação"
    elif codtipodemanifestacao == 3:
        codtipodemanifestacao = "Sugestão"
    consulta = 'insert into manifestacoes (titulo,descricao,autor,tipo) values(%s,%s,%s,%s)'
    dados = [TituloManifestacoes, DescricaoManifestacoes, AutorManifestacoes, codtipodemanifestacao]

    codigodemanifestacoes = insertNoBancoDados(conexão, consulta, dados)
    print("Manifestação cadastrada com sucesso! 0 código da sua manifestação é", codigodemanifestacoes)

def ExcluirManifestacao(conexão):
    codigo = int(input("Digite o código da manifestação que deseja excluir: "))
    consulta = 'delete from manifestacoes where codigo_manifestacao = %s'
    dados = [codigo]
    linhasAfetadas = excluirBancoDados(conexão, consulta, dados)
    if linhasAfetadas == 0:
        print("Não existe Manifestações para o código informado.")
    else:
        print("Manifestação removida com sucesso!!!")

