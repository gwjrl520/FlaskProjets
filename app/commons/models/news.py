from uuid import uuid4

from commons.settings.extensions import db
from commons.models.basemodel import BaseModel


class Channel(BaseModel):
    """
    新闻频道
    """
    __tablename__ = 'channel'

    channel_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='频道ID')
    name = db.Column(db.String, doc='频道名称')
    sequence = db.Column(db.Integer, default=0, doc='序号')
    is_visible = db.Column(db.Boolean, default=False, doc='是否可见')
    is_default = db.Column(db.Boolean, default=False, doc='是否默认')


class Article(BaseModel):
    """
    文章基本信息表
    """
    __tablename__ = 'article'

    class STATUS:
        DRAFT = 0  # 草稿
        UNREVIEWED = 1  # 待审核
        APPROVED = 2  # 审核通过
        FAILED = 3  # 审核失败
        DELETED = 4  # 已删除
        BANNED = 5  # 封禁

    STATUS_ENUM = [0, 1, 2, 3]

    article_id = db.Column(db.Integer, default=uuid4, primary_key=True,  doc='文章ID')
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), doc='用户ID')
    channel_id = db.Column(db.Integer, db.ForeignKey('channel.channel_id'), doc='频道ID')
    title = db.Column(db.String, doc='标题')
    cover = db.Column(db.JSON, doc='封面')
    is_advertising = db.Column(db.Boolean, default=False, doc='是否投放广告')
    status = db.Column(db.Integer, default=0, doc='帖文状态')
    reviewer_id = db.Column(db.Integer, doc='审核人员ID')
    review_time = db.Column(db.DateTime, doc='审核时间')
    delete_time = db.Column(db.DateTime, doc='删除时间')
    comment_count = db.Column(db.Integer, default=0, doc='评论数')
    allow_comment = db.Column(db.Boolean, default=True, doc='是否允许评论')
    reject_reason = db.Column(db.String, doc='驳回原因')
    content = db.relationship('ArticleContent', uselist=False)
    user = db.relationship('User', uselist=False)
    channel = db.relationship('Channel', uselist=False)


class ArticleContent(BaseModel):
    """
    文章内容表
    """
    __tablename__ = 'article_content'

    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), primary_key=True, doc='文章ID')
    content = db.Column(db.Text, doc='帖文内容')


class Collection(BaseModel):
    """
    用户收藏表
    """
    __tablename__ = 'news_collection'

    collection_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    article_id = db.Column(db.Integer, doc='文章ID')
    is_deleted = db.Column(db.Boolean, default=False, doc='是否删除')


class Attitude(BaseModel):
    """
    用户文章态度表
    """
    __tablename__ = 'news_attitude'

    class ATTITUDE:
        DISLIKE = 0  # 不喜欢
        LIKING = 1  # 点赞

    attitude_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    article_id = db.Column(db.Integer, doc='文章ID')
    attitude = db.Column(db.Boolean, doc='态度')
    article = db.relationship('Article', uselist=False)


class Report(BaseModel):
    """
    文章举报
    """
    __tablename__ = 'news_report'

    TYPE_LIST = (0, 1, 2, 3, 4, 5, 6, 7, 8)

    class TYPE:
        OTHER = 0

    report_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    article_id = db.Column(db.Integer, doc='文章ID')
    type = db.Column(db.Integer, doc='问题类型')
    remark = db.Column(db.String, doc='备注问题')


class Comment(BaseModel):
    """
    文章评论
    """
    __tablename__ = 'news_comment'

    class STATUS:
        UNREVIEWED = 0  # 待审核
        APPROVED = 1  # 审核通过
        FAILED = 2  # 审核失败
        DELETED = 3  # 已删除

    comment_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='评论ID')
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), doc='用户ID')
    article_id = db.Column(db.Integer, db.ForeignKey('article.article_id'), doc='文章ID')
    parent_id = db.Column(db.Integer, doc='被评论的评论id')
    like_count = db.Column(db.Integer, default=0, doc='点赞数')
    reply_count = db.Column(db.Integer, default=0, doc='回复数')
    content = db.Column(db.String, doc='评论内容')
    is_top = db.Column(db.Boolean, default=False, doc='是否置顶')
    status = db.Column(db.Integer, default=1, doc='评论状态')

    user = db.relationship('User', uselist=False)
    article = db.relationship('Article', uselist=False)


class CommentLiking(BaseModel):
    """
    评论点赞
    """
    __tablename__ = 'news_comment_liking'

    liking_id = db.Column(db.Integer, default=uuid4, primary_key=True, doc='主键ID')
    user_id = db.Column(db.Integer, doc='用户ID')
    comment_id = db.Column(db.Integer, doc='评论ID')
    is_deleted = db.Column(db.Boolean, default=False, doc='是否删除')