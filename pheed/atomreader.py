"""	AtomReader
	Copyright (c) 2010 Oliver C Dodd
	Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
"""
from datetime import datetime
from dateutil import parser
from pheed import domelement
from pheed.feed import Feed
from pheed.feedentry import FeedEntry
from pheed.feedreader import FeedReader

class AtomReader (FeedReader):
	
	def parseDocument(self,document,limit=None):
		feeds = document.getElementsByTagName("feed")
		if len(feeds) <= 0:
			return None
		root = feeds[0]
		feed = Feed()
		feed.title = root.tagValue("title")
		feed.url = root.getElementWithAttribute("link","rel","alternate").getAttribute("href")
		feed.entries = self.parseEntries(document.getElementsByTagName("entry"))
		return feed

	def parseEntry(self,entryNode):
		entry = FeedEntry()
		entry.title = entryNode.tagValue("title")
		entry.date = parser.parse(entryNode.tagValue("published"))
		entry.link = entryNode.getElementWithAttribute("link","rel","alternate").getAttribute("href")
		entry.author = entryNode.getElementByTagName("author").tagValue("name")
		entry.content = entryNode.tagValue("content")
		return entry
	
