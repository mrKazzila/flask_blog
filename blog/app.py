from flask import Flask, redirect, render_template, request, url_for

from blog.config import BlogConfig
from blog.services.blog_services import (create_new_post, delete_post, edit_post,
                                    get_all_posts, get_post)

app = Flask(__name__)
app.config.from_object(BlogConfig)


@app.route('/')
def index():
    """Main app page"""
    posts = get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/<int:post_id>')
def post(post_id):
    """Post page"""
    post = get_post(post_id=post_id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    """Create new post"""
    create_new_post(request=request)
    return render_template('create.html')


@app.route('/<int:post_id>/edit', methods=('GET', 'POST'))
def edit(post_id):
    """Edit post"""
    post = get_post(post_id=post_id)
    edit_post(request=request, post_id=post_id)
    return render_template('edit.html', post=post)


@app.route('/<int:post_id>/delete', methods=('POST',))
def delete(post_id):
    """Delete post"""
    post = get_post(post_id=post_id)
    post_title = post['title']
    delete_post(post_title=post_title, post_id=post_id)
    return redirect(url_for('index'))
