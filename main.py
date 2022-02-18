from flask import Flask, request, render_template, helpers, debughelpers
from utils import get_post_by_pk, get_posts_by_user, search_for_posts, get_comments_by_user, get_posts_all

app = Flask(__name__)


@app.route('/')
def page_index():
    posts = get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_pk>')
def pag_single_post(post_pk):
    post = get_post_by_pk(post_pk)
    comments = get_comments_by_user(post_pk)
    comments_len = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@app.route('/search')
def page_search():
    query = request.args.get("s")
    if not query:
        return "вы ничего не искали"
    posts = search_for_posts(query)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count, query=query)


@app.route("/user/<user_name>")
def page_user(user_name):
    posts = get_posts_by_user(user_name)
    posts_count = len(posts)

    return render_template("user-feed.html", posts=posts, posts_count=posts_count, user_name=user_name)

app.run()

