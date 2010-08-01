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
	
	#Wed, 19 May 2010 02:16:52 +0000
	dateFormat = "%a, %d %b %Y %H:%M:%S %z"
	
	def parseDocument(self,document,limit=None):
		feeds = document.getElementsByTagName("rss")
		if len(feeds) <= 0:
			return None
		root = feeds[0].getElementsByTagName("channel")[0]
		feed = Feed()
		feed.title = root.tagValue("title")
		feed.url = root.tagValue("link")
		feed.entries = self.parseEntries(document.getElementsByTagName("item"))
		return feed
	
	def parseEntry(self,entryNode):
		entry = FeedEntry()
		entry.title = entryNode.tagValue("title")
		entry.date = parser.parse(entryNode.tagValue("pubDate"))
		entry.link = entryNode.tagValue("link")
		entry.content = entryNode.tagValue("description")
		return entry
