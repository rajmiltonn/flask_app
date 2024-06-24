from flask import Flask
from flask_mysqldb import MySQL

app = Flask(__name__)

# Configuration for MySQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'your_username'
app.config['MYSQL_PASSWORD'] = 'your_password'
app.config['MYSQL_DB'] = 'users'

mysql = MySQL(app)

@app.route('/test_db')
def test_db():
    try:
        cursor = mysql.connection.cursor()
        cursor.execute('SELECT 1')
        result = cursor.fetchone()
        if result:
            return 'MySQL connection is successful!'
        else:
            return 'Failed to fetch data from MySQL.'
    except Exception as e:
        return f'MySQL connection error: {e}'

if __name__ == '__main__':
    app.run(debug=True)
