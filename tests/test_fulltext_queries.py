import mysql.connector
import time

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="ecommerce_user",
    password="",
    database="brazilian_ecommerce"
)

cur = conn.cursor()


start = time.time()
cur.execute("ALTER TABLE Orders ADD FULLTEXT(order_status);")
cur.execute("SELECT * FROM Orders WHERE MATCH(order_status) AGAINST('invoiced');")
results = cur.fetchall() 
print("Full-Text Search Time:", time.time() - start, "seconds")


cur.execute("EXPLAIN SELECT * FROM Orders WHERE MATCH(order_status) AGAINST('invoiced');")
print("EXPLAIN plan:", cur.fetchall())

cur.close()
conn.close()