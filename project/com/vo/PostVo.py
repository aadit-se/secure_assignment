# from project import db
from project import app
from project import cur
from project import con
# from project.com.vo import groupVo

# groupObj =groupVo()
# class PostVo(db.Model):
#     __tablename__ = 'postMaster'
#     PostId=db.Column('PostId', db.Integer, primary_key = True)
#     GroupId = db.Column('GroupId', db.Integer,nullable=False)
#     GroupName = db.Column('GroupName', db.Integer,nullable=False)
#     CreatorId = db.Column(db.Integer,nullable=False)
#     type=db.Column('type',db.String(100))
#     createdTime=db.Column(db.DateTime(timezone=True))
#     Status=db.Column('Status',db.Boolean)
#     AdminId = db.Column('AdminId',db.Integer,nullable=False)
#     UserName = db.Column('UserName',db.String(50))  
#     PostDescription=db.Column('PostDescription',db.String(500))

# with app.app_context():
#     db.create_all()

cur.execute('''
    CREATE TABLE IF NOT EXISTS postMaster
    (PostId integer primary key AUTOINCREMENT,
    GroupId integer,
    GroupName  varchar(100),
    CreatorId integer,
    type varchar(100),
    createdTime datetime, 
    Status boolean,
    AdminId integer,
    UserName varchar(100),
    PostDescription varchar(100))''')

class PostVo():
    def __init__(self,PostId=None,GroupId=None,GroupName=None,CreatorId=None,type=None,createdTime=None,Status =None,AdminId =None,UserName =None, PostDescription=None):
        self.PostId=PostId
        self.GroupId = GroupId
        self.GroupName = GroupName
        self.CreatorId = CreatorId
        self.type=type
        self.AdminId= AdminId
        self.createdTime=createdTime
        self.Status=Status
        self.UserName=UserName
        self.PostDescription=PostDescription
con.commit()

