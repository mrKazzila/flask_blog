from typing import NoReturn, Optional

from flask import flash, redirect, url_for
from werkzeug import Request
from werkzeug.datastructures import ImmutableMultiDict
from werkzeug.exceptions import abort

from blog.services.databese_services import (_add_post_to_db, _delete_post_from_db,
                                             _get_all_posts, _get_post,
                                             _update_post_in_db)


def get_post(post_id: int) -> Optional[str]:
    """Get post with post_id from database"""
    post = _get_post(post_id=post_id)
    return post if post is not None else abort(404)


def get_all_posts() -> list:
    """Get all posts from database"""
    posts = _get_all_posts()
    return posts if posts is not None else abort(404)


def delete_post(post_title: str, post_id: int) -> NoReturn:
    """Delete post by post_id from database"""
    _delete_post_from_db(post_id=post_id)
    flash(f'"{post_title}" was successfully deleted!')


def create_new_post(request: Request):
    """Create new post"""
    if request.method == 'POST':
        title, content = _get_title_and_content_from_form(request_form=request.form)

        if not title:
            flash('Title is required!')
        else:
            _add_post_to_db(title, content)
            return redirect(url_for('index'))


def edit_post(request: Request, post_id: int):
    """Edit post"""
    if request.method == 'POST':
        title, content = _get_title_and_content_from_form(request_form=request.form)

        if not title:
            flash('Title is required!')
        else:
            _update_post_in_db(title=title, content=content, post_id=post_id)
            return redirect(url_for('index'))


def _get_title_and_content_from_form(request_form: ImmutableMultiDict) -> tuple:
    """Get title and content from form"""
    return request_form['title'], request_form['content']
