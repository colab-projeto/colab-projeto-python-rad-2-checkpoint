import sqlite3
# Conectar ao banco de dados
conn = sqlite3.connect('petshop.db')  # Altere 'petshop.db' para o caminho correto do seu arquivo .db, se necessário
cursor = conn.cursor()
# Função para importar dados dos arquivos
def importar_dados():
   try:
       # Importar dados dos clientes
       with open('clientes.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               if len(dados) == 5:  # Verifica se temos 5 campos
                   cursor.execute('INSERT INTO CLIENTES (ID, NOME, TELEFONE, EMAIL, ENDEREÇO) VALUES (?, ?, ?, ?, ?)', dados)
               else:
                   print(f"Erro: Linha com dados incorretos: {linha.strip()}")
       # Importar dados dos pets
       with open('pets.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               if len(dados) == 5:  # Verifica se temos 5 campos
                   cursor.execute('INSERT INTO PETS (ID, NOME, TIPO, RAÇA, ID_CLIENTE) VALUES (?, ?, ?, ?, ?)', dados)
               else:
                   print(f"Erro: Linha com dados incorretos: {linha.strip()}")
       # Importar dados dos agendamentos
       with open('agendamentos.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               if len(dados) == 6:  # Verifica se temos 6 campos
                   cursor.execute('INSERT INTO AGENDAMENTOS (ID_AGENDAMENTO, DATA, HORÁRIO, SERVIÇO, ID_CLIENTE, ID_PET) VALUES (?, ?, ?, ?, ?, ?)', dados)
               else:
                   print(f"Erro: Linha com dados incorretos: {linha.strip()}")
       conn.commit()
       print("Dados importados com sucesso.")
   except Exception as e:
       print(f"Ocorreu um erro ao importar dados: {e}")
# Função para listar clientes
def listar_clientes():
   try:
       cursor.execute('SELECT * FROM CLIENTES')
       for cliente in cursor.fetchall():
           print(cliente)
   except Exception as e:
       print(f"Ocorreu um erro ao listar clientes: {e}")
# Executar funções
importar_dados()  # Importar dados
listar_clientes()  # Listar clientes
# Fechar a conexão
conn.close()
