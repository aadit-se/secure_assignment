# from project import db
from project import app

from project import cur
from project import con
cur.execute('''
    CREATE TABLE IF NOT EXISTS CommentVo
    (commentId integer primary key AUTOINCREMENT,
    commentDescription varchar(100),
    PostId integer NOT NULL,
    GroupId integer NOT NULL,
    CommentTime datetime NOT NULL,
    CommentorId integer NOT NULL,
    UserName varchar(50) NOT NULL,
    FOREIGN KEY (GroupId) REFERENCES goupMaster(GroupId),
    FOREIGN KEY (PostId) REFERENCES postMaster(PostId),
    FOREIGN KEY (CommentorId) REFERENCES User(UserId))''')

# class CommentVo():
#     __tablename__ = 'CommentVo'
#     commentId=db.Column('commentId',db.Integer, primary_key = True)
#     commentDescription = db.Column('commentDescription',db.String(100))
#     PostId=db.Column('PostId',db.Integer)
#     CommentTime=db.Column('comment time',db.DateTime(timezone=True))
#     CommentorId=db.Column('CommentorId',db.Integer)
#     UserName = db.Column('UserName',db.String(50))  

class CommentVo():
    def __init__(self,commentId=None,commentDescription=None,PostId=None,CommentTime=None,CommentorId=None,UserName=None):
        self.commentId=commentId
        self.commentDescription = commentDescription
        self.PostId=PostId
        self.CommentTime=CommentTime
        self.CommentorId=CommentorId
        self.UserName = UserName
con.commit()


# with app.app_context():
#     db.create_all()


