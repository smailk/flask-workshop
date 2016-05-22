# -*- coding: utf-8 -*-
"""
Created on Sun May 22 16:10:37 2016

@author: Smail Kozarcanin
"""

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    author = "Me"
    name = "You"
    return render_template('index1.html', author=author, name=name)

if __name__ == '__main__':
    app.run()