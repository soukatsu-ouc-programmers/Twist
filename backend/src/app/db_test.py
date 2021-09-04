import mysql.connector as mysql
user_name = "twist"
password = "twist"
host = "db"  # docker-composeで定義したMySQLのサービス名
database_name = "tweet-db"


conn = mysql.connect(
    host="db",
    user="twist",
    passwd="twist",
    port=3306,
    database="tweet-db"
)

conn.ping(reconnect=True)

cursor = conn.cursor()

sql = '''
CREATE TABLE student (
    student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    first_name VARCHAR(50) NULL,
    last_name VARCHAR(50) NULL,
    birthday DATE NULL,
    gender ENUM('F','M')
)'''
cursor.execute(sql)

cursor.execute("SHOW TABLES")
print(cursor.fetchall())

sql = ('''
INSERT INTO student 
    (first_name, last_name, birthday, gender)
VALUES 
    (%s, %s, %s, %s)
''')

data = [
    ('Shota', 'Sato', '2001-03-12', 'M'),
    ('Hiroki', 'Takagi', '2000-04-05', 'M'),
    ('Yuka', 'Kimura', '2001-03-27', 'F')
]

cursor.executemany(sql, data)
conn.commit()

print(f"{cursor.rowcount} records inserted.")

cursor.close()

print(conn.is_connected())
