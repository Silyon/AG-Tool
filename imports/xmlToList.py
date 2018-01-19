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
        pic = child.find('picture').text
        
       # print ("Title: " + title + "\nProducer: " + prod + "\nLink: " + link +
        #       "\nType: " + typ + "\nDate: " + date + "\n")
        
        entry = AniEntry.AniEntry(title, link, prod, date, pic, typ)
        aniList.append(entry)
        
    return aniList
        
        
def xmlToMatrix(xml):
    aniMatrix = []
    tree = ET.parse(xml)
    root = tree.getroot()
    nr = 1
    
    for child in root.findall('anime'):
        aniList = []
       
        title = child.find('title').text
        prod = child.find('producer').text
        typ = child.find('type').text
        date = child.find('date').text
        
        aniList.append(nr);
        nr += 1
        aniList.append(title);
        aniList.append(prod);
        aniList.append(typ);
        aniList.append(date);
      
        
        aniMatrix.append(aniList)
        
    return aniMatrix
       
        
if __name__ == "__main__":
    xmlToList("../res/saved_seasons/Winter2018.xml")