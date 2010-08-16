"""	AbstractFeedReader Class - read a subset of information from a feed
"""
import urllib2
import xml.dom.minidom
from pheed import domelement

class AbstractFeedReader:
	
	def fetch(self,url):
		""" Fake FeedBurner user agent to bypass feedburner redirection """
		req = urllib2.Request(url,headers = {'User-Agent' : 'FeedBurner/1.0 (http://www.FeedBurner.com)'})
		return urllib2.urlopen(req)
		
	def load(self,url,limit=None):
		return self.parse(self.fetch(url),limit)

	def parse(self,handle,limit=None):
		return self.parseDocument(xml.dom.minidom.parse(handle),limit)
	
	def parseString(self,xmlString,limit=None):
		return self.parseDocument(xml.dom.minidom.parseString(xmlString),limit)
	
	def parseDocument(self,document,limit=None): abstract
	
	def parseEntries(self,entryNodes,limit=None,feed=None):
		entries = []
		i = 0
		for e in entryNodes:
			if (limit != None) and (i >= limit):
				break
			entries.append(self.parseEntry(e,feed))
			i += 1
		return entries
	
