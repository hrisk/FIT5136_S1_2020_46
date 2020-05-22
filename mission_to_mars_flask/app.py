from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     return render_template('login.html')
#
#
# @app.route('/signup', methods=['GET', 'POST'])
# def signup():
#     return render_template('signup.html')


@app.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('login.html')


@app.route('/notfound', methods=['GET', 'POST'])
def error():
    return render_template('404.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
