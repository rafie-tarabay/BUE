import mysql.connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="",database="mydatabase")

mycursor = mydb.cursor()


print("###############################")
#mycursor.execute("CREATE DATABASE mydatabase")
mycursor.execute("SHOW DATABASES")
for x in mycursor:
    print(x)


print("###############################")
#mycursor.execute("CREATE TABLE mydatabase.customers (name VARCHAR(255), address VARCHAR(255))")
mycursor.execute("SHOW Tables")
for x in mycursor:
    print(x)

print("###############################")
sql ="INSERT INTO mydatabase.customers (name, address) VALUES (%s, %s)"
val = ("John","Highway 21")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record inserted.")

print("###############################")
sql="UPDATE customers SET address = %s WHERE address = %s"
val=("Valley 345","Canyon 123")
mycursor.execute(sql,val)
mydb.commit()
print(mycursor.rowcount,"record(s) affected")

print("###############################")
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x[0])
