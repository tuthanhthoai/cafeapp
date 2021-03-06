from datetime import datetime
from enum import Enum as UserEnum
from flask_login import UserMixin
from sqlalchemy import (
    Column, Integer, String, Float, Boolean, DateTime, ForeignKey, Enum)
from sqlalchemy.orm import relationship, backref
from webapp import db


class UserRole(UserEnum):
    ADMIN = 2
    USER = 1


class User(db.Model, UserMixin):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    email = Column(String(100), default="")
    phone_number = Column(String(20), default="")
    address = Column(String(20), default="")
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    active = Column(Boolean, default=True)
    joined_date = Column(DateTime, default=datetime.now())
    avatar = Column(String(100))
    user_role = Column(Enum(UserRole), default=UserRole.USER)

    def __str__(self):
        return self.name


class Category(db.Model):
    __tablename__ = "category"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
    products = relationship("Product", backref="category", lazy=True)

    # relationship("ClassName", backref="TableName", lazy=)

    def __str__(self):
        return self.name


class Product(db.Model):
    __tablename__ = "product"

    id = Column(Integer, primary_key=True, autoincrement=True)
    category_id = Column(Integer, ForeignKey("category.id"), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(200))
    price = Column(Float, default=0)
    active = Column(Boolean, default=True)
    image = Column(String(100))
    created_date = Column(DateTime, default=datetime.now())
    tags = relationship("Tag", secondary="product_tag", lazy="subquery",
                        backref=backref("products", lazy=True))


Product_tag = db.Table("product_tag",
                       Column("product_id", Integer, ForeignKey("product.id"), primary_key=True),
                       Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True))


class Tag(db.Model):
    __tablename__ = "tag"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=True, unique=True)


class Order(db.Model):
    __tablename__ = "order"
    id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.id"), nullable=False)
    order_date = Column(DateTime, default=datetime.now())


if __name__ == '__main__':
    db.create_all()

    # # Category
    # db.session.add(Category(name="Tr?? hoa qu???"))
    # db.session.add(Category(name="C?? ph??"))
    # db.session.add(Category(name="Tr?? s???a"))
    # db.session.add(Category(name="Smoothies"))
    # db.session.add(Category(name="N?????c ??p"))
    # db.session.add(Category(name="Cocktail"))
    # db.session.add(Category(name="B??nh ng???t"))
    # db.session.commit()
    #
    # # Product
    # db.session.add(Product(category_id=1, name="Tr?? c??c b???n t???", price=40000, image="image/products/p1.png"))
    # db.session.add(Product(category_id=1, name="Tr?? vi???t qu???t", price=40000, image="image/products/p2.png"))
    # db.session.add(Product(category_id=1, name="Tr?? v???i", price=40000, image="image/products/p3.png"))
    # db.session.add(Product(category_id=1, name="Tr?? d??u t??y", price=40000, image="image/products/p4.png"))
    # db.session.add(Product(category_id=1, name="Tr?? cam ????o", price=45000, image="image/products/p5.png"))
    # db.session.add(Product(category_id=1, name="Tr?? xo??i", price=35000, image="image/products/p6.png"))
    # db.session.add(Product(category_id=1, name="Tr?? t??o", price=35000, image="image/products/p7.png"))
    # db.session.add(Product(category_id=1, name="Tr?? chanh", price=35000, image="image/products/p8.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? ??en", price=30000, image="image/products/p9.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? s???a", price=35000, image="image/products/p10.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? tr???ng", price=45000, image="image/products/p11.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? Cococcino Latte", price=50000, image="image/products/p12.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? Cappuccino", price=65000, image="image/products/p13.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? Espresso", price=65000, image="image/products/p14.png"))
    # db.session.add(Product(category_id=2, name="C?? ph?? Mocha", price=50000, image="image/products/p15.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a tr??n ch??u", price=55000, image="image/products/p16.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a d??u t??y", price=50000, image="image/products/p17.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a khoai m??n", price=50000, image="image/products/p18.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a b???c h??", price=50000, image="image/products/p19.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a Kiwi", price=60000, image="image/products/p20.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a Gong Cha", price=80000, image="image/products/p21.png"))
    # db.session.add(
    #     Product(category_id=3, name="Tr?? s???a Oreo Chocolate Cream", price=70000, image="image/products/p22.png"))
    # db.session.add(
    #     Product(category_id=3, name="Tr?? s???a tr??n ch??u ???????ng ??en", price=55000, image="image/products/p23.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a s????ng s??o", price=50000, image="image/products/p24.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a vanila", price=50000, image="image/products/p25.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a c?? ph??", price=50000, image="image/products/p26.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a ?? long", price=50000, image="image/products/p27.png"))
    # db.session.add(Product(category_id=3, name="Tr?? s???a matcha", price=50000, image="image/products/p28.png"))
    # db.session.add(Product(category_id=4, name="Smoothies chu???i d???a", price=55000, image="image/products/p29.png"))
    # db.session.add(Product(category_id=4, name="Smoothies d??u vi???t qu???t", price=55000, image="image/products/p30.png"))
    # db.session.add(Product(category_id=4, name="Smoothies d??u", price=55000, image="image/products/p31.png"))
    # db.session.add(Product(category_id=4, name="Smoothies d??u chu???i", price=55000, image="image/products/p32.png"))
    # db.session.add(Product(category_id=4, name="Smoothies b???c h??", price=60000, image="image/products/p33.png"))
    # db.session.add(Product(category_id=4, name="Smoothies chanh d??y", price=80000, image="image/products/p34.png"))
    # db.session.add(Product(category_id=5, name="N?????c ??p d???a", price=60000, image="image/products/p35.png"))
    # db.session.add(Product(category_id=5, name="N?????c ??p t??o", price=50000, image="image/products/p36.png"))
    # db.session.add(Product(category_id=5, name="N?????c ??p cam", price=55000, image="image/products/p37.png"))
    # db.session.add(Product(category_id=5, name="N?????c ??p d??a h???u", price=50000, image="image/products/p38.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Bacardi", price=140000, image="image/products/p39.png"))
    # db.session.add(Product(category_id=6, name="Cocktail First Aid", price=150000, image="image/products/p40.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Puszta", price=130000, image="image/products/p41.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Matcha Hai", price=125000, image="image/products/p42.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Chapman", price=135000, image="image/products/p43.png"))
    # db.session.add(Product(category_id=7, name="B??nh Flan", price=15000, image="image/products/p44.png"))
    # db.session.add(Product(category_id=7, name="B??nh c?? ph?? phomai", price=25000, image="image/products/p45.png"))
    # db.session.add(
    #     Product(category_id=7, name="B??nh b??ng lan cu???n tr?? xanh", price=25000, image="image/products/p46.png"))
    # db.session.add(Product(category_id=7, name="B??nh su kem", price=8000, image="image/products/p47.png"))
    # db.session.add(Product(category_id=7, name="B??nh r??n Dorayaki", price=15000, image="image/products/p48.png"))
    # db.session.add(Product(category_id=7, name="Pancake", price=25000, image="image/products/p49.png"))
    # db.session.add(Product(category_id=7, name="Cheesecake", price=25000, image="image/products/p50.png"))
    # db.session.commit()

    # Tag
    db.session.add(Tag(name="new"))
    db.session.add(Tag(name="promotion"))
    db.session.commit()

    # User
    db.session.add(User(name="admin", username="admin", password="1a6b83c06b85f3c579742923a1295fa3", user_role="ADMIN"))
    db.session.commit()
