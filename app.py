from flask import Flask, render_template, request
from flask.json.tag import JSONTag
from flask_mysqldb import MySQL
app = Flask(__name__)


app.config['MYSQL_HOST'] = 'sql'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'test'
app.config['MYSQL_DB'] = 'mysql'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)

@app.route('/', methods=['GET', 'POST'])
def users():
    cur = mysql.connection.cursor()
    cur.execute('''SELECT * FROM people_db.people''')
    rv = cur.fetchall()
    return str(rv)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
