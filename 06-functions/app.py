# app.py
from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/run_python', methods=['POST'])
def run_python():
    try:
        code = request.form['python_code']
        result = subprocess.check_output(['python', '-c', code], text=True)
        return result
    except Exception as e:
        return str(e)

if __name__ == '__main__':
    app.run(debug=True)
