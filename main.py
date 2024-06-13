from flask import Flask, render_template
import requests
from post import Post

post_objects=[]

posts=requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()
for post in posts:
    post_obj = Post(post["id"],post["title"],post["subtitle"],post["body"])
    post_objects.append(post_obj)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html",posts=posts)

@app.route("/post/<int:blog_id>")
def loadpost(blog_id):
    for post in post_objects:
        if post.id==blog_id:
            blog=post
    return render_template("post.html",blog=blog)

if __name__ == "__main__":
    app.run(debug=True)
