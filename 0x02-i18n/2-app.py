#!/usr/bin/env python3
"""A basic flask app."""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """Configuration class."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    """Select the most suitable locale."""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Handle the index route."""
    return render_template("2-index.html")


if __name__ == '__main__':
    app.run(debug=True)
