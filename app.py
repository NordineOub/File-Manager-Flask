from flask import Flask
from flask import Flask, flash, redirect, render_template, request, session, abort
import os

app = Flask(__name__, template_folder='Template', static_folder='Static')


@app.route('/', methods = ['GET', 'POST'])
def home():
    return render_template('login.html')

@app.route('/main', methods = ['GET', 'POST'])
def main():
    return render_template('page1.html')
    
@app.route('/documents',methods = ['GET', 'POST'])
def documents():
    return render_template('documents.html')
    

@app.route('/quisommes',methods = ['GET', 'POST'])
def quisommes():
    return render_template('quisommesnous.html')
    

if __name__ == "__main__":
    app.secret_key = os.urandom(12)
    app.run(debug=True)
    