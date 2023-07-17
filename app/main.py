from flask import Flask, render_template, request, url_for, redirect
import gzip
import pickle as pk
from SBERT.API import Recommender



app = Flask(__name__)

@app.route('/results', methods=['POST'])
def result():
    query = request.form['query']
    result = Recommender.predict(query)
    return render_template('result.html', result=result)


@app.route('/')
def getrec():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)