from flask import Flask
from data import db_session
from data.users import User
from data.jobs import Jobs
from flask import render_template

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'


def main():
    db_session.global_init("db/blogs.db")
    app.run()


@app.route("/")
def index():
    db_sess = db_session.create_session()
    data = db_sess.query(Jobs).all()
    return render_template("news.html", data=data)


if __name__ == '__main__':
    main()
