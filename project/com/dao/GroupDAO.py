# from project import db
from project.com.vo.groupVo import GroupVo
from project.com.vo.UserGroupVo import UserGroupVo

from project.com.dao.UserGroupDAO import UserGroupDAO
from project import cur
from project import con
# UserGroupDao=UserGroupDAO()

class GroupDAO:
    def addGroup(self, GroupVo):
        # db.session.add(GroupVo)
        # db.session.commit()
        sqlite_insert_query=f'insert into goupMaster(GroupName,AdminId,Status,AdminName) values("{GroupVo.GroupName}","{GroupVo.AdminId}","{GroupVo.Status}","{GroupVo.AdminName}");'
        cur.execute(sqlite_insert_query)
        con.commit()

    def getAllGroup(self):
        sqlite_insert_query='select * from goupMaster;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToGroup(i))
        # print('inside getr all group')
        # groups=GroupVo.query.all()
        # print('group dao',groups)
        for g in groups:
            print(g.GroupName)
        return groups

    def getGroupsByGroupname(self,GroupName):
        sqlite_insert_query=f'select * from goupMaster where GroupName="{GroupName}";'
        cur.execute(sqlite_insert_query)
        # groups=GroupVo.query.filter_by(GroupName = GroupName).all()
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToGroup(i))
        return groups

    def getGroupsWhereAdminId(self,UserId):
        sqlite_insert_query='select * from goupMaster where AdminId='+str(UserId)+';'
        groups=cur.execute(sqlite_insert_query)
        # groups=GroupVo.query.filter_by(AdminId = UserId).all()
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToGroup(i))
        return groups
    def getGroupsByGroupId(self,GroupId):
        sqlite_insert_query='select * from goupMaster where GroupId='+str(GroupId)+';'
        cur.execute(sqlite_insert_query)
        # group=GroupVo.query.filter_by(GroupId = GroupId).all()
        ans=cur.fetchone()
        # groups=[]
        # for i in ans:
        group=ansToGroup(ans)
        return group
    
    def UnApporvedGroup(self):
        sqlite_insert_query='select * from goupMaster where Status='+str(0)+';'
        groups=cur.execute(sqlite_insert_query)
        # groups=GroupVo.query.filter_by(Status=0).all()
        ans=cur.fetchall()
        groups=[]
        for i in ans:
            groups.append(ansToGroup(i))
        return groups

    def apporvedGroup(self,GroupId):
        sqlite_select_query=f'select * from goupMaster where GroupId="{GroupId}";'
        group=cur.execute(sqlite_select_query)
        # group=self.getGroupsByGroupId(GroupId)
        ans=cur.fetchone()
        group=ansToGroup(ans)
        group.Status=1
        sqlite_insert_query=f'update goupMaster set Status=1 where GroupId="{GroupId}";'
        count=cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.commit()
        return 1
    
    def DeActivateGroup(self, GroupId):
        sqlite_select_query='select * from goupMaster where GroupId='+str(GroupId)+';'
        group=cur.execute(sqlite_select_query)
        ans=cur.fetchone()
        group=ansToGroup(ans)
        # group=self.getGroupsByGroupId(GroupId)
        # group=group[0]
        group.Status=0
        sqlite_insert_query=f'update goupMaster set Status="0" where GroupId="{group.GroupId}";'
        cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.commit()

    def activeGroups(self):
        print('activeGroups........ ')
        sqlite_insert_query=f'select * from goupMaster where Status=1;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        # groups=GroupVo.query.filter_by(Status = 1).all()
        groups=[]
        for i in ans:
            print(i)
            groups.append(ansToGroup(i))
        activeGroupUser=[]
        for j in groups:
            sqlite_insert_query=f'select * from UserGroup where GroupId="{j.GroupId}" and Status=1;'
            cur.execute(sqlite_insert_query)
            ans=cur.fetchone()
            if ans!=None:
                activeGroupUser.append([j,ansToUserGroup(ans)])
        print('................',activeGroupUser)
        return activeGroupUser

def ansToGroup(ans):
    vo=GroupVo(ans[0],ans[1],ans[2],ans[3],ans[4])
    return vo
def ansToUserGroup(ans):
    user=UserGroupVo(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5])
    return user