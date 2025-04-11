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
cur.execute("SELECT * FROM Orders WHERE order_id < 9000;")
print("Scalar Query Time:", time.time() - start, "seconds")
rows = cur.fetchall()

# USe of explain 
cur.execute("EXPLAIN SELECT * FROM Orders WHERE order_id < 9000;")
print("EXPLAIN Scalar:", cur.fetchall())
explain_rows = cur.fetchall()

for row in explain_rows:
    print(row)

cur.close()
conn.close()