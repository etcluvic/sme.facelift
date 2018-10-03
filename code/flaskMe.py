from flask import Flask, url_for
from flask import render_template
from flask import request
from urllib2 import *
from bs4 import BeautifulSoup
import simplejson
import os
import codecs

def printSeparator(character='*', times=50):
    print(character * times)

#elevation file - begin
elevationFile = 'elevationFiles/2018-10-02_21-00-07-646785.xml'

f = codecs.open(os.path.join(elevationFile),'r','utf-8')
content = f.read()
f.close()

smKeywords = []
efSoup = BeautifulSoup(content, 'lxml')
queryElements = efSoup.find_all('query')
for qe in queryElements:
    if qe.has_attr('text'):
        smKeywords += qe['text'].split()

#remove duplicates by turning the list into a set
smKeywords = sorted(list(set(smKeywords)))
print(type(smKeywords))
#print(smKeywords)
#elevation file - end

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


    return render_template('pure.results.sm.html', results=response['response']['docs'], smk=smKeywords)

    printSeparator()
