# from project import db
from project import app

# class UserGroupVo(db.Model):
#     __tablename__ = 'UserGroup'
#     GroupId = db.Column(db.Integer, db.ForeignKey('goupMaster.GroupId', ondelete='CASCADE'),primary_key=True)
#     GroupName = db.Column('GroupName',db.String(100))
#     UserId = db.Column(db.Integer,primary_key=True)
#     AdminId = db.Column(db.Integer,nullable=False)
#     Status=db.Column('Status',db.Boolean)
#     UserName = db.Column('UserName',db.String(50))  

# with app.app_context():
#     db.create_all()

from project import cur
from project import con
cur.execute('''
    CREATE TABLE IF NOT EXISTS UserGroup
    (GroupId integer,
    GroupName  varchar(100),
    UserId integer,
    Status boolean,
    AdminId integer,
    UserName varchar(100),
    PRIMARY KEY (GroupId,UserId)
    FOREIGN KEY (GroupId) REFERENCES goupMaster(GroupId),
    FOREIGN KEY (UserId) REFERENCES User(UserId),
    FOREIGN KEY (AdminId) REFERENCES User(UserId))''')

class UserGroupVo():
    def __init__(self,GroupId=None,GroupName=None,UserId=None,Status =None,AdminId =None,UserName=None):
        self.GroupId = GroupId
        self.GroupName = GroupName
        self.AdminId= AdminId
        self.Status=Status
        self.UserName=UserName
        self.UserId=UserId
con.commit()
