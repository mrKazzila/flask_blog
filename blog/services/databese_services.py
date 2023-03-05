import sqlite3
from typing import NoReturn


def _get_db_connection() -> sqlite3.Connection:
    """Get connection to database"""
    conn = sqlite3.connect('database.bd')
    conn.row_factory = sqlite3.Row

    return conn


def _get_all_posts() -> list:
    """Get all posts from database"""
    conn = _get_db_connection()
    posts = conn.execute('SELECT * FROM posts').fetchall()
    conn.close()

    return posts


def _get_post(post_id: int) -> str:
    """Get post with post_id from database"""
    conn = _get_db_connection()

    post = conn.execute(
        'SELECT * FROM posts WHERE id = ?',
        (post_id,),
    ).fetchone()

    conn.close()

    return post


def _add_post_to_db(title: str, content: str) -> NoReturn:
    """Add new post with param (title, content) in database"""
    conn = _get_db_connection()

    conn.execute(
        'INSERT INTO posts (title, content) VALUES (?, ?)',
        (title, content),
    )

    conn.commit()
    conn.close()


def _update_post_in_db(title: str, content: str, post_id: int) -> NoReturn:
    """Update post with param (title, content) in database"""
    conn = _get_db_connection()

    conn.execute(
        'UPDATE posts SET title = ?, content = ?'
        ' WHERE id = ?',
        (title, content, post_id),
    )

    conn.commit()
    conn.close()


def _delete_post_from_db(post_id: int) -> NoReturn:
    """Delete post by post_id from database"""
    conn = _get_db_connection()

    conn.execute(
        'DELETE FROM posts WHERE id = ?',
        (post_id,),
    )

    conn.commit()
    conn.close()
