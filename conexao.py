import mysql.connector

def conectar():
    mydb = mysql.connector.connect(
        host = 'dbaula.cpcnfjng6gnj.us-east-1.rds.amazonaws.com',
        user = 'admin',
        password= 'aulanoiteFaculdade',
        database = 'aula'
    )
    return mydb
    