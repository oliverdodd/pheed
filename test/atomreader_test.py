import xml.dom.minidom
import pheed.domelement
from pheed.atomreader import AtomReader
import unittest

class atomreader_test(unittest.TestCase):
	
	def setUp(self):
		self.file = open('atom.xml', 'r')
		self.atomReader = AtomReader()
	
	def tearDown(self):
		self.file.close()

	def test_parse(self):
		feed = self.atomReader.parse(self.file)
		# feed
		self.assertEqual(feed.title, "Edible Oddities")
		self.assertEqual(feed.url, "http://edible-oddities.blogspot.com/")
		self.assertEqual(len(feed.entries), 25)
		# entries
		self.assertEqual(feed.entries[0].title, "Durian")
		self.assertEqual(feed.entries[0].date.isoformat(), "2009-07-16T07:53:00.007000-04:00")
		self.assertEqual(feed.entries[0].link, "http://edible-oddities.blogspot.com/2009/07/durian.html")
		self.assertEqual(feed.entries[0].content[:37], "The kings of myth, legend, and cinema")
	
	def test_parse_limit(self):
		feed = self.atomReader.parse(self.file,5)
		self.assertEqual(len(feed.entries), 5)
	
	def test_load(self):
		feed = self.atomReader.load("http://edible-oddities.blogspot.com/feeds/posts/default")
		self.assertEqual(feed.title, "Edible Oddities")
		self.assertEqual(feed.url, "http://edible-oddities.blogspot.com/")
		self.assertEqual(len(feed.entries), 25)

if __name__ == '__main__':
	unittest.main()