from flask import Flask, render_template, make_response, jsonify, redirect, \
    url_for
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/text')
def text():
    return render_template('text.txt'), 200, {'Content-Type': 'text/plain'}


@app.route('/xml')
def xml():
    return '<h1>this is shown as <b>XML</b> in the browser</h1>', 200, \
           {'Content-Type': 'application/xml'}


@app.route('/json')
def json():
    return jsonify({'first_name': 'John', 'last_name': 'Smith'})


@app.route('/redirect')
def redir():
    return redirect(url_for('text'))


@app.route('/cookie')
def cookie():
    resp = redirect(url_for('index'))
    resp.set_cookie('cookie', 'Hello, I\'m a cookie')
    return resp


@app.route('/error')
def error():
    return 'Bad Request', 400


@app.route('/response')
def response():
    resp = make_response(render_template('text.txt'))
    resp.headers['Content-Type'] = 'text/plain'
    return resp


if __name__ == '__main__':
    app.run(debug=True)
