import urllib2
from bs4 import BeautifulSoup
import json

with open('secure.txt', 'r') as f:
    api_key = f.readline()

print 'win'

r = urllib2.urlopen('http://api.nal.usda.gov/ndb/reports/?ndbno=01009&type=f&format=json&'
                'api_key=' + api_key)
soup = BeautifulSoup(r)
nd = json.loads(soup.text)
print 'win'