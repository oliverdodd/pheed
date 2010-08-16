"""	FeedReader Class - Autodectect and read a subset of information from an RSS2 or Atom feed
"""
from pheed import domelement
from pheed.feed import Feed
from pheed.feedentry import FeedEntry
from pheed.abstractfeedreader import AbstractFeedReader
from pheed.atomreader import AtomReader
from pheed.rss2reader import RSS2Reader

class FeedReader (AbstractFeedReader):
	
	reader = None
	
	def getReader(self,document):
		# atom ?
		if document.getElementByTagName("feed").tagName:
			return AtomReader()
		# rss2?
		elif document.getElementByTagName("rss").tagName:
			return RSS2Reader()
		return None

	def parseDocument(self,document,limit=None):
		self.reader = self.getReader(document)
		return self.reader.parseDocument(document,limit)

	def parseEntry(self,entryNode,feed=None):
		return self.reader.parseEntry(entryNode,feed)
	
