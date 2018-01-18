import AniEntry
import xml.etree.ElementTree as ET

def xmlToList(xml):
    aniList = []
    tree = ET.parse(xml)
    root = tree.getroot()
    
    for child in root.findall('anime'):
        title = child.find('title').text
        prod = child.find('producer').text
        link = child.find('link').text
        typ = child.find('type').text
        date = child.find('date').text
        
       # print ("Title: " + title + "\nProducer: " + prod + "\nLink: " + link +
        #       "\nType: " + typ + "\nDate: " + date + "\n")
        
        entry = AniEntry.AniEntry(title, link, prod, date, typ)
        aniList.append(entry)
        
    return aniList
        
        
       
        
if __name__ == "__main__":
    xmlToList("../res/saved_seasons/Winter2018.xml")