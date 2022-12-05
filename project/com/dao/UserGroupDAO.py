# from project import db
from project.com.vo.UserGroupVo import UserGroupVo
from project.com.vo.groupVo import GroupVo
from project import cur
from project import con

def ansToUserGroupVo(ans):
    vo=UserGroupVo(ans[0],ans[1],ans[2],ans[3] ,ans[4] ,ans[5])
    return vo

class UserGroupDAO:
    def addUserGroup(self, UserGroupVo):
        sqlite_insert_query=f'insert into UserGroup(GroupId,GroupName,UserId,Status ,AdminId ,UserName) values("{UserGroupVo.GroupId}","{UserGroupVo.GroupName}","{UserGroupVo.UserId}","0","{UserGroupVo.AdminId}","{UserGroupVo.UserName}");'
        cur.execute(sqlite_insert_query)
        con.commit()
        # print('add iuser group.......')
        # print(vo.GroupId,vo.UserId)
        # db.session.add(vo)
        # db.session.commit()

    def addUserGroupAdmin(self, vo):
        print('add iuser group.......')
        sqlite_insert_query='insert into UserGroup(GroupId,GroupName,UserId,Status ,AdminId ,UserName) values('+UserGroupVo.GroupId+','+UserGroupVo.GroupName+','+UserGroupVo.UserId+','+str(1)+','+UserGroupVo.AdminId+','+UserGroupVo.UserName+');'
        cur.execute(sqlite_insert_query)
        con.commit()
        # print(vo.GroupId,vo.UserId)
        # vo.Status=1
        # db.session.add(vo)
        # db.session.commit()
    
    def getByUserId(self,userId):
        sqlite_insert_query='select * from UserGroup where userId='+userId+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToUserGroupVo(i))
        # con.commit()
        # groups=UserGroupVo.query.filter_by(UserId = userId).all()
        return groups
    
    def getByUserIdGroupId(self,userId,GroupId):
        sqlite_insert_query='select * from UserGroup where userId='+userId+' and GroupId='+GroupId+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToUserGroupVo(i))
        # groups=UserGroupVo.query.filter_by(UserId = userId).filter_by(GroupId = GroupId).all()
        return groups
   
    def getApprovedGroupsByUserId(self,userId):
        req=[]
        print(userId)
        sqlite_insert_query=f'select * from UserGroup where userId="{userId}" and Status="1";'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        approvedGroups=[]
        for i in ans:
            approvedGroups.append(ansToUserGroupVo(i))
        # approvedGroups=UserGroupVo.query.filter_by(UserId = userId).filter_by(Status=1).all()
        # print(approvedGroups.GroupName)
        for gr in approvedGroups:
            sert_query=f'select * from goupMaster where GroupId="{gr.GroupId}";'
            cur.execute(sert_query)
            ans=cur.fetchone()
            group=ansToGroup(ans)
            print(group.Status)
            if group.Status==1:
                req.append(group)
        return req
    
    def getUnapporvedUserByGroupId(self, GroupId):
        # unApprovedUsers=UserGroupVo.query.filter_by(GroupId = GroupId).filter_by(Status = 0).all()
        sqlite_insert_query=f'select * from UserGroup where GroupId="{GroupId}" and Status=0;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        unApprovedUsers=[]
        for i in ans:
            unApprovedUsers.append(ansToUserGroupVo(i))
        return unApprovedUsers
    
    def getUnapporvedUser(self):
        # unApprovedUsers=UserGroupVo.query.filter_by(Status = 0).all()
        sqlite_insert_query='select * from UserGroup where Status=0;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        unApprovedUsers=[]
        for i in ans:
            unApprovedUsers.append(ansToUserGroupVo(i))
        return unApprovedUsers
    
    def apporveUser(self,vo):
        sqlite_insert_query=f'select * from UserGroup where UserId="{vo.UserId}" and GroupId="{vo.GroupId}";'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        GroupVo=ansToGroup(ans)
        # groups=self.getByUserIdGroupId(vo.UserId,vo.GroupId)
        GroupVo.Status=1
        sqlite_insert_query=f'update UserGroup set Status=1 where  GroupId="{GroupVo.GroupId}" and UserId="{vo.UserId}"'
        cur.execute(sqlite_insert_query)
        con.commit()

        # db.session.commit()
        # return 1
    
def ansToGroup(ans):
    vo=GroupVo(ans[0],ans[1],ans[2],ans[3],ans[4])
    return vo