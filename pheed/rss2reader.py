"""	RSS2Reader - read a subset of information from an RSS2 feed
"""
from datetime import datetime
from dateutil import parser
from pheed import domelement
from pheed.feed import Feed
from pheed.feedentry import FeedEntry
from pheed.abstractfeedreader import AbstractFeedReader

class RSS2Reader (AbstractFeedReader):
	
	def parseDocument(self,document,limit=None):
		root = document.getElementByTagName("rss").getElementByTagName("channel")
		if root.tagName == None:
			return None
		feed = Feed()
		feed.title = root.tagValue("title")
		feed.url = root.tagValue("link")
		feed.entries = self.parseEntries(document.getElementsByTagName("item"),limit,feed)
		return feed
	
	def parseEntry(self,entryNode,feed=None):
		entry = FeedEntry()
		entry.title = entryNode.tagValue("title")
		entry.date = parser.parse(entryNode.tagValue("pubDate"))
		entry.link = entryNode.tagValue("link")
		entry.content = entryNode.tagValue("content:encoded")
		entry.feed = feed
		return entry
