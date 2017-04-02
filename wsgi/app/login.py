from app import app
from flask import Flask, request, render_template, redirect, url_for, flash
import unirest
from forms import MessageForm
from app import simple
from app import database
from flask_navigation import Navigation
import flask_login
import flask
from database import mongo
from bokeh.util.string import encode_utf8


'''collection = mongo.db.users
users = []
for doc in collection.find():
    users.append({doc['username']:{'pw' : doc['password']}})

'''

login_manager = flask_login.LoginManager()

login_manager.init_app(app)

users = {'clouduser': {'pw': 'cloud123'}}

class User(flask_login.UserMixin):
    pass


@login_manager.user_loader
def user_loader(email):
    if email not in users:
        return

    user = User()
    user.id = email
    return user


@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in users:
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['pw'] == users[email]['pw']

    return user

@app.route('/login', methods=['GET', 'POST'])
def login():
    if flask.request.method == 'GET':
        html = flask.render_template('login.html')
        return encode_utf8(html)

    email = flask.request.form['email']
    if email in users and flask.request.form['pw'] == users[email]['pw'] :
        user = User()
        user.id = email
        flask_login.login_user(user)
        return flask.redirect(flask.url_for('protected'))


    html = flask.render_template('bad_login.html')
    return encode_utf8(html)


@app.route('/protected')
@flask_login.login_required
def protected():
    id = flask_login.current_user.id
    html = flask.render_template('protected.html',id=id)
    return encode_utf8(html)

@app.route('/logout')
def logout():
    flask_login.logout_user()
    html = flask.render_template('logout.html')
    return encode_utf8(html)

@login_manager.unauthorized_handler
def unauthorized_handler():
    html = flask.render_template('unauthorized.html')
    return encode_utf8(html)
