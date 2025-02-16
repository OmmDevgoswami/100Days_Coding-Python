from bs4 import BeautifulSoup
import requests

class Songlist:
    def __init__(self, dateVal):
        self.songList = {}
        self.url = "https://www.billboard.com/charts/hot-100/" + dateVal
        self.finalList()
        
    def finalList(self):
        headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"}
        website = requests.get(self.url, headers = headers)
        website.raise_for_status()
        content = website.text
        soupDetails = BeautifulSoup(markup = content, features = "html.parser")
        songName = soupDetails.select(selector = "li.o-chart-results-list__item > h3.c-title")
        songArtists = soupDetails.select(selector = "li.o-chart-results-list__item > span.a-no-trucate")
        songArtist = []
        for artist in songArtists:
            artist_text = artist.text.strip()  
            artist_text = artist_text.replace("Featuring", "feat.").replace("\\'", "'")
            songArtist.append(artist_text)
        
        for song, artist in zip(songName, songArtist):
            self.songList[song.text.strip()] = artist
        return self.songList
        
# a = Songlist()
# val = a.finalList()
# print(val)

# val = input("Enter the date:")
# url = "https://www.billboard.com/charts/hot-100/" + val+"/"
# headers = {
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
# }
# website = requests.get(url, headers = headers)
# website.raise_for_status
# content = website.text
# soupDetails = BeautifulSoup(markup = content, features = "html.parser")
# songName = soupDetails.select(selector = "li.o-chart-results-list__item > span.a-no-trucate")
# for _ in songName:
#     print(_.text.strip())
