# from application import db
# from sqlalchemy.orm import relationship
from application.utils.models import BaseModel, db
from werkzeug.security import generate_password_hash, check_password_hash


class Book(BaseModel):
    __tablename__  = 'b_data'
    id = db.Column(db.Integer, primary_key=True, comment='主键ID')
    img_name = db.Column(db.String(50), comment="书封面")
    book_name = db.Column(db.String(50), comment='书名')
    author = db.Column(db.String(50), comment='作者名')
    book_type = db.Column(db.String(50), comment='小说类型')
    book_byte = db.Column(db.String(255), comment='小说字数')
    brief_introduction = db.Column(db.String(255), comment='小说简介')
    books_text = db.relationship('Book_text', backref='b_data')
    def __repr__(self):
        return self.book_name

class Book_text(BaseModel):
    __tablename__ = 'b_text'
    id = db.Column(db.Integer, primary_key=True, comment='主键ID')
    book_chapter = db.Column(db.String(50), comment='章节名')
    chapter_text = db.Column(db.Text(), comment='章节内容')
    book_data_id = db.Column(db.Integer,db.ForeignKey('b_data.id'))


# class User(db.Model):
#     __tablename__ = "mf_users"
#     id = db.Column(db.Integer, primary_key=True, comment="主键ID")
#     name = db.Column(db.String(255), unique=True, comment="账户名")
#     password = db.Column(db.String(255), comment="登录密码")
#     ip_address = db.Column(db.String(255), index=True, comment="登录IP")
#
#     def __repr__(self):
#         return self.name
