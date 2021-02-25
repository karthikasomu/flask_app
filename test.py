import sqlite3
connection = sqlite3.connect('data.db')
cursor = connection.cursor()
create_table = "CREATE TABLE if not exists users (id Integer PRIMARY KEY,username text,password text)"

cursor.execute(create_table)
insert_query = "insert into users values (?,?,?)"
user = (1,'karthika','karthi')
cursor.execute(insert_query,user)
users = [
    (2,'gayathri','gayath'),
    (3,'vignesh','vignes'),
    (4,'abcd','ab')
]
cursor.executemany(insert_query,users)

create_table_item = "CREATE TABLE if not exists items (id Integer PRIMARY KEY,name text,price text)"

cursor.execute(create_table_item)
insert_query_item = "insert into items values(?,?)"
item_names = [
    ('chair',23.45),
    ('keyboard',34.56),
    ('tshirt',56.56)]

cursor.executemany(insert_query_item,item_names)


select_query = "select * from users"
for row in cursor.execute(select_query):
    print(row)

select_query_items = "select * from items"
for row in cursor.execute(select_query_items):
    print(row)
connection.commit()
connection.close()