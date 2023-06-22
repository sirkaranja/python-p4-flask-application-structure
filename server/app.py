#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)

@app.route('/<string:username>')
def user(username):
    return f'<h1>Profile for {username}</h1>'
