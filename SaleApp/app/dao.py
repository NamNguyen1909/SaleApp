# SaleApp/app/dao.py

from itertools import product

from app.models import Category,Product,User,Receipt,ReceiptDetails
from app import app, db
import hashlib
import cloudinary.uploader
from flask_login import current_user

def load_categories():
    return Category.query.order_by('id').all()
    # return [{
    #     "id": 1,
    #     "name": "Mobile"
    # }, {
    #     "id": 2,
    #     "name": "Tablet"
    # }, {
    #     "id": 3,
    #     "name": "Laptop"
    # }]


def load_products(kw=None,cate_id=None,page=1):
    query = Product.query

    if kw:
        query=query.filter(Product.name.contains(kw))  #Lọc sản phẩm có tên chứa từ khóa

    if cate_id:
        query=query.filter(Product.category_id==cate_id)  # Lọc sản phẩm thuộc danh mục

    page_size=app.config["PAGE_SIZE"]
    start=(page-1)*page_size
    query=query.slice(start,start+page_size) # Cắt ra phần tử từ start đến start + page_size

    return query.all() #trả về tất cả các sản phẩm phù hợp với các điều kiện trong truy vấn

def count_products():
    return Product.query.count()

# def load_products():
    # return [{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }, {
    #     "id": 2,
    #     "name": "iPad Pro 2020",
    #     "description": "Apple, 128GB, RAM: 6GB",
    #     "price": 37000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
    #     "category_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Galaxy Note 10 Plus",
    #     "description": "Samsung, 64GB, RAML: 6GB",
    #     "price": 24000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
    #     "category_id": 1
    # },{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }, {
    #     "id": 2,
    #     "name": "iPad Pro 2020",
    #     "description": "Apple, 128GB, RAM: 6GB",
    #     "price": 37000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
    #     "category_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Galaxy Note 10 Plus",
    #     "description": "Samsung, 64GB, RAML: 6GB",
    #     "price": 24000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
    #     "category_id": 1
    # },{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }, {
    #     "id": 2,
    #     "name": "iPad Pro 2020",
    #     "description": "Apple, 128GB, RAM: 6GB",
    #     "price": 37000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
    #     "category_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Galaxy Note 10 Plus",
    #     "description": "Samsung, 64GB, RAML: 6GB",
    #     "price": 24000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
    #     "category_id": 1
    # },{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }, {
    #     "id": 2,
    #     "name": "iPad Pro 2020",
    #     "description": "Apple, 128GB, RAM: 6GB",
    #     "price": 37000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
    #     "category_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Galaxy Note 10 Plus",
    #     "description": "Samsung, 64GB, RAML: 6GB",
    #     "price": 24000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
    #     "category_id": 1
    # },{
    #     "id": 1,
    #     "name": "iPhone 7 Plus",
    #     "description": "Apple, 32GB, RAM: 3GB, iOS13",
    #     "price": 17000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647056401/ipmsmnxjydrhpo21xrd8.jpg",
    #     "category_id": 1
    # }, {
    #     "id": 2,
    #     "name": "iPad Pro 2020",
    #     "description": "Apple, 128GB, RAM: 6GB",
    #     "price": 37000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1646729533/zuur9gzztcekmyfenkfr.jpg",
    #     "category_id": 2
    # }, {
    #     "id": 3,
    #     "name": "Galaxy Note 10 Plus",
    #     "description": "Samsung, 64GB, RAML: 6GB",
    #     "price": 24000000,
    #     "image": "https://res.cloudinary.com/dxxwcby8l/image/upload/v1647248722/r8sjly3st7estapvj19u.jpg",
    #     "category_id": 1
    # }]

def add_user(name,username,password,avatar=None):
    password = str(hashlib.md5(password.encode('utf-8')).hexdigest())
    # hoặc có thể set url avaatar mặc định ở đây thay vì models.User
    u=User(name=name,username=username,password=password)

    if avatar:
        res=cloudinary.uploader.upload(avatar)
        u.avatar=res.get("secure_url")
    db.session.add(u)
    db.session.commit()

def auth_user(username,password,role=None):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    u= User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password))
    if role:
        u=u.filter(User.user_role.__eq__(role))

    return u.first()

def get_user_by_id(id):
    return User.query.get(id)

def add_receipt(cart):
    if cart:
        r=Receipt(user=current_user)
#       user nằm trong backrep
        db.session.add(r)

        for c in cart.values():
            d=ReceiptDetails(quantity=c['quantity'],unit_price=['price'],
                             product_id=c['id'],receipt=r)
            db.session.add()

        db.session.commit()
