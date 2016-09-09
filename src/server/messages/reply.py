from json import dumps

class ReplyBase(object):
    def json(self):
        return dumps(self,
        	default=lambda o: o.__dict__, 
            sort_keys=True,
            indent=4)



class ImportBookmarkDetectedGroup(ReplyBase):
	"""
	Represents the detected possible recepes
	from a web source (i.e.: Tasty or Tastemade)
	"""
	def __init__(self, source, links):
		ReplyBase.__init__(self)
		self.source = source
		self.links = links
