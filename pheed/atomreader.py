"""	AtomReader - read a subset of information from an atom feed
"""
from datetime import datetime
from dateutil import parser
from pheed import domelement
from pheed.feed import Feed
from pheed.feedentry import FeedEntry
from pheed.abstractfeedreader import AbstractFeedReader

class AtomReader (AbstractFeedReader):
	
	def parseDocument(self,document,limit=None):
		root = document.getElementByTagName("feed")
		if root.tagName == None:
			return None
		feed = Feed()
		feed.title = root.tagValue("title")
		feed.url = root.getElementWithAttribute("link","rel","alternate").getAttribute("href")
		feed.entries = self.parseEntries(document.getElementsByTagName("entry"),limit,feed)
		return feed

	def parseEntry(self,entryNode,feed=None):
		entry = FeedEntry()
		entry.title = entryNode.tagValue("title")
		entry.date = parser.parse(entryNode.tagValue("published"))
		entry.link = entryNode.getElementWithAttribute("link","rel","alternate").getAttribute("href")
		entry.author = entryNode.getElementByTagName("author").tagValue("name")
		entry.content = entryNode.tagValue("content")
		entry.feed = feed
		return entry
	
