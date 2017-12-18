########################################################################
##   @@@@@@  @@@@@@ @               @  @@@@@@  @          @@@@@@      ##
##        @  @       @             @   @       @          @           ##
##        @  @@@@     @     @     @    @@@@    @          @@@@        ##
##        @  @         @   @ @   @     @       @          @           ##
##   @    @  @          @ @   @ @      @       @          @           ##
##    @@@@   @@@@@@      @     @       @@@@@@@ @@@@@@@@   @@@@@@      ##
##                                                                    ##
##   Copy Right by JEWELE                                             ##
##                                                                    ##
########################################################################
#It's will Dynamically changed

import requests
boxurl = requests.get("http://www.imdb.com/chart/boxoffice")

text = boxurl.text
boxurl.title = text[text.find('<tbody>')+7:text.find('<div class="reported text-smaller">')][:20557]
boxmovie = boxurl.title.split('<td class="titleColumn">')
link = []
for name in range(1,11):
    boxmovie1 = boxmovie[name].split('<a href=')
    boxmovie2 = boxmovie1[1].split('/')
    boxmovie3 = boxmovie2[2].split('"')
    final = 'http://www.imdb.com/'+'title/'+boxmovie3[0]
    link.append(final)
print(link)
#print(link[1])

