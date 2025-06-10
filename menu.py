from operacoesbd import *
from Metodos import  *
conexão = criarConexao('127.0.0.1','root','12345','manifestacoes')

opcao = 1
while opcao !=7:
    print("\n1) Listagem das Manifestações \n2) Listagem de Manifestações por Tipo \n3) Criar uma nova Manifestação \n4) Exibir quantidade de manifestações \n5) Pesquisar uma manifestação por código \n6) Excluir uma Manifestação pelo Código \n7) Sair do Sistema ")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        ListarManifestacoes(conexão)

    elif opcao == 2:


    elif opcao == 3:
        CriarManifestacoes(conexão)

    elif opcao == 4:
        quantidademanifestações(conexão)

    elif opcao == 5:
        PesquisarManifestacao(conexão)


    elif opcao == 6:
        ExcluirManifestacao(conexão)


    elif opcao  != 7:
        print("opção invalida")

print("Obrigado por acessar as manifestações")
encerrarConexao(conexão)
