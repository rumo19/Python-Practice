"""
Looping through nodes
Often the XML has multiple nodes and we
 need to write a loop to process all of the nodes. 
 In the following program, 
 we loop through all of the user nodes:"


"""

import xml.etree.ElementTree as ET 
input= '''
<stuff>
<users>
<user x="2">
<id> 001 </id>
<name> Kamrul </name>
</user>
<user x="7">
<id> 002 </id>
<name> Hasan </name>
</user>
</users>
</stuff>
'''
stuff=ET.fromstring(input)
lst=stuff.findall('users/user')
print('User count: ', len(lst))
for item in lst:
    print('Name', item.find('name').text)
    print('Id ', item.find('id').text)
    print('Attribute', item.get("x"))
#Code: http://www.py4e.com/code3/xml2.py
