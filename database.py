import psycopg2

class DB:
    def __init__(self):
        self.db = 'banquito'
        self.user = "postgres"
        self.password = "123"
        self.host = "localhost"
        self.port = "5432"

        self.conn = psycopg2.connect(f"dbname={self.db} user={self.user} password={self.password} host={self.host} port={self.port}")
        self.cur = self.conn.cursor()
        
        self.cur.execute("""
            CREATE TABLE IF NOT EXISTS cuentas (
                id VARCHAR(255) PRIMARY KEY,
                balance FLOAT
            );
        """)
        
        self.conn.commit()

    def get_accounts(self):
        self.cur.execute("SELECT * from cuentas")
        rows = self.cur.fetchall()
        return rows
    
    def add_account(self, id):

        self.cur.execute(f"INSERT INTO cuentas (id, balance) VALUES ('{id}', 0)")

        self.conn.commit()

        return True
    
    def update_balance(self, id, amount):
        self.cur.execute(f"UPDATE cuentas SET balance = {amount} WHERE id = '{id}'")

        self.conn.commit()

        return True
    
    def __del__(self):
        self.cur.close()
        self.conn.close()