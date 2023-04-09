from flask import Flask, url_for, render_template, request, flash, session, redirect, abort, g
import os
from FDataBase import *


DATABASE = '/tmp/newapp.db'
DEBUG = True
SECRET_KEY = 'dsvq1dwq234!123<>{"{Ls2342vcj0j203i'

app = Flask(__name__)
app.config.from_object(__name__)
app.config.update(dict(DATABASE=os.path.join(app.root_path, 'newapp.db')))


# ----------------------Работа-с-базой-данных---------------------------------------

dbase = None
@app.before_request
def before_request():
    global dbase
    db = get_db()
    dbase = FDataBase(db)


def connect_db():
    conn = sqlite3.connect(app.config['DATABASE'])
    conn.row_factory = sqlite3.Row
    return conn


def create_db():
    """Вспомогательная функция для создания таблиц БД"""
    db = connect_db()
    with app.open_resource('sq_db.sql', mode='r') as file:
        db.cursor().executescript(file.read())
    db.commit()
    db.close()


def get_db():
    '''Соединение с БД, если оно еще не установлено'''
    if not hasattr(g, 'link_db'):
        g.link_db = connect_db()
        return g.link_db



@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'link_db'):
        g.link_db.close()


# ----------------------Обработчики-страниц---------------------------------------

@app.route('/index')
def index():
    '''Обработчик главной страница'''
    return render_template('index.html', menu=dbase.getMenu(),
                           posts=dbase.getPostAnonce(), username=session['userLogger'])

@app.route("/")
def test():
    """Заглушка выдающая авторизацию"""
    return render_template('login.html', title="Авторизация")


@app.route("/login", methods=["POST", "GET"])
def login():
    """Обработчик страницы с авторизацией"""
    if 'userLogger' in session:
        return redirect(url_for('profile', username=session['userLogger']))
    elif request.method == 'POST' and request.form['username'] == 'svr013'\
            and request.form['psw'] == '123':
        session['userLogger'] = request.form['username']
        return redirect(url_for('profile', username=session['userLogger']))
    elif request.method == 'POST' and request.form['username'] != 'svr013'\
            or request.form['psw'] != '123':
        flash('Неправильное имя пользователя или пароль', category='error')
        return render_template('login.html', title="Авторизация", menu=[])
    return render_template('login.html', title="Авторизация", menu=[])


@app.route('/profile/<username>')
def profile(username):
    '''Обработчик страница с профилем пользователя'''
    if 'userLogger' not in session or session['userLogger'] != username:
        abort(401)

    return redirect(url_for('index'))


@app.route('/create', methods=['POST', 'GET'])
def create():
    """Обработчик страницы с добавлением нового дела в список"""
    if request.method == 'POST':
        if len(request.form["case_name"]) > 2:
            res = dbase.addPost(request.form["case_name"], request.form["case_comment"])
            if not res:
                flash('Дело не добавлено', category='error')
            else:
                flash('Дело добавлено', category='success')
        else:
            flash('Дело не добавлено', category='error')

    return render_template('create.html', title='Добавить новое дело:',
                           menu=dbase.getMenu(), username=session['userLogger'])


@app.errorhandler(404)
def page_not_found(error):
    """ Обработчик страницы с заглушкой при ошибке 404"""
    print(error)
    return render_template('page404.html', title="Cтраница не найдена",
                           menu=dbase.getMenu(), username=session['userLogger']), 404

@app.errorhandler(500)
def page_not(error):
    """ Обработчик страницы с заглушкой при попытке обойти авторизацию"""
    print(error)
    return redirect(url_for('login'))

@app.route('/update/<int:id_post>', methods=['POST', 'GET'])
def createUpdate(id_post):
    """Обработчик страницы с добавлением нового дела в список"""
    for i, j in dbase.getPost(id_post):
        title = i
        comment = j
        if not title:
            abort(404)
    if request.method == 'POST':
        if len(request.form["case_name"]) > 2:
            res = dbase.updatePost(id_post, request.form["case_name"], request.form["case_comment"])
            if not res:
                flash('Дело не изменено', category='error')
            else:
                flash('Дело изменено', category='success')
                return render_template('post.html',
                                       menu=dbase.getMenu(),
                                       title=request.form["case_name"],
                                       comment=request.form["case_comment"],
                                       id_post=id_post, username=session['userLogger'])
        else:
            flash('Дело не изменено', category='error')

    return render_template('post.html', menu=dbase.getMenu(), title=title,
                           comment=comment, id_post=id_post, username=session['userLogger'])


@app.route('/delete/<int:id_post>')
def delete(id_post):
    """Обработчик страницы с удалением дела"""
    res = dbase.deletePost(id_post)
    if not res:
        print('Дело удалено')
    return render_template("delete.html",
                           menu=dbase.getMenu(), id_post=id_post,
                           username=session['userLogger'])



if __name__ == "__main__":
    app.run(debug=False)
