from flask import Flask, render_template, url_for, request, redirect
from random import choice
from datetime import datetime

app = Flask(__name__)

names = ['Jean-Max', 'Louis', 'Louis-Antoine', 'Jacques', 'François', 'Maxime', 'Eloi', 'Antoine', 'Audrey', 'Justine', 'Émilie', 'Guillaume', 'Martin', 'Justin']

@app.route('/')
def index(name=None):
    return render_template('index.html', name=choice(names).upper())

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')