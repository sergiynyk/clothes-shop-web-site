import sqlite3

class ShopDB:
    def __init__(self, dbname):
        self.dbname = dbname
        self.connection = None
        self.cursor = None

    def open(self):
        self.connection = sqlite3.connect(self.dbname) # Підключаємося до бази даних
        self.cursor = self.connection.cursor()

    def close(self):
        self.cursor.close()
        self.connection.close()

    def get_all_posts(self):
        self.open()
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        self.close()
        return data