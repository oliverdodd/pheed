import xml.dom.minidom

"""
Extend DOM Element
"""

def textValue(self):
	return "".join([e.nodeValue for e in self.childNodes])

def tagValue(self,tag):
	for e in self.getElementsByTagName(tag):
		return e.textValue()

def tagWithAttribute(self,tag,attribute,attributeValue):
	for e in self.getElementsByTagName(tag):
		if (e.getAttribute(attribute) == attributeValue):
			return e
	
def tagValueWithAttribute(self,tag,attribute,attributeValue):
	return self.tagWithAttribute(tag,attribute,attributeValue).textValue()

xml.dom.minidom.Element.textValue = textValue
xml.dom.minidom.Element.tagValue = tagValue
xml.dom.minidom.Element.tagWithAttribute = tagWithAttribute
xml.dom.minidom.Element.tagValueWithAttribute = tagValueWithAttribute