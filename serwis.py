import web
import xml.etree.ElementTree as ET
import json

#xmlp = ET.XMLParser(encoding="utf-8")
#tree = ET.parse('data.xml',parser=xmlp)
#root = tree.getroot()

with open("data.xml", 'r') as xml_file:
    xml_tree = ET.parse(xml_file)
#tree = ET.parse('data.xml')
#root = tree.getroot()
root = xml_tree.getroot()

urls = (
    '/organizations', 'list_organizations',
    '/organizations/(.*)', 'get_organization'
)

app = web.application(urls, globals())

class list_organizations:        
    def GET(self):
        output = '[';
        for child in root:
            print (child.attrib)
            #print ("child", child.tag, child.attrib)
            #output += json.dumps(child.attrib) + ','
        #output += ']';
            output += json.dumps(child.attrib) + ',' 
        output = output[:-1]
        output += ']'
        return output

class get_organization:
    def GET(self, org):
        for child in root:
            if child.attrib['key'] == org:
                return str(child.attrib)

if __name__ == "__main__":
    app.run()
