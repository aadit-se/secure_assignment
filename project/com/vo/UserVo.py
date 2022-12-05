# from project import db
from project import app

# class UserVo(db.Model):
#     __tablename__ = 'user'
#     UserId = db.Column('UserId', db.Integer, primary_key = True)
#     FirstName = db.Column('FirstName',db.String(100))
#     Emaild=db.Column('Emaild',db.String(100))
#     LastName = db.Column('LastName',db.String(100))
#     UserName = db.Column('UserName',db.String(50))  
#     Password = db.Column('Password',db.String(200))
#     GroupOwner = db.Column('GroupOwner',db.Integer)
#     InGroup = db.Column('InGroup',db.String(100))
#     # 0=user
#     # 1=admin
#     Role=db.Column('Role',db.Boolean)
#     # 0=not approved
#     # 1=approved
#     Status=db.Column('Status',db.Boolean)


# with app.app_context():
#     db.create_all()

from project import cur
from project import con
cur.execute('''
    CREATE TABLE IF NOT EXISTS User
    (UserId integer primary key AUTOINCREMENT,
    FirstName  varchar(100),
    Emaild varchar(200),
    LastName varchar(100),
    Status boolean,
    UserName varchar(100),
    Password varchar(200),
    GroupOwner integer,
    InGroup varchar(100),
    Role boolean)''')

class UserVo():
    def __init__(self,UserId='Null',FirstName='Null',Emaild='Null',LastName='Null',Status =0,UserName='Null',Password ='Null',GroupOwner='Null',InGroup='Null',Role=0):
        self.UserId = UserId
        self.FirstName=FirstName
        self.Emaild=Emaild
        self.LastName=LastName
        self.Status=Status
        self.UserName=UserName
        self.Password=Password
        self.GroupOwner=GroupOwner
        self.InGroup=InGroup
        self.Role=Role
        
con.commit()
