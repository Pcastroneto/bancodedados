from conexao import conectar

#chama a função conectar 
conn = conectar()
#criandp um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
# solicitando a entrada do usuario 
busca = input("Digite o nome do estado que deseja editar: ") 
#executando a consulta com o LIKE para verificar se o registro ex
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%" + busca + "%",)
cursor.execute(sql,val)
#obtendo o resultado
result = cursor.fetchone()
#se o resultado nao for nulo, o registro existe e pode ser editado

if result:
    codigo = result[0]
    nome_antigo = result[1]
    print(f"O nome o atual do estado é'{nome_antigo}'.")
    nome_novo = input("Digite o novo nome do estado: ")
        #solicite as novas informações par ao registro
    while not nome_novo:
        nome_novo = input("Digite o novo nome do estado: ")
    confirmacao = input(f"Tem certeza que deseja alterar o nome do estado'{nome_antigo}' para '{nome_novo}'?(s/n)")
    if confirmacao.lower() == 's':
        sql = "UPDATE estado SET nome = %s WHERE codigo = %s"
        val = (nome_novo, codigo)
        cursor.execute(sql,val)
        conn.commit()
        print(f"O nome do estado'{nome_antigo}'foi atualizado para '{nome_novo}'com sucesso!")
    else:
        print("Operação cancelada pelo usuario.")
        #se o resultado for nulo, o registro não existe
else:
    print("Não foi encontrado nenhum estado com esse nome informado")
#fechar a conexão e o cursor
conn.close()
