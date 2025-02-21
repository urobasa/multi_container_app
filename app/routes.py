from flask import render_template, request, redirect, url_for
from .extensions import db  # Импортируем db из extensions.py
from .models import Post

def init_routes(app):
    @app.route('/')
    def index():
        posts = Post.query.all()
        return render_template('index.html', posts=posts)

    @app.route('/add', methods=['GET', 'POST'])
    def add_post():
        if request.method == 'POST':
            title = request.form['title']
            body = request.form['body']
            user_id = 1  # Используем существующий user_id

            new_post = Post(title=title, body=body, user_id=user_id)
            db.session.add(new_post)
            db.session.commit()

            return redirect(url_for('index'))

        return render_template('add_post.html')

