from operacoesbd import *

conexão = criarConexao('127.0.0.1','root','12345', 'manifestacoes')
consulta = 'select * from Manifestacoes'
manifestacoes = listarBancoDados(conexão,consulta)
if len(manifestacoes) == 0:
     print("Não existe nenhuma Manifestação para ser listada")
else:
     print("Lista de Manifestações:")
     for item in manifestacoes:
          print("- Código da Manifestação:",item[0],"Titulo da Manifestação:",item[1],"Autor:",item[3],"Tipo da manifestação: ",item[4])

encerrarConexao(conexão)