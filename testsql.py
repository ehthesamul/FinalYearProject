import mysql.connector
mydb =  mysql.connector.connect(host="localhost", user="root", passwd="samul54321",database="userslist",auth_plugin='mysql_native_password')
mycursor = mydb.cursor()
mycursor.execute("select * from users")
for i in mycursor:
    print(i[2])