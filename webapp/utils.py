import hashlib

from sqlalchemy import func

from webapp import db
from webapp.models import User, Product, Category


def get_user_by_id(user_id):
    return User.query.get(user_id)


def get_category_by_id(category_id):
    return Category.query.get(category_id)


def check_login(username, password):
    if username and password:
        password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

        return User.query.filter(User.username.__eq__(username.strip()),
                                 User.password.__eq__(password),
                                 ).first()
    return None


def product_count_by_cate():
    return Category.query.join(Product, Product.category_id.__eq__(Category.id), isouter=True) \
        .add_column(func.count(Product.id)).group_by(Category.id).all()


def add_user(new_account, **kwargs):
    new_account["password"] = str(hashlib.md5(new_account["password"].strip().encode("utf-8")).hexdigest())
    user = User(name=new_account["name"].strip(),
                email=new_account["email"].strip(),
                phone_number=new_account["phone_number"],
                address=new_account["address"],
                username=new_account["username"].strip(),
                password=new_account["password"].strip()
                )
    db.session.add(user)
    db.session.commit()
