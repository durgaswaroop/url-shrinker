from flask import Flask, render_template, request
import validators

import hashlib

app = Flask(__name__)

hostname = "http://localhost:5000/"


@app.route('/')
def index():
    return render_template('index.html', entered_url="http://", shrunken_url="")


@app.route('/', methods=['POST'])
def index_post():
    url = request.form['url']
    if not validate_url(url):
        return render_template('index.html', entered_url=url,
                               shrunken_url="Entered URL is not valid. Only Valid URL's can be shrunken")

    return render_template('index.html', entered_url=url, shrunken_url=shrink_it(url))


def shrink_it(url):
    hash = hashlib.md5()
    hash.update(url.encode('UTF-8'))
    return hostname + hash.hexdigest()[:7]


def validate_url(url):
    return validators.url(url)


def main():
    app.run(debug=True)


if __name__ == '__main__':
    main()
