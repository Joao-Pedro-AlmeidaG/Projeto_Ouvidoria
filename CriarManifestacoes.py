from operacoesbd import *

TituloManifestacoes = input("Digite o titulo da manifestação:")
DescricaoManifestacoes = input("Digite a descrição:")
AutorManifestacoes = input("Qual o Autor:")
codtipodemanifestacao = int(input("Digite o tipo da sua manifestação 1-Para Elogio, 2- Para Reclamanção, 3- Para Sugestão:"))
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