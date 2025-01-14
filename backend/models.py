from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    date = db.Column(db.Date, default=datetime.utcnow)
    role = db.Column(db.String(100))
    company = db.Column(db.String(100))
    status = db.Column(db.String(20))  # "Yes", "No", or "Pending"

    def to_dict(self):
        return {
            "id": self.id,
            "date": self.date,
            "role": self.role,
            "company": self.company,
            "status": self.status
        }
