import xml.dom.minidom
"""
Extend DOM Element
"""
def textValue(self):
	return "".join([e.nodeValue for e in self.childNodes])
xml.dom.minidom.Element.textValue = textValue

def getElementByTagName(self,tag):
	for e in self.getElementsByTagName(tag):
		return e
	return xml.dom.minidom.Element(None)
xml.dom.minidom.Element.getElementByTagName = getElementByTagName

def getElementWithAttribute(self,tag,attribute,attributeValue):
	for e in self.getElementsByTagName(tag):
		if (e.getAttribute(attribute) == attributeValue):
			return e
	return xml.dom.minidom.Element(None)
xml.dom.minidom.Element.getElementWithAttribute = getElementWithAttribute
	
def tagValue(self,tag):
	return self.getElementByTagName(tag).textValue()
xml.dom.minidom.Element.tagValue = tagValue
	
def tagValueWithAttribute(self,tag,attribute,attributeValue):
	return self.getElementWithAttribute(tag,attribute,attributeValue).textValue()
xml.dom.minidom.Element.tagValueWithAttribute = tagValueWithAttribute