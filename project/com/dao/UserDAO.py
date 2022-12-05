# from project import db
from project.com.vo.UserVo import UserVo
import sqlite3
from project import con
from project import cur


def ansToPostVo(ans):
    vo=UserVo(ans[0],ans[1],ans[2],ans[3],ans[4] ,ans[5] ,ans[6],ans[7],ans[8],ans[9])
    return vo

class UserDAO:
    def addUser(self, UserVo):
        print('inside add user................')
        print(UserVo.UserName)
        sqlite_insert_query=f'insert into User(FirstName,Emaild,LastName,UserName ,Password ,GroupOwner,InGroup,Role,Status) values("{UserVo.FirstName}","{UserVo.Emaild}","{UserVo.LastName}","{UserVo.UserName}","{UserVo.Password}","{UserVo.GroupOwner}","{UserVo.InGroup}",0,0);'
        cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.add(UserVo)
        # db.session.commit()

    def deActivateUser(self, UserId):
        user=self.getByUserId(UserId)
        sqlite_insert_query='select * from User where UserId='+str(UserId)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        UserVo=ansToPostVo(ans)
        UserVo.Status=0
        sqlite_insert_query=f'UPDATE user SET Status="0" WHERE UserId="{UserId}";'
        cur.execute(sqlite_insert_query)
        con.commit()

        # db.session.add(user[0])
        # db.session.commit()
    
    def getByUserId(self, userId):
        sqlite_insert_query='select * from User where UserId='+str(userId)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        user=ansToPostVo(ans)
        # user=UserVo.query.filter_by(UserId = userId).all()
        return user

    def getUserByUserName(self,name):
        print('inside get................')
        sqlite_insert_query='select * from User where UserName="'+str(name)+'";'
        cur.execute(sqlite_insert_query)
        print('tryint to execute')
        ans=cur.fetchone()
        print('tryint to executed....')
        user=None
        if ans!=None:
            user=ansToPostVo(ans)
        # print(user.UserName)
        # user=UserVo.query.filter_by(UserName = name).all()
        return user
        
    def getUserByEmailId(self,email):
        sqlite_insert_query='select * from User where EmailId='+str(email)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        user=ansToPostVo(ans)
        # user=UserVo.query.filter_by(EmailId = email).all()
        return user
    def getUnApprovedUsers(self):
        sqlite_insert_query='select * from User where Status=0;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        users=[]
        for i in ans:
            users.append(ansToPostVo(i))
        # user=ansToPostVo(ans)
        # users=UserVo.query.filter_by(Status=0).all()
        return users
    
    def approveUser(self,UserId):
        sqlite_insert_query='select * from User where UserId='+str(UserId)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        # users=[]
        # for i in ans:
        #     users.append(ansToPostVo(i))
        UserVo=ansToPostVo(ans)
        # user=self.getByUserId(UserId)
        UserVo.Status=1
        sqlite_insert_query=f'UPDATE user SET Status="1" WHERE UserId="{UserId}";'
        cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.commit()
        # return 1

    def getActiveUsers(self):
        sqlite_insert_query='select * from User where Status=1;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        activeUser=[]
        for i in ans:
            activeUser.append(ansToPostVo(i))
        # activeUser=UserVo.query.filter_by(Status = 1).filter_by(Role = 0).all()
        print(activeUser)
        return activeUser