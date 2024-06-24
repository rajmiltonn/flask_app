from flask import Flask, render_template, request, redirect, url_for, abort
from flask_mysqldb import MySQL
from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

mysql = MySQL(app)

@app.route('/')
def index():
    return "Welcome to my Flask Application!"

@app.route('/hello')
def hello():
    return "Hello, World!"

@app.route('/new_user', methods=['GET', 'POST'])
def new_user():
    cursor = None
    try:
        if request.method == 'POST':
            name = request.form.get('name')
            email = request.form.get('email')
            role = request.form.get('role')

            cursor = mysql.connection.cursor()
            cursor.execute('INSERT INTO users (name, email, role) VALUES (%s, %s, %s)', (name, email, role))
            mysql.connection.commit()

            return redirect(url_for('users'))

        return render_template('new_user.html')

    except Exception as e:
        return f'Error: {e}'

    finally:
        if cursor:
            cursor.close()

@app.route('/users')
def users():
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT id, name, email, role FROM users')
        users = cursor.fetchall()
        return render_template('users.html', users=users)

    except Exception as e:
        return f'Error fetching users: {e}'

    finally:
        if cursor:
            cursor.close()

@app.route('/user/<int:user_id>')
def user_detail(user_id):
    cursor = None
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT * FROM users WHERE id = %s', (user_id,))
        user = cursor.fetchone()
        if user:
            return render_template('user_detail.html', user=user)
        else:
            return 'User not found', 404

    except Exception as e:
        return f'Error fetching user details: {e}'

    finally:
        if cursor:
            cursor.close()

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True)
