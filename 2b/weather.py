from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
              'August', 'September', 'October', 'November', 'December']
    return render_template('index.html', city='Portland, OR', months=months)


if __name__ == '__main__':
    app.run(debug=True)
