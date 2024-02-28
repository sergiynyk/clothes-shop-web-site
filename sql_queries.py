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

    def get_all_products(self):
        self.open()
        self.cursor.execute("SELECT * FROM products")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_products_by_category(self, category_id):
        self.open()
        self.cursor.execute('''SELECT * FROM products WHERE "category_id"=?''', [category_id])
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_all_categories(self):
        self.open()
        self.cursor.execute("SELECT * FROM categories")
        data = self.cursor.fetchall()
        self.close()
        return data
    
    def get_product(self, product_id):
        self.open()
        self.cursor.execute('''SELECT * FROM products WHERE "id"=?''', [product_id])
        data = self.cursor.fetchone()
        self.close()
        return data
    
    def create_support(self, name, mail, phone_number, text):
        self.open()
        self.cursor.execute('''INSERT INTO support( name, mail, "phone number", text) VALUES(?, ?, ?, ?)''', [name, mail, phone_number, text])
        self.connection.commit()
        self.close()

    def create_order(self, product_id, name, phone, email, address, post_service, city, delivery, quantity, comment, cost, status = 0):
        self.open()
        self.cursor.execute('''INSERT INTO orders(product_id, name, phone, email, address, post_sevice, city, delivery, quantity, comment, cost, status) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''', [product_id, name, phone, email, address, post_service, city, delivery, quantity, comment, cost, str(status)])
        self.connection.commit()
        self.close()
