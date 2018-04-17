from flask import render_template
from app import app
from .classroom import Classroom
from .post import Post

post = Post(1, 'Return the linked list from function?', 'Richie', 6)
capstone = Classroom('CSCI 135')

for x in range(0, 50):
    capstone.addPost(post)    

@app.route('/')
@app.route('/index')
def loadPosts():
    return render_template('classposts.html', title=capstone.name, posts=capstone.posts)
    