import os
from flask import Blueprint, render_template, request, current_app
from . import db  # Correct import statement

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return "Welcome to my Flask Application!"

@main.route('/new_user', methods=['GET', 'POST'])
def new_user():
    cursor = None
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            role = request.form.get('role')

            cursor = db.connection.cursor()
            cursor.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
            db.connection.commit()

            return f'New user added: {name}, {email}, {role}'
        
        # Render the new_user.html template for GET requests
        template_dir = os.path.join(current_app.root_path, 'templates')
        print(f"Templates directory: {template_dir}")
        return render_template('new_user.html')
    
    except Exception as e:
        return f'Error: {e}'
    
    finally:
        if cursor:
            cursor.close()

@main.route('/users')
def users():
    cursor = None
    try:
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM users')
        users = cursor.fetchall()
        return render_template('users.html', users=users)
    
    except Exception as e:
        return f'Error fetching users: {e}'
    
    finally:
        if cursor:
            cursor.close()

@main.route('/user/<int:user_id>')
def user_detail(user_id):
    cursor = None
    try:
        cursor = db.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        if user:
            return render_template('user_detail.html', user=user)
        else:
            return 'User not found'
    
    except Exception as e:
        return f'Error fetching user details: {e}'
    
    finally:
        if cursor:
            cursor.close()
