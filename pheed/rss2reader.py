"""	RSS2Reader Class - Read a subset of information from RSS and Atom feeds
	Copyright (c) 2010 Oliver C Dodd
	
	Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
"""
from datetime import datetime
from dateutil import parser
from pheed import domelement
from pheed.feed import Feed
from pheed.feedentry import FeedEntry
from pheed.feedreader import FeedReader

class RSS2Reader (FeedReader):
	
	def parseDocument(self,document,limit=None):
		root = document.getElementByTagName("rss").getElementByTagName("channel")
		if root.tagName == None:
			return None
		feed = Feed()
		feed.title = root.tagValue("title")
		feed.url = root.tagValue("link")
		feed.entries = self.parseEntries(document.getElementsByTagName("item"),limit)
		return feed
	
	def parseEntry(self,entryNode):
		entry = FeedEntry()
		entry.title = entryNode.tagValue("title")
		entry.date = parser.parse(entryNode.tagValue("pubDate"))
		entry.link = entryNode.tagValue("link")
		entry.content = entryNode.tagValue("description")
		return entry
