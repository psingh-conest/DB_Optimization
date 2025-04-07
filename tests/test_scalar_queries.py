import mysql.connector
import time

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_root_pw',
    database='ecommerce_orders'
)

cur = conn.cursor()

start = time.time()
cur.execute("SELECT AVG(payment_value) FROM payments;")
print("Avg Payment:", cur.fetchone())
print("Scalar query time:", time.time() - start, "s")
