from flask import Flask, render_template
from sql_queries import ShopDB

app = Flask(__name__)

db = ShopDB("clothes.db")

@app.route("/")
def index():
    categories = db.get_all_categories()
    products = db.get_all_products()
    return render_template("index.html", title = "Clothes-Shop", products = products, categories = categories)

@app.route("/support")
def support():
    categories = db.get_all_categories()
    return render_template("support.html", title = "Support", categories = categories)

@app.route("/catalog")
def all_catalog():
    categories = db.get_all_categories()
    products = db.get_all_products()
    return render_template("all_products.html", title = "Clothes-Shop", products = products, categories = categories)

@app.route("/catalog/<category_id>")
def catalog(category_id):
    categories = db.get_all_categories()
    products = db.get_products_by_category(category_id)
    return render_template("catalog-clothes.html", title = "Каталог", categories = categories, products = products)

@app.route("/product/<product_id>")
def product(product_id):
    categories = db.get_all_categories()
    product = db.get_product(int(product_id))
    return render_template("product.html", title = product[1], product = product, categories = categories)

@app.route("/product/<product_id>/order")
def order(product_id):
    categories = db.get_all_categories()
    product = db.get_product(int(product_id))
    return render_template("order.html", title = product[1], product = product, categories = categories)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)