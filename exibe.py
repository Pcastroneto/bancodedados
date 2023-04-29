import mysql.connector

#conectando banco de dados
config = {
    'user':'admin',
    'password':'aulanoiteFaculdade',
    'host':'dbaula.cpcnfjng6gnj.us-east-1.rds.amazonaws.com',
    'database':'aula'
}

#Estabelecer a conexão com banco de dados
try:
    conn =mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou:{err}")
    
#Criando um objeto cursor para executar as consultas SQL
cursor = conn.cursor()
    
#Inserindo o estado na tabela
sql = "SELECT * FROM estado"
cursor.execute(sql)

#Obter resultado da consulta
result = cursor.fetchall()
print(result)

#Imprimindo os resultados
for linhas in result:
    print(linhas)

#Fechar a conexão e o cursor 
conn.close()