import sqlite3
conexao = sqlite3.connect("E:\Igor\Desktop\dados.db")

cursor = conexao.cursor()



#sql = '''
#create table teste (
#    id INTEGER PRIMARY KEY NOT NULL,
#    nome VARCHAR(20),
#    data VARCHAR(20),
 #   status VARCHAR(20),
#    categoria_id INT NOT NULL,
#    FOREIGN KEY (categoria_id) REFERENCES categoria(id)
#)

#'''

#cursor.execute(sql)

#id = 10
#ome = 'Iago'
#data = '01/03/2023'
#status = 'em andamento'
#categoria_id = 2
#cursor.execute("""
#INSERT INTO teste (id, nome, data, status, categoria_id) VALUES (?, ?, ?, ?, ?)
#""", (id, nome, data, status, categoria_id))

#cursor.execute(sql)

def execut_query():
    query = cursor.execute("""select * from teste""")   
    for linha in query:
        print(linha)


execut_query()
conexao.commit()
conexao.close()
