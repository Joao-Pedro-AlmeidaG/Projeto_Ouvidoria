# 🗣️ Sistema de Ouvidoria em Python

Este projeto é um sistema simples de ouvidoria desenvolvido em Python que permite cadastrar, listar, pesquisar e excluir manifestações de usuários em um banco de dados MySQL.

## 📌 Funcionalidades

- 📄 **Cadastrar manifestações** (Elogio, Reclamação, Sugestão)
- 📋 **Listar todas as manifestações**
- 🔍 **Listar manifestações por tipo**
- 🔢 **Exibir a quantidade de manifestações**
- 🆔 **Pesquisar manifestação por código**
- ❌ **Excluir manifestação por código**

## 🛠️ Tecnologias Utilizadas

- Python 3.x
- MySQL
- Biblioteca `mysql-connector-python`

## 🧩 Estrutura do Projeto

- `menu.py`: Interface principal do sistema com menu de navegação.
- `Metodos.py`: Contém as funções que implementam as funcionalidades principais.
- `operacoesbd.py`: Funções auxiliares para conexão, consulta, inserção e exclusão no banco de dados.
- `CriarManifestacoes.py`, `Listar.py`, `Listar-por-tipo.py`, `Pesquisar.py`, `quantidade1.py`: Scripts independentes para executar funcionalidades específicas.
