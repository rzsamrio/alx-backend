#!/usr/bin/env python3
"""A basic flask app."""
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """Configuration class."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABLE_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Get the logged in user."""
    try:
        user_id = int(request.args.get("login_as"))
    except (ValueError, TypeError):
        return None
    return users.get(user_id)


@app.before_request
def before_request():
    """Store the current user if any."""
    user = get_user()
    if user is not None:
        g.user = user


@babel.localeselector
def get_locale():
    """Select the most suitable locale."""
    user = get_user()
    langs = app.config["LANGUAGES"]
    if request.args.get("locale") in langs:
        return request.args.get("locale")
    elif user is not None and user.get("locale") in langs:
        return user.get("locale")
    else:
        return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """Handle the index route."""
    return render_template("6-index.html")


if __name__ == '__main__':
    app.run(debug=True)
