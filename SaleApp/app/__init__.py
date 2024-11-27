# __init.py__

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from urllib.parse import quote
import cloudinary
from flask_login import LoginManager

app = Flask(__name__)

app.secret_key='SDFKJFLHJKSDHF98Y235IU43Y578RF984I53801Y8NDF' # THÊM KEY(tự định nghĩa)để mã hóa session ĐỂ FIX RuntimeError: The session is unavailable because no secret key was set.  Set the secret_key on the application to something unique and secret.

# app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" %quote("Admin@123")
app.config["SQLALCHEMY_DATABASE_URI"] ="mysql+pymysql://root:%s@localhost/saledb?charset=utf8mb4" %quote("ThanhNam*1909")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

app.config["PAGE_SIZE"]=8
db = SQLAlchemy(app)

cloudinary.config(cloud_name='ds05mb5xf',
                  api_key='129254722258642',
                  api_secret='OQScAUMjqFmA3g6gog1GfBRCM14')

login=LoginManager(app)

