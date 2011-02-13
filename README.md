pheed
======
Simple python feed reader (atom and rss2) for aggregating links to blog posts.

Usage
-----
	url = "http://example.com/atom.xml"
	limit = 10
	
	feed = FeedReader().load(url,limit)
	print feed.title
	print feed.url
	
	for entry in feed.entries:
		print entry.title
		print entry.date
		print entry.link
		print entry.author
		print entry.content
