#!/usr/bin/python3
from datetime import datetime
from flask import Flask, g, render_template, request, abort, session, url_for, redirect
from jinja2 import TemplateNotFound

app = Flask(__name__)
app.secret_key = '26682bea5f914ef84a779f0a7a678432'

now = datetime.now()


@app.route('/')
def index():
    return f"Hello World! {now}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7000, debug=True)
