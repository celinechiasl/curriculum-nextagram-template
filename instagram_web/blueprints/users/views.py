from flask import Blueprint, render_template, redirect, flash, url_for, request
from werkzeug.security import generate_password_hash
from models.user import * #for postbird to read the user list


users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('users/new.html')


@users_blueprint.route('/create', methods=['POST'])
def create():
    username = request.form.get('username')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)
    # pop out noti when successful signed up
    successsignedup = User(username=username, email=email, password=hashed_password)
    if successsignedup.save() and password != "":
        flash('Successfully signed up!', "success")
        return redirect(url_for('users.new')) #this users.new is referred to def new() as above
    else:
        flash('Registration failed. Username has been taken.', "danger")
        return render_template ('/users/new.html')


@users_blueprint.route('/<username>', methods=["GET"])
def show(username):
    pass


@users_blueprint.route('/', methods=["GET"])
def index():
    return "USERS"


@users_blueprint.route('/<id>/edit', methods=['GET'])
def edit(id):
    pass


@users_blueprint.route('/<id>', methods=['POST'])
def update(id):
    pass
