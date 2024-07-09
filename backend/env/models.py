from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Crop(db.Model):
    __tablename__ = 'crop'  # Đặt tên bảng là 'crop'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    conditions = db.Column(db.String(200))
    care = db.Column(db.String(500))
    harvest_time = db.Column(db.String(200))
    fertilization = db.Column(db.String(500))

class Weather(db.Model):
    __tablename__ = 'weather'  # Đặt tên bảng là 'weather'

    id = db.Column(db.Integer, primary_key=True)
    temperature = db.Column(db.Float)
    humidity = db.Column(db.Float)
    rainfall = db.Column(db.Float)
    light = db.Column(db.Float)
