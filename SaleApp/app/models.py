# models.py

from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String, Float, ForeignKey, Boolean,Enum
from app import db,app
import hashlib
from enum import Enum as RoleEnum
from flask_login import UserMixin

class UserRole(RoleEnum):
    ADMIN=1
    USER=2

class User(db.Model,UserMixin):
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String(100),nullable=False)
    username=Column(String(100),nullable=False,unique=True)
    password=Column(String(100),nullable=False)
    avatar=Column(String(100),nullable=True,default='https://res.cloudinary.com/ds05mb5xf/image/upload/v1730272507/cld-sample-4.jpg')
    active=Column(Boolean,default=True)
    user_role=Column(Enum(UserRole),default=UserRole.USER)


class Category(db.Model):
    # --tablename__='cate' #khi muon table ten khac
    id=Column(Integer,primary_key=True,autoincrement=True)
    name =Column(String(50),nullable=False,unique=True)
    products = relationship('Product',backref = 'category', lazy = True)

    def __str__(self):
        return self.name

class Product(db.Model):
    id=Column(Integer,primary_key=True,autoincrement=True)
    name =Column(String(50),nullable=False,unique=True)
    description=Column(String(255),nullable=True)
    price=Column(Float,default=0)
    image=Column(String(500),nullable=True)
    category_id=Column(Integer,ForeignKey(Category.id),nullable=False)

    def __str__(self):
        return self.name


if __name__=='__main__':
    with app.app_context():
        # pass
        db.create_all()                 #chay de tao db

        # u=User(name="admin",username="admin",password=str(hashlib.md5("123456".encode('utf-8')).hexdigest()),
        #        avatar="https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
        #        user_role=UserRole.ADMIN)
        # db.session.add(u)
        # db.session.commit()
        #
        # c1=Category(name='Mobile')
        # c2=Category(name='Tablet')
        # c3=Category(name='Desktop')
        #
        # db.session.add_all([c1,c2,c3])
        # db.session.commit()

        data = [
            {"id": 1, "name": "iPhone 12 Plus", "description": "Apple, 32GB, RAM: 3GB, iOS13", "price": 17000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 2, "name": "iPad Pro 2024", "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 3, "name": "Galaxy Note 17 Plus", "description": "Samsung, 64GB, RAM: 6GB", "price": 24000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 4, "name": "iPhone 9 Plus", "description": "Apple, 32GB, RAM: 3GB, iOS13", "price": 17000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 5, "name": "iPad Pro 2022", "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 6, "name": "Galaxy Note 12 Plus", "description": "Samsung, 64GB, RAM: 6GB", "price": 24000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 7, "name": "iPhone 10 Plus", "description": "Apple, 32GB, RAM: 3GB, iOS13", "price": 17000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 8, "name": "iPad Pro 2023", "description": "Apple, 128GB, RAM: 6GB", "price": 37000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 9, "name": "Galaxy Note 13 Plus", "description": "Samsung, 64GB, RAM: 6GB", "price": 24000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 10, "name": "iPhone 12 Mini", "description": "Apple, 64GB, RAM: 4GB, iOS14", "price": 18000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 11, "name": "iPad Air 2025", "description": "Apple, 256GB, RAM: 6GB", "price": 40000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 12, "name": "Galaxy S20 Ultra", "description": "Samsung, 128GB, RAM: 12GB", "price": 29000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 13, "name": "iPhone 11 Pro Max", "description": "Apple, 256GB, RAM: 4GB, iOS13", "price": 22000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 14, "name": "iPad Mini 2024", "description": "Apple, 64GB, RAM: 4GB", "price": 22000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 15, "name": "Galaxy Z Fold 2", "description": "Samsung, 256GB, RAM: 12GB", "price": 35000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 16, "name": "iPhone 13", "description": "Apple, 128GB, RAM: 6GB, iOS14", "price": 21000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 17, "name": "iPad Pro 2021", "description": "Apple, 512GB, RAM: 6GB", "price": 50000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 18, "name": "Galaxy Note 20 Ultra", "description": "Samsung, 128GB, RAM: 8GB", "price": 28000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 19, "name": "iPhone 14 Pro", "description": "Apple, 128GB, RAM: 6GB, iOS15", "price": 25000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 20, "name": "iPad Pro 2026", "description": "Apple, 1TB, RAM: 8GB", "price": 65000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
             "category_id": 2},  # Tablet
            {"id": 21, "name": "Galaxy Z Flip 3", "description": "Samsung, 256GB, RAM: 8GB", "price": 32000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
             "category_id": 1},  # Mobile
            {"id": 22, "name": "iPhone SE", "description": "Apple, 64GB, RAM: 4GB", "price": 14000000,
             "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
             "category_id": 1},  # Mobile
            {"id": 23, "name": "MacBook Pro M1", "description": "Apple, 512GB SSD, RAM: 16GB", "price": 45000000,
             "image": "https://res.cloudinary.com/ds05mb5xf/image/upload/v1732090562/capture_1666429395_1667548641_ycdy6u.png",
             "category_id": 3},  # Desktop
            {"id": 24, "name": "MacBook Air M2", "description": "Apple, 256GB SSD, RAM: 8GB", "price": 35000000,
             "image": "https://res.cloudinary.com/ds05mb5xf/image/upload/v1732090517/111867_SP869-2022-macbook-air-m2-colors_rrcpuh.png",
             "category_id": 3},  # Desktop
            {"id": 25, "name": "Surface Laptop 4", "description": "Microsoft, 256GB SSD, RAM: 8GB", "price": 32000000,
             "image": "https://res.cloudinary.com/ds05mb5xf/image/upload/v1732090456/Surface-Laptop-4-1_idshmc.jpg",
             "category_id": 3},  # Desktop
            {"id": 26, "name": "Dell XPS 13", "description": "Dell, 512GB SSD, RAM: 16GB", "price": 47000000,
             "image": "https://res.cloudinary.com/ds05mb5xf/image/upload/v1732090389/notebook-xps-13-9345-t-gray-gallery-4_pmv5gg.avif",
             "category_id": 3},  # Desktop
            {"id": 27, "name": "Mac Pro 2023", "description": "Apple, 1TB SSD, RAM: 32GB", "price": 100000000,
             "image": "https://res.cloudinary.com/ds05mb5xf/image/upload/v1732088759/111340_macbook-pro-2023-14in_ou0cpb.png",
             "category_id": 3}  # Desktop
        ]


        # Add products to the database
        for p in data:
            prod = Product(name=p['name'], description=p['description'], price=p['price'],
                           image=p['image'], category_id=p['category_id'])
            db.session.add(prod)

        db.session.commit()

