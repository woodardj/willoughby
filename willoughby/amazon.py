from amazonproduct import API
import pprint

class AmazonChecker(object):
  def __init__(self):
    AWS_KEY = '***REMOVED***'
    SECRET_KEY = '***REMOVED***'
    ASSOCIATE_TAG = 'stream0a-20'
    
    self.api = API(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG)
    #self.api = JSONAPI(AWS_KEY, SECRET_KEY, 'us')
  
  def availability(self, needle):
    #Instant Video browse node: 16261631 or maybe 2649513011
    #api.call(Operation='ItemSearch', SearchIndex='Video') #US/Video? 493964
    #data = self.api.browse_node_lookup(16261631)
    
    params = {
      #'SearchIndex':'Movies',
      'Title':'Inception'
      #'ReponseGroup':'Medium',
      #'IdType':'ASIN'
    }
    
    #data = self.api.item_lookup('B0047WJ11G', **params)
    #data = self.api.item_lookup('Inception', **params)
    data = self.api.item_search('Movies',**params)
    
    pp = pprint.PrettyPrinter(indent=3)
    pp.pprint( dir(data['Items']['Item']) )
    return data