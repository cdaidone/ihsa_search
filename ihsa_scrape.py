from urllib.request import urlopen
from bs4 import BeautifulSoup

html = urlopen("https://members.ihsainc.com/publicteaminfo/currentteams.aspx")
bsObj = BeautifulSoup(html, "html.parser")

t = open("schools.py", "w")

t.write("schools = [")

schoolList = bsObj.find("table", {"id":"MainContent_lvTeamListing_tblLayoutTeamListing"}).findAll("td")
for index in range (0, len(schoolList)):
    t.write("{")
    row1 = schoolList[index].findAll("a")
    college = row1[0]
    coach = row1[1]
    row2 = schoolList[index].findAll("span")
    state = row2[1]
    t.write("%s,\n" % college.get_text()) + t.write("%s,\n" % state.get_text()) + t.write("%s\n" % coach.get_text())

    #print(info.get_text() + "\n" + info2.get_text())
    #row2 = schoolList[index].findAll("td")
    #info2 = row2[1].get_text()
    #t.write("%r" % info2)
    #info2 = row1[1].get_text()
    #t.write("'Coach'") + t.write(":") + t.write("%r" % info2)
    #school_info = index.get_text()
    t.write("}")
t.write("]")

t.close()
