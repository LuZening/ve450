import psycopg2

conn = psycopg2.connect(host="localhost", database="ve450")
cursor = conn.cursor()
cursor.execute("CREATE TABLE test (time varchar, sen1 real);")
cursor.execute("INSERT INTO test values ('haha', 12.323);")
conn.commit()
cursor.execute("SELECT * from test;")
row = cursor.fetchone()
print(row)
cursor.close()
conn.close()
