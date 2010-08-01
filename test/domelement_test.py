import xml.dom.minidom
import pheed.domelement
import unittest

class domelement_test(unittest.TestCase):
	
	def setUp(self):
		self.xmlString = """
		<test>
			<title>DOM Element Extension Test</title>
			<url ref="homepage">http://01001111.net</url>
			<url ref="documentation">http://docs.python.org</url>
		</test>
		"""
		self.document = xml.dom.minidom.parseString(self.xmlString)
		self.rootNode = self.document.firstChild
	
	def test_getElementByTagName(self):
		self.assertEqual(self.rootNode.getElementByTagName("title").textValue(), "DOM Element Extension Test")
		self.assertEqual(self.rootNode.getElementByTagName("invalid").textValue(), "")
		
	def test_getElementWithAttribute(self):
		self.assertEqual(self.rootNode.getElementWithAttribute("url","ref","homepage").textValue(),"http://01001111.net")
		self.assertEqual(self.rootNode.getElementWithAttribute("url","ref","invalid").textValue(),"")

	def test_tagValue(self):
		self.assertEqual(self.rootNode.tagValue("title"), "DOM Element Extension Test")

	def test_tagValueWithAttribute(self):
		self.assertEqual(self.rootNode.tagValueWithAttribute("url","ref","homepage"),"http://01001111.net")
		self.assertEqual(self.rootNode.tagValueWithAttribute("url","ref","documentation"),"http://docs.python.org")
		

if __name__ == '__main__':
	unittest.main()