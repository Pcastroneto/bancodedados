import mysql.connector

#conectando banco de dados
config = {
    'user':'admin',
    'password':'aulanoiteFaculdade',
    'host':'dbaula.cpcnfjng6gnj.us-east-1.rds.amazonaws.com',
    'database':'aula'
}

# Estabelecer a conexão com banco de dados
try:
    conn = mysql.connector.connect(**config)
    print("Conexão executada com sucesso.")
except mysql.connector.Error as err:
    print(f"Conexão falhou: {err}")
    
#criando um objeto cursor para executar as consutlas SQL
cursor = conn.cursor()

#Pedindo ao usuário o nome e código do estado
nome_estado = input("Digite o nome estado: ")
codigo_estado = int(input("Digite o código do estado: "))

#Inserindo o estado na tabela
sql ="INSERT INTO estado (codigo,nome) VALUES (%s, %s)"
val = (codigo_estado, nome_estado)
cursor.execute(sql,val)

#Efetuando as mudanças no banco de dados
conn.commit()

print(cursor.rowcount,"registro(s) inserido(s) com sucesso.")

#Fechar a conexão e o cursor
conn.close()