
#from xml.etree import ElementTree
from xml.etree.ElementTree import Element, SubElement, dump


template = Element("template")


# CPU
SubElement(template, "CPU")          .text = "1"

# VCPU
SubElement(template, "VCPU")         .text = "1"


# MEMORY
SubElement(template, "MEMORY")       .text = "2048"

# DISK
disk = SubElement(template, "DISK")
SubElement(disk, "IMAGE")            .text = "delf3d-worker-os"
SubElement(disk, "IMAGE_UNAME")      .text = "fortissimo-lyklev"

# os
os = SubElement(template, "OS")
SubElement(os, "ARCH")               .text = "x86_64"

# context
context = SubElement(template, "context")
SubElement(context, "NETWORK")       .text = "YES"
SubElement(context, "SSH_PUBLIC_KEY").text = "$USER[SSH_PUBLIC_KEY]"

# NIC (Network interfaces)
nic = SubElement(template, "NIC")
nic_0 = SubElement(nic, "0")
SubElement(nic_0, "NETWORK")         .text = "internet"
SubElement(nic_0, "NETWORK_UNAME")   .text = "oneadmin"

nic_1 = SubElement(nic, "1")
SubElement(nic_0, "NETWORK")         .text = "fortissimo-surfsara.int"
SubElement(nic_0, "NETWORK_UNAME")   .text = "fortissimo-lyklev"


# FEATURES
features = SubElement(template, "FEATURES")
SubElement(features, "ACPI")         .text = "yes"
SubElement(features, "LOCALTIME")    .text = "no"

# GRAPHICS
graphics = SubElement(template, "GRAPHICS")
SubElement(graphics, "LISTEN")       .text = "0.0.0.0"
SubElement(graphics, "TYPE")         .text = "vnc"

dump(template)