class ES():
  def __init__(self, config):
        self.host = config.get('elasticsearch','host')
        self.port = config.get('elasticsearch','port')
        self.path= config.get('elasticsearch','path')
        self.timeframe = config.get('sample-creation','timeframe')
  
  def insert_data_ES(self, src_soid, src_stream, dest_soid, dest_stream, events, usage):
     return
  def insert_document_ES(self, src_soid, src_stream, dest_soid, dest_stream, event, timestamp):
     return
