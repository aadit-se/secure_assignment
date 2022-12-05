# from project import db
from project.com.vo.PostVo import PostVo
from project.com.dao.CommentDAO import CommentDAO
from project import cur
from project import con
CommentDao=CommentDAO()

def ansToPostVo(ans):
    vo=PostVo(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5],ans[6] ,ans[7] ,ans[8] , ans[9])
    return vo

class PostDAO:
    def addPost(self, PostVo,time):
        sqlite_insert_query=f'insert into postMaster(GroupId,GroupName,CreatorId,type,createdTime,Status ,AdminId ,UserName , PostDescription) values("{PostVo.GroupId}","{PostVo.GroupName}","{str(PostVo.CreatorId)}","{PostVo.type}","{PostVo.createdTime}","{PostVo.Status}","{PostVo.Status}","{PostVo.UserName}","{PostVo.PostDescription}");'
        cur.execute(sqlite_insert_query)
        con.commit()
        sqlite_select_query=f'select * from postMaster where createdTime="{PostVo.createdTime}";'
        cur.execute(sqlite_select_query)
        ans=cur.fetchone()
        post=ansToPostVo(ans)
        return post
    
    def deletePost(self, PostId):
        sqlite_insert_query='DELETE FROM postMaster where PostId='+str(PostId)+';'
        cur.execute(sqlite_insert_query)
        con.commit()
        # post=self.getPostByPostId(PostId)[0]
        # db.session.delete(post)
        # db.session.commit()
        return 

    def getpostByCreatTime(self,time):
        sqlite_insert_query='SELET * FROM postMaster where createdTime='+str(time)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        post=ansToPostVo(ans)
        # post=PostVo.query.filter_by(createdTime = time).all()
        return post
    
    def getPostByPostId(self, PostId):
        sqlite_insert_query='SELET * FROM postMaster PostId='+str(PostId)+';'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        post=ansToPostVo(ans)
        # post=PostVo.query.filter_by(PostId = PostId).all()
        return post

    def getUnapporvedPostByGroupId(self, GroupId):
        sqlite_insert_query=f'SELECT * FROM postMaster where GroupId="{GroupId}" and Status=0;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        unApprovedPosts=[]
        for i in ans:
            unApprovedPosts.append(ansToPostVo(i))
        # post=ansToPostVo(ans)
        # unApprovedPosts=PostVo.query.filter_by(GroupId = GroupId).filter_by(Status = 0).all()
        return unApprovedPosts

    def getApporvedPostByGoupId(self, GroupId):
        sqlite_insert_query=f'SELECT * FROM postMaster where GroupId="{GroupId}" and Status=1;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        approvedPosts=[]
        for i in ans:
            approvedPosts.append(ansToPostVo(i))
        print('inside.....getApporvedPostByGoupId')
        # approvedPosts=PostVo.query.filter_by(GroupId = GroupId).filter_by(Status = 1).all()
        postComments=[]
        for j in approvedPosts:
            comments=CommentDao.getCommentByPostId(j.PostId)
            postComments.append([j,comments])
        print('postComments:',postComments)
        return postComments

    def getUnapporvedPost(self):
        # unApprovedPosts=PostVo.query.filter_by(Status = 0).all()
        sqlite_insert_query='SELECT * FROM postMaster where Status=0;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        unApprovedPosts=[]
        for i in ans:
            unApprovedPosts.append(ansToPostVo(i))
        return unApprovedPosts

    def getApporvedPost(self):
        print('inside getApprovedPost..............')
        sqlite_insert_query='SELECT * FROM postMaster where Status=1;'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        approvedPosts=[]
        for i in ans:
            approvedPosts.append(ansToPostVo(i))
        return approvedPosts
        # approvedPosts=PostVo.query.filter_by(Status = 1).all()
        # # get comment here append with post and then load it
        # postComments=[]
        # for j in approvedPosts:
        #     comments=CommentDao.getCommentByPostId(j.PostId)
        #     postComments.append([j,comments])
        # print('postComments:',postComments)
        # return postComments

    def apporvePost(self,PostId):
        print(PostId)
        sqlite_insert_query=f'SELECT * FROM postMaster where PostId="{PostId}";'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchone()
        PostVo=ansToPostVo(ans)
        # approvedPosts=[]
        # post=self.getPostByPostId(PostId)
        PostVo.Status=1
        sqlite_insert_query=f'UPDATE postMaster set Status=1 where POstId="{PostVo.PostId}";'
        cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.commit()
        # return 1