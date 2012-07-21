import urllib2, urllib
import json

class ImdbLookup(object):
  def __init__(self):
    self.api_url = "http://www.imdbapi.com/?"
    
  def search(self, needle):
    result = urllib2.urlopen(self.api_url + urllib.urlencode({'t':needle})).read()
    
    print result
    
    return json.loads(result)