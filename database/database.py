import mysql.connector

# conn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password=""
# )
#
# mycursor = conn.cursor()

# mycursor.execute("SHOW DATABASES")
#
# for x in mycursor:
#     print(x)

#Create Database
# mycursor.execute("CREATE DATABASE python")


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="python"
)

mycursor = conn.cursor()

#Show Tables
# mycursor.execute("SHOW TABLES")
#
# for x in mycursor:
#     print(x)

#Create Table
# mycursor.execute("CREATE TABLE users (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255), age INT)")

#Insert Data
# mycursor.execute("INSERT INTO users (name, age) VALUES ('John', 30)")
# sql = "INSERT INTO users (name, age) VALUES (%s, %s)"
# val = (
#     ('Jane', 25),
#     ('Bob', 40),
#     ('Alice', 35),
#     ('Mike', 28)
# )
# mycursor.executemany(sql, val)
# conn.commit()
#
# print(mycursor.rowcount, "record inserted.")

#Select Data
# mycursor.execute("SELECT * FROM users")
# mycursor.execute('SELECT * FROM users LIMIT 2 OFFSET 2')
# users = mycursor.fetchall()
#
# for x in users:
#     print(x)

#Select Data by ID
# mycursor.execute("SELECT * FROM users WHERE id = 1")
#
# users = mycursor.fetchall()
#
# for x in users:
#     print(x)

#Select first row
# mycursor.execute("SELECT * FROM users LIMIT 1")
# user = mycursor.fetchall()
# print(user) #[(1, 'John', 30)]

# mycursor.execute("SELECT * FROM users")
# users = mycursor.fetchone()
# print(users) #(1, 'John', 30)

#Where and Order By and LIKE
# mycursor.execute("SELECT * FROM users WHERE age = 30 ORDER BY name DESC")
# mycursor.execute("SELECT * FROM users WHERE name LIKE 'J%'")
# users = mycursor.fetchall()
# print(users)

#Update Data
# mycursor.execute("UPDATE users SET age = 35 WHERE id = 1")
# conn.commit()
# print(mycursor.rowcount, "record(s) affected")

#Delete Data
# mycursor.execute("DELETE FROM users WHERE id = 1")
# conn.commit()
# print(mycursor.rowcount, "record(s) deleted")

#Delete Table
# mycursor.execute("DROP TABLE users")
# mycursor.execute("DROP TABLE IF EXISTS users")
# conn.commit()
# print(mycursor.rowcount, "table(s) deleted")

#Delete Database
# mycursor.execute("DROP DATABASE python")
# conn.commit()
# print(mycursor.rowcount, "database(s) deleted")

#Create another table posts
# mycursor.execute("CREATE TABLE posts (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), content TEXT)")
# conn.commit()
# print(mycursor.rowcount, "table(s) created")

#Insert Many items in posts table
# sql = "INSERT INTO posts (title, content) VALUES (%s, %s)"
# val = (
#     ('Post 1', 'Content 1'),
#     ('Post 2', 'Content 2'),
#     ('Post 3', 'Content 3'),
#     ('Post 4', 'Content 4'),
#     ('Post 5', 'Content 5')
# )
# mycursor.executemany(sql, val)
# conn.commit()
# print(mycursor.rowcount, "record(s) inserted.")

#Select Data from posts table
# mycursor.execute("SELECT * FROM posts")
# posts = mycursor.fetchall()
# for x in posts:
#     print(x)

#Add new column user_id to posts table
# mycursor.execute("ALTER TABLE posts ADD COLUMN user_id INT")
# conn.commit()
# print(mycursor.rowcount, "column(s) added")

#Join Tables
# mycursor.execute("SELECT users.name,\
#  posts.title \
#  FROM users \
#  JOIN posts ON users.id = posts.user_id")
# users = mycursor.fetchall()
# print(users)

#Left join
# mycursor.execute("SELECT users.name, posts.title FROM users LEFT JOIN posts ON users.id = posts.user_id")
# users = mycursor.fetchall()
# print(users)

#Right join
# mycursor.execute("SELECT users.name, posts.title FROM users RIGHT JOIN posts ON users.id = posts.user_id")
# users = mycursor.fetchall()
# print(users)







