# app.py

from flask import Flask, render_template, request, redirect, url_for
from matrix.py import Matrix

app = Flask(__name__)
matrix = Matrix()

@app.route('/')
def index():
    return render_template('index.html', matrix=matrix.get_matrix())

@app.route('/add_row', methods=['POST'])
def add_row():
    matrix.add_row()
    return redirect(url_for('index'))

@app.route('/add_column', methods=['POST'])
def add_column():
    matrix.add_column()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
