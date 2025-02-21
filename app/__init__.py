from flask import Flask
from .extensions import db  # Импортируем db из extensions.py
from .models import User  # Импортируем модель User

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://user:password@db:5432/flaskdb'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        from . import routes
        db.create_all()
        routes.init_routes(app)

        # Добавляем пользователя, если таблица пуста
        if not User.query.first():
            default_user = User(name="Default User", username="default", email="default@example.com")
            db.session.add(default_user)
            db.session.commit()

    return app

app = create_app()

