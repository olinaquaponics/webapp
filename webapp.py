#!/usr/bin/env python3
""" Web app for the olin aquaponics club
"""

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
