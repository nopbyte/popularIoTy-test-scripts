import time
import datetime
import random
#import json
import simplejson as json
import httplib, urllib
import sys

class ES():
  def __init__(self, config):
        self.host = config.get('elasticsearch','host')
        self.port = config.get('elasticsearch','port')
        self.path= config.get('elasticsearch','path')
        self.timeframe = config.getint('sample-creation','timeframe')

  def generateRandomTime(self):
       now = datetime.datetime.now()
       now += datetime.timedelta(seconds=random.randint(1, self.timeframe))
       return time.mktime(now.timetuple())*1000
     
  
  def insert_data_ES(self, src_soid, src_stream, dest_soid, dest_stream, events, usage):
     base = random.randint(1,sys.maxint/2)
     for e in range (int(events)):
        data = self.insert_document_ES(base+e,src_soid,src_stream,dest_soid,dest_stream,True,self.generateRandomTime())
     for u in range(int(usage)):
        data = self.insert_document_ES(base+events+u,src_soid,src_stream,dest_soid,dest_stream,False,self.generateRandomTime())
        
  def put_document_ES(self, data, id):
        conn = httplib.HTTPConnection(
                        host=self.host,
                        port=self.port,
                )
        conn.request(
                method="PUT",
                url=self.path+'/'+str(id),
                body=json.dumps(data)
        )
        response=conn.getresponse()
        print response.status, response.reason


  def insert_document_ES(self, id, src_soid, src_stream, dest_soid, dest_stream, event, timestamp):
     f = open('templates/popularity.json', 'r+')
     document = f.read()
     f.close()
     data = json.loads(document)
     data['src']['soid']=src_soid
     data['src']['streamid']=src_stream
     data['dest']['soid']=dest_soid
     data['dest']['streamid']=dest_stream
     data['event']=event
     data['date']=timestamp
     self.put_document_ES(data,id)
     print "update: "+json.dumps(data)
     return data

   
