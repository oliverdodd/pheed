"""	Feed Class - object containing information read from a feed
 	Copyright (c) 2010 Oliver C Dodd

	Licensed under the MIT license: http://www.opensource.org/licenses/mit-license.php
"""
class Feed:
	title = ''
	url = ''
	entries = []
	
	def __init__(self, title = '', url = '', entries = []):
		self.title = title
		self.url = url
		self.add_entries(entries)
	
	def add_entry(self, entry):
		self.entries.push(entry)
	
	def add_entries(self, entries):
		self.entries.extend(entries)
