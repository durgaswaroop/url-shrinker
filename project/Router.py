from flask import Flask, render_template, request
import validators

import hashlib

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', shrunken_url="")


@app.route('/', methods=['POST'])
def index_post():
    url = request.form['url']
    return render_template('index.html', shrunken_url=shrink_it(url))


def shrink_it(url):
    hash = hashlib.md5()
    hash.update(url.encode('UTF-8'))
    return hash.hexdigest()[:7]


def validate_url(url):
    return validators.url(url)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
