from flask import Flask, request, render_template, helpers, debughelpers
import utils

# from utils import get_posts_all, get_posts_by_user, get_post_by_pk, search_for_posts

app = Flask(__name__)


@app.route('/')
def page_index():
    posts = utils.get_posts_all()
    return render_template('index.html', posts=posts)


@app.route('/posts/<int:post_pk>')
def pag_single_post(post_pk):
    post = utils.get_post_by_pk(post_pk)
    comments = utils.get_comments_by_user(post_pk)
    comments_len = len(comments)
    return render_template("post.html", post=post, comments = comments, comments_len=comments_len)

@app.route('/search')
def page_search():
    query = request.args.get("s")
    if not query or query == "":
        return "вы ничего не искали"
    posts = utils.search_for_posts(query)
    posts_count = len(posts)
    return render_template("search.html", posts=posts, posts_count=posts_count, query=query)

@app.route("/user/<user_name>")
def page_user(user_name):
    posts = utils.get_posts_by_user(user_name)
    posts_count = len(posts)

    return render_template("user-feed.html", posts=posts, posts_count=posts_count, user_name=user_name)

if __name__ == '__name__':
  app.run(debug=True)
