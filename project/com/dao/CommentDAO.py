# from project import db
from project.com.vo.CommentVo import CommentVo
from project import cur
from project import con

# vo=CommentVo()
# pstvo=PostVo()
def ansToComment(ans):
    vo=CommentVo(ans[0],ans[1],ans[2],ans[3],ans[4],ans[5])
    return vo
class CommentDAO:
    def addComment(self, CommentVo):
        
        sqlite_insert_query=f'insert into CommentVo(commentDescription,PostId,CommentTime,CommentorId,UserName) values("{CommentVo.commentDescription}","{CommentVo.PostId}","{CommentVo.CommentTime}","{CommentVo.CommentorId}","{CommentVo.UserName}");'
        count=cur.execute(sqlite_insert_query)
        con.commit()
        # db.session.commit()

    def getCommentByPostId(self, PostId):
        # comments=CommentVo.query.filter_by(PostId = PostId).all()
        sqlite_insert_query=f'SELECT * FROM CommentVo where PostId="{PostId}";'
        cur.execute(sqlite_insert_query)
        ans=cur.fetchall()
        comments=[]
        for i in ans:
            comments.append(ansToComment(i))
        return comments