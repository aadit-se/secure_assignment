# from project import db
from project import app

# class GroupVo(db.Model):
#     __tablename__ = 'goupMaster'
#     GroupId = db.Column('GroupId', db.Integer, primary_key = True)
#     GroupName = db.Column('GroupName',db.String(100))
#     AdminId = db.Column(db.Integer,nullable=False)
#     Status=db.Column('Status',db.Boolean)
#     AdminName= db.Column('AdminName',db.String(50))
# with app.app_context():
#     db.create_all()

from project import cur
from project import con
cur.execute('''
    CREATE TABLE IF NOT EXISTS goupMaster
    (GroupId integer primary key AUTOINCREMENT,
    GroupName varchar(100),
    AdminId integer NOT NULL,
    Status boolean NOT NULL,
    AdminName integer NOT NULL,
    FOREIGN KEY (AdminId) REFERENCES User(UserId))''')

class GroupVo():
    def __init__(self,GroupId=None,GroupName=None,AdminId=None,Status=None,AdminName=None):
        self.GroupId = GroupId
        self.GroupName = GroupName
        self.AdminId = AdminId
        self.Status=Status
        self.AdminName= AdminName

con.commit()

