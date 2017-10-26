""" Views file for the Flask APP"""
from flask import render_template, session, redirect, url_for, request
# from werkzeug.utils import secure_filename
from app import APP

DATABASE = [
    ("User1", "password"),
    ("User2", "password")
]

USER = {'nickname': 'Sylvance', 'job': 'Carpernter', 'categoriesno': 8, 'recipesno': 23}

@APP.route('/')
@APP.route('/index')
def index():
    """ Here the user sees the signup and signin gateways """
    return render_template('home.html',
                           title='Home')


@APP.route('/addcategory', methods=['GET', 'POST'])
def addcategory():
    """ A form to add a new category """
    return render_template('addcategory.html',
                           title='addcategory',
                           user=USER)


@APP.route('/addrecipe', methods=['GET', 'POST'])
def addrecipe():
    """ A form that adds a new recipe """
    return render_template('addrecipe.html',
                           title='addrecipe',
                           user=USER)


@APP.route('/category')
def category():
    """ This is a view page for the category """
    return render_template('category.html',
                           title='category',
                           user=USER)


@APP.route('/editcategory', methods=['GET', 'POST'])
def editcategory():
    """ A form that edits the category """
    return render_template('editcategory.html',
                           title='editcategory',
                           user=USER)


@APP.route('/editrecipe', methods=['GET', 'POST'])
def editrecipe():
    """ Here you can edit the details of the recipe """
    return render_template('editrecipe.html',
                           title='editrecipe',
                           user=USER)


@APP.route('/profile')
def profile():
    """ Here the use r can view his/her profile """
    return render_template('profile.html',
                           title='profile',
                           user=USER)


@APP.route('/recipe')
def recipe():
    """ This is where you view the recipe"""
    return render_template('recipe.html',
                           title='recipe',
                           user=USER)


@APP.route('/signin', methods=['GET', 'POST'])
def signin():
    """ This is the page where you sign in """
    if request.method == 'POST':

        session['username'] = request.form['username']
        username = request.form['username']
        password = request.form['password']
        if (username, password) in DATABASE:
            return redirect('/profile')
        return redirect('/signin')

    return render_template('signin.html',
                           title='signin')

@APP.route('/signup', methods=['GET', 'POST'])
def signup():
    """ This is a form that takes sign up details """
    if request.method == 'POST':
        session['username'] = request.form['username']
        newusername = request.form['username']
        newpassword = request.form['password']
        DATABASE.append((newusername, newpassword))
        return redirect('/profile')
    return render_template('signup.html',
                           title='signup')


@APP.route('/viewcategory')
def viewcategory():
    """ You can view the list of categories """
    return render_template('viewcategory.html',
                           title='viewcategory',
                           user=USER)


@APP.route('/viewrecipe')
def viewrecipe():
    """ You can see a list of recipes """
    return render_template('viewrecipe.html',
                           title='viewrecipe',
                           user=USER)


@APP.route('/logout')
def logout():
    """ remove the username from the session if it's there """
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
APP.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    APP.run(debug=True,
            host="0.0.0.0",
            port="8888")
