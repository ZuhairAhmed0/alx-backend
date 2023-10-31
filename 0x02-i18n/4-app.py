#!/usr/bin/env python3
"""
create flask server
"""
from flask import Flask, render_template, request
from flask_babel import Babel, gettext


class Config:
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


def get_locale():
    """
    Determine the best match with our supported languages.
    """
    locale = request.args.get("locale", "").strip()
    if locale and locale in Config.LANGUAGES:
        return locale
    return request.accept_languages.best_match(app.config["LANGUAGES"])


babel.init_app(app, locale_selector=get_locale)


@app.route("/")
def index():
    """
    Print Hello world
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run()
