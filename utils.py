import json, os
import pprint


def get_posts_all():
    """
    отображается вс посты
    """
    with open("data/data.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if os.path.exists('data/data.json'):
          return data
        else:
          return None




def get_posts_by_user(user_name):
    """
    отображает посты выбранного пользователя
    """
    posts = get_posts_all()
    posts_by_user = []
    for post in posts:
        if post["poster_name"] == user_name:
            posts_by_user.append(post)
    return posts_by_user


def search_for_posts(query):
    """
    отображает список словарей
    """
    posts = get_posts_all()
    matching_posts = []
    query_lower = query.lower()

    for post in posts:
        if query_lower in post["content"].lower():
            matching_posts.append(post)
    return matching_posts


def get_post_by_pk(pk):
    """
    отображает пост по его ID
    """
    posts = get_posts_all()
    for post in posts:
        if post['pk'] == pk:
          return post
        else:
          return None


def get_comments_all():
    """
    получаем комменатрии
    """
    with open("data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        if os.path.exists('data/comments.json'):
          return data
        else:
            return None


def get_comments_by_user(pk):
    """
    возвращает комментарии определенного пользователя
    """
    comments = get_comments_all()
    comments_for_posts = []

    for comment in comments:
        if comment["post_id"] == pk:
            comments_for_posts.append(comment)

    return comments_for_posts

