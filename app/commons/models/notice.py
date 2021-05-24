from uuid import uuid4

from commons.models.basemodel import BaseModel
from commons.settings.extensions import db


class Announcement(BaseModel):
    """
    系统公告表
    """
    __tablename__ = 'global_announcement'

    class STATUS:
        UNPUBLISHED = 0  # 待发布
        PUBLISHED = 1  # 已发布
        OBSELETE = 2  # 已撤下

    announcement_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='公告ID')
    title = db.Column(db.String, doc='标题')
    content = db.Column(db.Text, doc='正文')
    status = db.Column(db.Integer, default=0, doc='状态')
    pubtime = db.Column('publish_time', db.DateTime, doc='发布时间')


class SensitiveWord(BaseModel):
    """
    敏感词
    """
    __tablename__ = 'recommend_sensitive_word'

    sens_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='敏感词id')
    word = db.Column(db.String, doc='敏感词')
    weights = db.Column(db.Integer, doc='权重')
    hold_count = db.Column(db.Integer, doc='拦截次数')
    

class Word(BaseModel):
    """
    单词
    """
    __tablename__ = 'word'

    word_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='id')
    word = db.Column(db.String, doc='英文')
    fanyi = db.Column(db.Integer, doc='翻译')
