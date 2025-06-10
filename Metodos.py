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

