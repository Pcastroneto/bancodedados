from conexao import conectar

# chama a função conectar
conn = conectar()

# criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()

# solicitando a entrada do usuário
busca = input("Digite o nome que deseja buscar: ")

# executando a consulta com LIKE para verificar se o registro existe
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%" + busca + "%",)
cursor.execute(sql, val)

# obtendo o resultado
result = cursor.fetchone()

# se o resultado não for nulo, o registro existe e pode ser deletado
if result:
    codigo = result[0]
    nome = result[1]
    confirmacao = input(f"Tem certeza que deseja deletar o estado '{nome}'? (s/n) ")

    # se a confirmação for positiva, deleta o registro
    if confirmacao.lower() == "s":
        sql = "DELETE FROM estado WHERE codigo = %s"
        val = (codigo,)
        cursor.execute(sql, val)
        conn.commit()
        print(f"O estado '{nome}' foi deletado com sucesso!")
    else:
        print("Operação cancelada pelo usuário.")

# se o resultado for nulo, o registro não existe
else:
    print("Não foi encontrado nenhum estado com o nome informado.")

# fechar a conexão e o cursor
conn.close()