from pyflix2 import *

class NetflixChecker(object):
  def __init__(self):
    self.api = NetflixAPIV2('FindStream','d4ug96pzrrgctwsa4srk883b','6J4PsutRHE')
  
  def availability(self, title):
    results = self.api.search_titles(title)
    title_id = results['catalog'][0]['id']
    data = self.api.get_title(title_id,"format_availability")
    
    #print data
    
    rval = []
    rval.append({"service":"netflix-instant","available": True if 'instant' in data['delivery_formats'] else False})
    rval.append({"service":"netflix-dvd","available": True if 'DVD' in data['delivery_formats'] else False})
    rval.append({"service":"netflix-bluray","available": True if 'Blu-ray' in data['delivery_formats'] else False})
    return rval