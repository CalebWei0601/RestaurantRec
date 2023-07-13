from flask import Flask, render_template, request, url_for, redirect
import pickle as pk


app = Flask(__name__)

@app.route('/result')
def result(query):
    return Recommender.predict(query)


@app.route('/ask', methods=['POST', 'GET'])
def getrec():
    if request.method == 'POST':
        query = request.form['query']
        return redirect(url_for('result'), query=query)
    else:
        query = request.args.get('query')
        return redirect(url_for('result'), query=query)

if __name__ == '__main__':
    app.run(debug=True)