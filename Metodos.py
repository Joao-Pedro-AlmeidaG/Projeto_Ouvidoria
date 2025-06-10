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
