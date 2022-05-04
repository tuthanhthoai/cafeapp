from flask import render_template, request, url_for
from flask_login import login_user, current_user

from webapp import login
from webapp.admin import *


@app.route('/')
def home():
    return render_template('home.html')


@login.user_loader
def load_user(user_id):
    return utils.get_user_by_id(user_id=user_id)


@app.route("/signin", methods=["get", "post"])
def signin():
    err_msg = ""
    if request.method.__eq__("POST"):
        username = request.form.get("username")
        password = request.form.get("password")

        user = utils.check_login(username=username, password=password)
        if user:
            login_user(user=user)
            return redirect("/")
        else:
            err_msg = "Incorrect username or password"
    return render_template("signin.html", err_msg=err_msg)


@app.route("/signup", methods=["get", "post"])
def signup():
    err_msg = ""
    if request.method.__eq__("POST"):
        new_account = {
            "name": "",
            "email": "",
            "phone": "",
            "address": "",
            "username": "",
            "password": "",
        }
        new_account["name"] = request.form.get("name")
        new_account["email"] = request.form.get("email")
        new_account["phone_number"] = request.form.get("phone_number")
        new_account["address"] =request.form.get("address")
        new_account["username"] = request.form.get("username")
        new_account["password"] = request.form.get("password")
        confirm_password = request.form.get("confirm_password")
        try:
            if new_account["password"].strip().__eq__(confirm_password.strip()):
                utils.add_user(new_account)
                return redirect("/")
            else:
                err_msg = "Invalid Confirm Password"
        except Exception as ex:
            err_msg = "Wrong"
    return render_template("signup.html", err_msg=err_msg)


@app.route("/Tra-hoa-qua")
def show_id_01():
    products = Product.query.all()
    category_id = 1
    category_name = "Trà hoa quả"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Ca-phe")
def show_id_02():
    products = Product.query.all()
    category_id = 2
    category_name = "Cà phê"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Tra-sua")
def show_id_03():
    products = Product.query.all()
    category_id = 3
    category_name = "Trà sữa"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Smoothies")
def show_id_04():
    products = Product.query.all()
    category_id = 4
    category_name = "Smoothies"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Nuoc-ep")
def show_id_05():
    products = Product.query.all()
    category_id = 5
    category_name = "Nước ép"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Cocktail")
def show_id_06():
    products = Product.query.all()
    category_id = 6
    category_name = "Cocktail"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


@app.route("/Banh-ngot")
def show_id_07():
    products = Product.query.all()
    category_id = 7
    category_name = "Bánh ngọt"
    return render_template("products.html", products=products, category_id=category_id, category_name=category_name)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
