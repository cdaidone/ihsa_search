from urllib.request import urlopen
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import csv

html = urlopen("https://members.ihsainc.com/publicteaminfo/currentteams.aspx")
bsObj = BeautifulSoup(html, "html.parser")

schoolList = bsObj.find("table", {"id":"MainContent_lvTeamListing_tblLayoutTeamListing"}).findAll("td")

with open('schools2.csv', 'w') as csvfile:
    fieldnames = ['School', 'State', 'Coach']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    #Need .writeheader() so that app knows what data to grab. It's ".writeheader()" not .header().
    for index in range (0, len(schoolList)):
        row1 = schoolList[index].findAll("a")
        college = row1[0]
        college = college.get_text()
        coach = row1[1]
        coach = coach.get_text()
        coach = ' '.join( coach.split('\xa0\r\n') )
        coach = ' '.join( coach.split() )
        # First split tells the code to split at "\xa0\r\n" and essentially removes it. Then join occurs (PEMDAS), joining it on one space. The 2nd split gets rid of whatever is between the text, then join adds one space.
        row2 = schoolList[index].findAll("span")
        state = row2[1]
        state = state.get_text()
        writer.writerow({'School': college, 'State': state, 'Coach': coach})
    #print('School': college, 'State': state, 'Coach': coach)
