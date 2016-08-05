
#from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump


template = Element("template")

# context
context = SubElement(template, "context")
SubElement(context, "NETWORK")       .text = "YES"
SubElement(context, "SSH_PUBLIC_KEY").text = "$USER[SSH_PUBLIC_KEY]"

# CPU
SubElement(template, "CPU")          .text = "1"

# DISK
disk = SubElement(template, "DISK")
SubElement(disk, "IMAGE")            .text = "delf3d-worker-os"
SubElement(disk, "IMAGE_UNAME")      .text = "fortissimo-lyklev"

# FEATURES
features = SubElement(template, "FEATURES")
SubElement(features, "ACPI")         .text = "yes"
SubElement(features, "LOCALTIME")    .localtime = "no"

# GRAPHICS
graphics = SubElement(template, "GRAPHICS")
SubElement(graphics, "LISTEN")       .text = "0.0.0.0"
SubElement(graphics, "TYPE")         .text = 'vnc'





dump(template)