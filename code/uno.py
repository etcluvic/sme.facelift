from urllib2 import *
import simplejson
connection = urlopen('http://206.12.100.91:8983/solr/sme/select?q=atari&wt=json')
response = simplejson.load(connection)
print response['response']['numFound'], "documents found."

# Print the name of each document.

for document in response['response']['docs']:
  print('title:', document['title'])
  print('set:',  document['set'])
  print('text:', document['text'])
  print('doi:', document['doi'])
  print('keywords:', document['keywords'])
  print('*' * 50)
