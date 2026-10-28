import sqlite3
from flask import Flask, request
import ast

app = Flask(__name__)


def get_user(username):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE users (username TEXT)')
    cur.execute('INSERT INTO users (username) VALUES (?)', ('test',))
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cur.fetchall()
    conn.close()
    return result


@app.route('/user')
def user():
    return str(get_user(request.args.get('username', '')))


@app.route('/calc')
def calc():
    expr = request.args.get('expr', '1')
    return str(ast.literal_eval(expr))  # safely evaluate expression


if __name__ == "__main__":
    app.run(debug=True)
