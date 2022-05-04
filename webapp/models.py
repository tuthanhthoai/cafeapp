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
    # db.session.add(Category(name="Trà hoa quả"))
    # db.session.add(Category(name="Cà phê"))
    # db.session.add(Category(name="Trà sữa"))
    # db.session.add(Category(name="Smoothies"))
    # db.session.add(Category(name="Nước ép"))
    # db.session.add(Category(name="Cocktail"))
    # db.session.add(Category(name="Bánh ngọt"))
    # db.session.commit()
    #
    # # Product
    # db.session.add(Product(category_id=1, name="Trà cúc bồn tử", price=40000, image="image/products/p1.png"))
    # db.session.add(Product(category_id=1, name="Trà việt quất", price=40000, image="image/products/p2.png"))
    # db.session.add(Product(category_id=1, name="Trà vải", price=40000, image="image/products/p3.png"))
    # db.session.add(Product(category_id=1, name="Trà dâu tây", price=40000, image="image/products/p4.png"))
    # db.session.add(Product(category_id=1, name="Trà cam đào", price=45000, image="image/products/p5.png"))
    # db.session.add(Product(category_id=1, name="Trà xoài", price=35000, image="image/products/p6.png"))
    # db.session.add(Product(category_id=1, name="Trà táo", price=35000, image="image/products/p7.png"))
    # db.session.add(Product(category_id=1, name="Trà chanh", price=35000, image="image/products/p8.png"))
    # db.session.add(Product(category_id=2, name="Cà phê đen", price=30000, image="image/products/p9.png"))
    # db.session.add(Product(category_id=2, name="Cà phê sữa", price=35000, image="image/products/p10.png"))
    # db.session.add(Product(category_id=2, name="Cà phê trứng", price=45000, image="image/products/p11.png"))
    # db.session.add(Product(category_id=2, name="Cà phê Cococcino Latte", price=50000, image="image/products/p12.png"))
    # db.session.add(Product(category_id=2, name="Cà phê Cappuccino", price=65000, image="image/products/p13.png"))
    # db.session.add(Product(category_id=2, name="Cà phê Espresso", price=65000, image="image/products/p14.png"))
    # db.session.add(Product(category_id=2, name="Cà phê Mocha", price=50000, image="image/products/p15.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa trân châu", price=55000, image="image/products/p16.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa dâu tây", price=50000, image="image/products/p17.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa khoai môn", price=50000, image="image/products/p18.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa bạc hà", price=50000, image="image/products/p19.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa Kiwi", price=60000, image="image/products/p20.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa Gong Cha", price=80000, image="image/products/p21.png"))
    # db.session.add(
    #     Product(category_id=3, name="Trà sữa Oreo Chocolate Cream", price=70000, image="image/products/p22.png"))
    # db.session.add(
    #     Product(category_id=3, name="Trà sữa trân châu đường đen", price=55000, image="image/products/p23.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa sương sáo", price=50000, image="image/products/p24.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa vanila", price=50000, image="image/products/p25.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa cà phê", price=50000, image="image/products/p26.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa ô long", price=50000, image="image/products/p27.png"))
    # db.session.add(Product(category_id=3, name="Trà sữa matcha", price=50000, image="image/products/p28.png"))
    # db.session.add(Product(category_id=4, name="Smoothies chuối dừa", price=55000, image="image/products/p29.png"))
    # db.session.add(Product(category_id=4, name="Smoothies dâu việt quất", price=55000, image="image/products/p30.png"))
    # db.session.add(Product(category_id=4, name="Smoothies dâu", price=55000, image="image/products/p31.png"))
    # db.session.add(Product(category_id=4, name="Smoothies dâu chuối", price=55000, image="image/products/p32.png"))
    # db.session.add(Product(category_id=4, name="Smoothies bạc hà", price=60000, image="image/products/p33.png"))
    # db.session.add(Product(category_id=4, name="Smoothies chanh dây", price=80000, image="image/products/p34.png"))
    # db.session.add(Product(category_id=5, name="Nước ép dứa", price=60000, image="image/products/p35.png"))
    # db.session.add(Product(category_id=5, name="Nước ép táo", price=50000, image="image/products/p36.png"))
    # db.session.add(Product(category_id=5, name="Nước ép cam", price=55000, image="image/products/p37.png"))
    # db.session.add(Product(category_id=5, name="Nước ép dưa hấu", price=50000, image="image/products/p38.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Bacardi", price=140000, image="image/products/p39.png"))
    # db.session.add(Product(category_id=6, name="Cocktail First Aid", price=150000, image="image/products/p40.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Puszta", price=130000, image="image/products/p41.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Matcha Hai", price=125000, image="image/products/p42.png"))
    # db.session.add(Product(category_id=6, name="Cocktail Chapman", price=135000, image="image/products/p43.png"))
    # db.session.add(Product(category_id=7, name="Bánh Flan", price=15000, image="image/products/p44.png"))
    # db.session.add(Product(category_id=7, name="Bánh cà phê phomai", price=25000, image="image/products/p45.png"))
    # db.session.add(
    #     Product(category_id=7, name="Bánh bông lan cuộn trà xanh", price=25000, image="image/products/p46.png"))
    # db.session.add(Product(category_id=7, name="Bánh su kem", price=8000, image="image/products/p47.png"))
    # db.session.add(Product(category_id=7, name="Bánh rán Dorayaki", price=15000, image="image/products/p48.png"))
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
