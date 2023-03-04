from flask import Flask, redirect, render_template, request, url_for

from services.blog_services import (create_new_post, delete_post, edit_post,
                                    get_all_posts, get_post)

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you secret key'


@app.route('/')
def index():
    """Main app page"""
    posts = get_all_posts()
    return render_template('index.html', posts=posts)


@app.route('/<int:id>')
def post(id):
    """Post page"""
    post = get_post(id)
    return render_template('post.html', post=post)


@app.route('/create', methods=('GET', 'POST'))
def create():
    """Create new post"""
    create_new_post(request=request)
    return render_template('create.html')


@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    """Edit post"""
    post = get_post(id)
    edit_post(request=request, post_id=id)
    return render_template('edit.html', post=post)


@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    """Delete post"""
    post = get_post(id)
    post_title = post['title']
    delete_post(post_title=post_title, post_id=id)
    return redirect(url_for('index'))
