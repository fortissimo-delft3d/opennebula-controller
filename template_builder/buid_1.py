
#from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump


template = Element("template")

# context
context = SubElement(template, "context")
SubElement(context, "NETWORK")       .text = "YES"
SubElement(context, "SSH_PUBLIC_KEY").text = "$USER[SSH_PUBLIC_KEY]"

# CPU
cpu = Subelement(template, "

print dump(template)

