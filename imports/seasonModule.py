from __future__ import print_function
import sys
from bs4 import BeautifulSoup
import requests
import os
import errno

sys.path.append('../imports')

from imports import MyDate, AniEntry

def strOrUnicode(st):
    if isinstance(st, str):
        return st
    elif isinstance(st, unicode):
        return st.encode("utf-8")
    else:
        return -1
   

def main(season, aniDump):
    global toPrint
    global theAnis
     
    isOk = False
    seaDictionary = ["summer", "spring", "fall", "winter"]
    
    #Checking if the input is valid
    while isOk == False:
        #season = raw_input("What season do you want parsed [season][year]: ").lower()
        
        #season = []
        seasonProc = season.split(' ')
    
        i = 0
    
        for s in seasonProc:
            if s.isdigit():
                i += 1
            if not (s.isdigit()):
                if not (s in seaDictionary):
                    i += 1
                
        if i == 1 and len(seasonProc) == 2:
            isOk = True
    
    #aniDump = raw_input("Do you want me to dump the titles of the anime here [y/n]: ")
    
    request = "https://myanimelist.net/anime/season/"
    filename = ""
    
    #The input can be given in either [season][year] or [year][season] format
    if seasonProc[0].isdigit():
        request += seasonProc[0] + "/" + seasonProc[1]
        filename += seasonProc[1].capitalize() + seasonProc[0]
    else:
        request += seasonProc[1] + "/" + seasonProc[0]
        filename += seasonProc[0].capitalize() + seasonProc[1]
    filename += ".xml"
    
    toPrint = "\nParsing website data into XML..." + "\n\t> " + request + "\n"
    
    if __name__ == "__main__":
        print(toPrint)
    
    ############
    #Requests and BeautifulSoup doing work
    req = requests.get(request)
    
    toParse = req.text
    
    soup = BeautifulSoup(toParse, 'html.parser')
    
    allTitles = soup.find_all('a', class_='link-title')
    startTimes = soup.find_all('span', class_="remain-time")
    allProducers = soup.find_all('span', class_="producer")
    allTypes = soup.find_all('div', class_="info")
    #############
    
    titles = []
    links = []
    times = []
    producers = []
    atype = []
    
    #Getting the titles of all of the anime
    #and also all of the links by cutting out the bits between the found indexes
    for title in allTitles:
        titles.append(title.get_text())
        links.append(str(title)[str(title).find('href=')+6:str(title).find('">')])
        
        
    #Getting all of the time and removing some odd whitespace
    for time in startTimes:
        times.append(time.get_text().strip())
    
    #Getting all of the types for the anime
    for ty in allTypes:
        ty = str(ty).strip()
        atype.append(ty[ty.find(">")+1 : ty.find("-")].strip())
        
    
    #Getting all of the producers and not removing whitespace because strip is dumb
    for producer in allProducers:
        producers.append(producer.get_text().strip())
    
    #Are deletes even necessary in Python?
    del allTitles
    del startTimes
    del allProducers
    #Not really iirc
    
    monthMap = {"Jan" : 1, "Feb" : 2, "Mar" : 3, "Apr" : 4, "May" : 5, "Jun" : 6, "Jul" : 7, "Aug" : 8, "Sep" : 9, "Oct" : 10, "Nov" : 11, "Dec" : 12}
    
    dates = []
    
    #Turn the time string into a more manageable Date class
    for time in times:
        time = str(time)
        date = MyDate.MyDate(time[4:5], monthMap[time[0:3]], time[(time.find(',') + 2) : (time.find(',') + 6)])
        dates.append(date)
    
    aniContainer = []
    
    aniDump = aniDump.lower()
    j = 1
    theAnis = ""
    
    #Generate a list of all entry objects with data and then make the XML file
    directory = "./res/saved_seasons/"
    
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXISTS:
            raise
    
    with open(directory + filename, 'a+') as the_file:
        print('<?xml version="1.0" encoding="utf-8"?>', file = the_file)
    
        for i in range(0,len(titles)):
            entry = AniEntry.AniEntry(titles[i], links[i], producers[i], dates[i], atype[i])
            if entry.time.checkSeason(season) and entry.atype == "TV":
                aniContainer.append(entry)
                if(aniDump == "y"):
                    theAnis += str(j) + ". " + entry.title + "\n"
                    j += 1
                    
        if __name__ == "__main__":
            print(theAnis.encode('utf-8'))
    
        for entry in aniContainer:
            print("<anime>", file = the_file)
            print("\t<title>" + strOrUnicode(entry.title) + "</title>", file = the_file)
            print("\t<producer>" + strOrUnicode(entry.producer) + "</producer>", file = the_file)
            print("\t<link>" + strOrUnicode(entry.link) + "</link>", file = the_file)
            print("\t<type>" + strOrUnicode(entry.atype) + "</type>", file = the_file)
            print("\t<date>" + entry.time.toString + "</date>", file = the_file)
            print("</anime>\n", file = the_file)


if __name__ == "__main__":
     season = raw_input("What season do you want parsed [season][year]: ").lower()
     aniDump = raw_input("Do you want me to dump the titles of the anime here [y/n]: ")
     
     main(season, aniDump)