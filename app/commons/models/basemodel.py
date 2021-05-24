from datetime import datetime

from commons.settings.extensions import db


class BaseModel(db.Model):
    __abstract__ = True
    create_time = db.Column(db.DateTime, default=datetime.now, doc='创建时间')
    update_time = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now, doc='更新时间')

    def get(self):
        db.session.get(self)
        db.session.commit()

    def add(self):
        db.session.add(self)
        db.session.commit()
    
    def update(self):
        db.session.update(self)
        db.session.commit()
    
    def delete(self):
        db.session.delete(self)
        db.session.commit()