import mysql.connector
import time

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='your_root_pw',
    database='ecommerce_orders'
)

cur = conn.cursor()



cur.execute("CREATE FULLTEXT INDEX ft_product ON products(product_name);")
conn.commit()

start = time.time()
cur.execute("SELECT * FROM products WHERE MATCH(product_name) AGAINST('celular');")
print("Fulltext query time:", time.time() - start, "s")

cur.execute("EXPLAIN SELECT * FROM products WHERE MATCH(product_name) AGAINST('celular');")
print("EXPLAIN plan:", cur.fetchall())
