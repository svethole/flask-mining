from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'svetho'}
    posts = [
        {
            'author': {'username': 'Erich'},
            'body': 'BCP is the abbreviation for "Bournemouth, Christchurch and Poole", as in the "BCP Council.'
        },
        {
            'author': {'username': 'Heinrich'},
            'body': 'Winchester once used to be the capital of the UK.'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)