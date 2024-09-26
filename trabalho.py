# Função para importar dados dos arquivos
def importar_dados():
   try:
       with open('clientes.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               cursor.execute('INSERT INTO CLIENTES (ID, NOME, TELEFONE, EMAIL, ENDERECO) VALUES (?, ?, ?, ?, ?)', dados)
       with open('pets.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               cursor.execute('INSERT INTO PETS (ID, NOME, TIPO, RACA, ID_CLIENTE) VALUES (?, ?, ?, ?, ?)', dados)
       with open('agendamentos.txt', 'r') as arq:
           next(arq)  # Pular cabeçalho
           for linha in arq:
               dados = linha.strip().split(', ')
               cursor.execute('INSERT INTO AGENDAMENTOS (ID_AGENDAMENTO, DATA, HORARIO, SERVICO, ID_CLIENTE, ID_PET) VALUES (?, ?, ?, ?, ?, ?)', dados)
       conn.commit()
       print("Dados importados com sucesso.")
   except Exception as e:
       print(f"Ocorreu um erro ao importar dados: {e}")
