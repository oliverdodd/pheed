from pheed.rss2reader import RSS2Reader
import unittest

class rss2reader_test(unittest.TestCase):
	
	def setUp(self):
		self.file = open('rss2.xml', 'r')
		self.rss2Reader = RSS2Reader()
	
	def tearDown(self):
		self.file.close()

	def test_parse(self):
		feed = self.rss2Reader.parse(self.file)
		# feed
		self.assertEqual(feed.title, "c01001111de")
		self.assertEqual(feed.url, "http://01001111.net/code")
		self.assertEqual(len(feed.entries), 10)
		# entries
		self.assertEqual(feed.entries[0].title, "Synchronous NSTask")
		self.assertEqual(feed.entries[0].date.isoformat(), "2010-05-19T02:16:52+00:00")
		self.assertEqual(feed.entries[0].link, "http://01001111.net/code/?p=159")
		self.assertEqual(feed.entries[0].content[:109], "<p>The <strong>NSTask</strong> class allows developers to run another program from within a Cocoa Application")
	
	def test_parse_limit(self):
		feed = self.rss2Reader.parse(self.file,5)
		self.assertEqual(len(feed.entries), 5)
		
	def test_load(self):
		feed = self.rss2Reader.load("http://01001111.net/code/?feed=rss2")
		self.assertEqual(feed.title, "c01001111de")
		self.assertEqual(feed.url, "http://01001111.net/code")
		self.assertEqual(len(feed.entries), 10)

if __name__ == '__main__':
	unittest.main()