import mysql.connector

#conectando banco de dados
config = {
    'user':'admin',
    'password':'aulanoiteFaculdade',
    'host':'dbaula.cpcnfjng6gnj.us-east-1.rds.amazonaws.com',
    'database':'aula'
}

# Estabeleccer a conexão com o banco de dados
try:
    conn=mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
#Criando um objeto com o cursor para executar as consultas SQL
cursor = conn.cursor()

#Solicitando a entrada do usuário
busca = input("Digite o nome que deseja buscar:")

#Executando a consulta com LIKE
sql = "SELECT * FROM estado WHERE nome LIKE %s"
val = ("%"+ busca+"%",)
cursor.execute(sql,val)

#Obtendo os resultados
results= cursor.fetchall()

#iterando sobre os resultados
for result in results:
    print(result)

#Fechar a conexão e o cursor
conn.close()
    