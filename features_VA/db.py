import sqlite3

con = sqlite3.connect("Voice_Assistant.db")
cursor = con.cursor()

query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key,name varchar(100),path varchar(100))"
cursor.execute(query)

# query = "INSERT INTO sys_command VALUES(null,'vs code','C:\\Users\\HP\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe')"
# cursor.execute(query)

query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key,name varchar(100),url varchar(100))"
cursor.execute(query)

# query = "INSERT INTO web_command VALUES(null,'google','https://google.com/')"

# cursor.execute(query)
con.commit()