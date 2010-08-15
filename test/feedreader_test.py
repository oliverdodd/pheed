import xml.dom.minidom
import pheed.domelement
from pheed.atomreader import AtomReader
from pheed.rss2reader import RSS2Reader
from pheed.feedreader import FeedReader
import unittest

class feedreader_test(unittest.TestCase):
	
	def test_getReader_atom(self):
		r = FeedReader()
		f = open('atom.xml', 'r')
		self.assertEqual(type(r.getReader(xml.dom.minidom.parse(f))), type(AtomReader()))
	
	def test_getReader_rss2(self):
		r = FeedReader()
		f = open('rss2.xml', 'r')
		self.assertEqual(type(r.getReader(xml.dom.minidom.parse(f))), type(RSS2Reader()))
	
	def test_getReader_none(self):
		r = FeedReader()
		s = """
		<test>
			<title>DOM Element Extension Test</title>
			<url ref="homepage">http://01001111.net</url>
			<url ref="documentation">http://docs.python.org</url>
		</test>
		"""
		d = xml.dom.minidom.parseString(s)
		self.assertEqual(r.getReader(d), None)
	
	def test_parse_atom(self):
		r = FeedReader()
		f = open('atom.xml', 'r')
		feed = r.parse(f)
		# feed
		self.assertEqual(feed.title, "Edible Oddities")
		self.assertEqual(feed.url, "http://edible-oddities.blogspot.com/")
		self.assertEqual(len(feed.entries), 25)
		# entries
		self.assertEqual(feed.entries[0].title, "Durian")
		self.assertEqual(feed.entries[0].date.isoformat(), "2009-07-16T07:53:00.007000-04:00")
		self.assertEqual(feed.entries[0].link, "http://edible-oddities.blogspot.com/2009/07/durian.html")
		self.assertEqual(feed.entries[0].content[:37], "The kings of myth, legend, and cinema")
	
	def test_parse_rss2(self):
		r = FeedReader()
		f = open('rss2.xml', 'r')
		feed = r.parse(f)
		# feed
		self.assertEqual(feed.title, "c01001111de")
		self.assertEqual(feed.url, "http://01001111.net/code")
		self.assertEqual(len(feed.entries), 10)
		# entries
		self.assertEqual(feed.entries[0].title, "Synchronous NSTask")
		self.assertEqual(feed.entries[0].date.isoformat(), "2010-05-19T02:16:52+00:00")
		self.assertEqual(feed.entries[0].link, "http://01001111.net/code/?p=159")
		self.assertEqual(feed.entries[0].content[:89], "The NSTask class allows developers to run another program from within a Cocoa Application")

if __name__ == '__main__':
	unittest.main()