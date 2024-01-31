import psycopg2

db = 'banquito'
user = "admin"
password = "123"
host = "localhost"
port = "5432"

conn = psycopg2.connect(f"dbname={db} user={user} password={password} host={host} port={port}")