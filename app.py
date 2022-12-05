from project import app
from flask import url_for, redirect
# from project import db
# from project.com.dao.UserDAO import UserDAO
# from project.com.vo.UserVo import UserVo



if __name__=='__main__':
    app.run(debug=True,threaded=True, port=8000)
    # return redirect(url_for('index'))