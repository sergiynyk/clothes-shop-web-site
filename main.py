from flask import Flask, render_template, request, flash
from sql_queries import ShopDB
import os
app = Flask(__name__)

db = ShopDB("clothes.db")
app.config["SECRET_KEY"] = 'WLIgvbihg248go48ug240tuPHJ#TY9u32hgq80ef'

@app.route("/")
def index():
    categories = db.get_all_categories()
    products = db.get_all_products()
    return render_template("index.html", title = "Clothes-Shop", products = products, categories = categories)

@app.route("/support", methods = ["POST", "GET"])
def support():
    categories = db.get_all_categories()
    if request.method == "POST":
        try:
            db.create_support(request.form['name'], request.form['email'], request.form['phone'], request.form['problem'])
            flash("Повідомлення додано, очікуйте відповідь на пошті!", "alert-success")
        except:
            flash("Помилка надсилання повідомлення до сервера, спробуйте ще раз пініше.", "alert-danger")
    return render_template("support.html", title = "Support", categories = categories)

@app.route("/about_us")
def about_us():
    categories = db.get_all_categories()
    return render_template("about_us.html", title = "About Us", categories = categories)


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

@app.route("/product/<product_id>/order", methods = ["POST", "GET"])
def order(product_id):
    categories = db.get_all_categories()
    product = db.get_product(int(product_id))
    if request.method == "POST":
        try:
            cost = request.form["quantity"] * product[6]
            db.create_order(product_id, request.form['name'], request.form['phone'], request.form['email'], request.form['address'], request.form['post_service'], request.form['city'], request.form['delivery'], request.form['quantity'], request.form['comment'], cost, 0)
            flash("Замовлення оформлено!", "alert-success")
        except:
            flash("Помилка оформлення, спробуйте ще раз пініше.", "alert-danger")
    return render_template("order.html", title = product[1], product = product, categories = categories)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)