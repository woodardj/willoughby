from amazonproduct import API, NoExactMatchesFound
import pprint

class AmazonChecker(object):
  def __init__(self):
    AWS_KEY = ''
    SECRET_KEY = ''
    ASSOCIATE_TAG = 'stream0a-20'
    
    self.api = API(AWS_KEY, SECRET_KEY, 'us', ASSOCIATE_TAG)
    #self.api = JSONAPI(AWS_KEY, SECRET_KEY, 'us')
  
  def availability(self, needle):
    #Instant Video browse node: 16261631 or maybe 2649513011
    #api.call(Operation='ItemSearch', SearchIndex='Video') #US/Video? 493964
    #data = self.api.browse_node_lookup(16261631)
    
    #data = self.api.item_lookup('B0047WJ11G', **params)
    #data = self.api.item_lookup('Inception', **params)
    
    #data = self.api.item_search("DVD", Title="Inception", ResponseGroup="Large")
    try:
      data = self.api.item_search("Video", Title=needle, BrowseNode="16261631")
    except NoExactMatchesFound:
      return [{"service":"amazon-instant", "available":False}]
    
    #print data
    #print dir(data)
    
    #for root in data:
    #  print "root"
    #  print dir(root.Items.Item.ItemAttributes)
    #  print root.Items.Item.ItemAttributes.Title
    
    #pp = pprint.PrettyPrinter(indent=3)
    return [{"service":"amazon-instant", "available":True}]
