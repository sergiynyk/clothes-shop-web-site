from flask import Flask, render_template
from sql_queries import ShopDB

app = Flask(__name__)

db = ShopDB("clothes.db")

@app.route("/")
def index():
    posts = db.get_all_posts()
    return render_template("index.html", title = "Clothes-Shop", posts = posts)
@app.route("/support")
def support():
    return render_template("support.html", title = "Support")

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug = True)