from flask import Flask, url_for
from flask import render_template
from flask import request
from urllib2 import *
import simplejson

def printSeparator(character='*', times=50):
    print(character * times)

app = Flask(__name__)
"""
@app.route('/')
def hello_world():
    return 'Hello, World!'
"""


@app.route('/results/')
#@app.route('/results/<name>')
def getResults(query=None):

    url_for('static', filename='share.png')
    url_for('static', filename='3.points-2.png')

    if request.method == 'POST':
        print('post method!!!!')
    else:
        print('get method!!!!')
        #print('*get*', request.args["queryString"])

    #print('*', request.query_string, '*')
    queryString = request.query_string

    url = 'http://206.12.100.91:8983/solr/sme/select?q='+ queryString + '&wt=json&rows=100'

    connection = urlopen(url)
    response = simplejson.load(connection)
    print(response['response']['numFound'], "documents found.")


    return render_template('pure.results.html', results=response['response']['docs'])

    printSeparator()
