from operacoesbd import *
def quantidademanifestações(conexão):
    consulta = 'select count(*) from manifestacoes'
    quantidademanifestacoes = listarBancoDados(conexão, consulta)
    print('Existem', quantidademanifestacoes[0][0], 'manifestações!')
    