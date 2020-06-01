from flask import Flask, render_template, request, redirect, url_for, flash, session
import re

# setup the app
app = Flask(__name__)
app.config['DEBUG'] = True

####  setup routes  ####
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/charts')
def charts():
    return render_template('charts.html')


@app.route('/tables')
def tables():
    return render_template('tables.html')


@app.route('/forms')
def forms():
    return render_template('forms.html')


@app.route('/bootstrap-elements')
def bootstrap_elements():
    return render_template('bootstrap-elements.html')


@app.route('/bootstrap-grid')
def bootstrap_grid():
    return render_template('bootstrap-grid.html')


@app.route('/blank-page')
def blank_page():
    return render_template('blank-page.html')


@app.route('/profile')
def profile():
    return render_template('profile.html')


@app.route('/settings')
def settings():
    return render_template('settings.html')

####  end routes  ####



if __name__ == "__main__":
	# change to app.run(host="0.0.0.0"), if you want other machines to be able to reach the webserver.
	app.run() 