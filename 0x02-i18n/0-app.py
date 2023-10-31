#!/usr/bin/env python3
"""
create flask server
"""
from flask import Flask, render_template


app = Flask(__name__)


@app.get("/")
def index():
    """
    print Hello world
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    app.run()
