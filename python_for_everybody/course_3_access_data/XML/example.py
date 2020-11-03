import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chack</name>
    <phone type="intl">
    +1 742 787 2727
    </phone>
    <email hide="yes"/>
</person>'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr', tree.find('email').get('hide'))