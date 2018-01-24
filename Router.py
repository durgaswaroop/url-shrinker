from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def index_post():
    url = request.form['url']
    return url


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
