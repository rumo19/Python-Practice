"""
Here is a simple application that parses some XML and extracts some data elements from the XML:

"""

import xml.etree.ElementTree as ET
data='''
<person>
<name> Kamrul </name>
<phone type="intl">
01547899090
</phone>
<email hide="yes" />
</person>
'''
tree=ET.fromstring(data)
print('Name: ', tree.find('name').text)
print('Attr: ', tree.find('email').get('hide'))
# Code: http://www.py4e.com/code3/xml1.py
