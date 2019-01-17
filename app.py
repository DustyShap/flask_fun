from flask import Flask, render_template, request, jsonify, redirect, url_for, abort
import requests

app = Flask(__name__)

ENDPOINT = 'http://raymondberg.com/story/lists/data/list_master.json'

@app.route('/')
def index():
    return redirect(url_for('picklechips'))

@app.route('/picklelist')
def picklelist():
    return redirect(url_for('picklechips'))

@app.route('/picklelist/all', methods=['GET', 'POST'])
def picklechips():
    if request.method == 'POST':
        ranked_chip = int(request.form['rank'])
        if ranked_chip >= len(pickle_chips()):
            return 'Out of range!'
        return pickle_chips()[ranked_chip-1]
    return render_template('index.html', chip_list=pickle_chips())

@app.route('/picklelist/<int:rank>')
def pickleranks(rank):
    #try except
    try:
        ranked_chip = pickle_chips()[rank-1]
        return ranked_chip
    except IndexError:
        return abort(404)


@app.route('/picklelist/json')
def picklejson():
    return jsonify(pickle_chips())

def pickle_chips():
    request = requests.get(ENDPOINT)
    return request.json()['lists'][4]['simple_items']

if __name__ == '__main__':
    app.run(debug=True)
