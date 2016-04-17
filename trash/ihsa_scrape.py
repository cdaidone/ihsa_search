# -*- coding: utf-8 -*-
from urllib.request import urlopen
from bs4 import BeautifulSoup
from html.parser import HTMLParser

html = urlopen("https://members.ihsainc.com/publicteaminfo/currentteams.aspx")
bsObj = BeautifulSoup(html, "html.parser")


t = open("schools.py", "w")

t.write("colleges = [")

schoolList = bsObj.find("table", {"id":"MainContent_lvTeamListing_tblLayoutTeamListing"}).findAll("td")

for index in range (0, len(schoolList)):
    t.write("{")
    row1 = schoolList[index].findAll("a")
    college = row1[0]
    coach = row1[1]
    coach = coach.get_text()
    # coach = coach.replace(u'\xa0', u' ')
    coach = ' '.join( coach.split('\xa0\r\n') )
    coach = ' '.join( coach.split() )
    # First split tells the code to split at "\xa0\r\n" and essentially removes it. Then join occurs (PEMDAS), joining it on one space. The 2nd split gets rid of whatever is between the text, then join adds one space.
    mydata = row1[1]

    # cleandata = strip_tags(mydata)
    # print(cleandata)
    # cleandata2 = ' '.join( cleandata.split() )
    # print(cleandata2)

    row2 = schoolList[index].findAll("span")
    state = row2[1]
    t.write("'College'") + t.write(": ") + t.write("'%s',\n" % college.get_text()) + t.write("'State'") + t.write(": ") + t.write("'%s',\n" % state.get_text()) + t.write("'Coach'") + t.write(": ") + t.write("%r" % coach)

    t.write("},")
t.write("]")


t.close()


#print(info.get_text() + "\n" + info2.get_text())
#row2 = schoolList[index].findAll("td")
#info2 = row2[1].get_text()
#t.write("%r" % info2)
#info2 = row1[1].get_text()
#t.write("'Coach'") + t.write(":") + t.write("%r" % info2)
#school_info = index.get_text()
