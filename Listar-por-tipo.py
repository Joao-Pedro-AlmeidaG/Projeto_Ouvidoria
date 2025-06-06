from operacoesbd import *

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
