from flask import Flask, Blueprint, request, render_template, make_response, jsonify, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user
from hitode_control.user_mgmt import User
from hitode_control.program_mgmt import Program

hitode_matching = Blueprint('hitode', __name__)

# Main Page
@hitode_matching.route('/')
def main_page():
    if current_user.is_authenticated:
        items = Program.find_all()
        return render_template('hitode.html', user_email=current_user.user_email, items=items)
    else:
        return render_template('hitode.html')

# Create Page
@login_required
@hitode_matching.route('/create')
def create():
    if current_user.is_authenticated:
        return render_template('create.html', user_email=current_user.user_email)
    else:
        return "Error"
    
# Update Page
@login_required
@hitode_matching.route('/update')
def update():
    if current_user.is_authenticated:
        return render_template('update.html', user_email=current_user.user_email)
    else:
        return "Error"
    
# delete Page
@login_required
@hitode_matching.route('/delete')
def delete():
    if current_user.is_authenticated:
        return render_template('delete.html', user_email=current_user.user_email)
    else:
        return "Error"


# User
# Login | Register
@hitode_matching.route('/set_email', methods=['POST'])
def set_email():
    user = User.create(request.form['user_email'], request.form['user_password'])
    login_user(user)
    return redirect(url_for('hitode.main_page'))

# User
# Logout
@login_required # test
@hitode_matching.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('hitode.main_page'))


# Program
# Create
@login_required
@hitode_matching.route('/program_create', methods=['POST'])
def program_create():
    Program.create(current_user.id, request.form['program_content'])
    return redirect(url_for('hitode.main_page'))


# Program
# Update
@login_required
@hitode_matching.route('/program_update', methods=['POST'])
def program_update():
    if current_user.id == Program.find_one(int(request.form['program_no'])):
        Program.update(int(request.form['program_no']), request.form['program_content'])
    return redirect(url_for('hitode.main_page'))



# Program
# Delete
@login_required
@hitode_matching.route('/program_delete', methods=['POST'])
def program_delete():
    if current_user.id == Program.find_id(int(request.form['program_no'])):
        Program.delete(int(request.form['program_no']))    
    return redirect(url_for('hitode.main_page'))



# @login_required
# @hitode_matching.route('/auth')
# def auth_test():
#     return 'auth'