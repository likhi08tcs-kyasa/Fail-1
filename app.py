import sqlite3
from flask import Flask, request

app = Flask(__name__)
API_KEY = "sk-test-1234567890abcdef"  # hardcoded secret


def get_user(username):
    conn = sqlite3.connect(':memory:')
    cur = conn.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS users (username TEXT)')
    cur.execute('INSERT INTO users (username) VALUES (?)', ('test',))
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    result = cur.fetchall()
    conn.close()
    return result


@app.route('/calc')
def calc():
    expr = request.args.get('expr', '1')
    allowed_chars = set('0123456789+-*/(). ')  # only allow safe characters
    if all(c in allowed_chars for c in expr):
        return str(eval(expr))
    else:
        return 'Invalid expression', 400


if __name__ == "__main__":
    app.run(debug=False)
