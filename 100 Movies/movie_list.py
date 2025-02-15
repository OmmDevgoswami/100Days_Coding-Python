from bs4 import BeautifulSoup
import requests

wesbite = requests.get("https://editorial.rottentomatoes.com/guide/best-anime-movies/")
wesbite.raise_for_status
content = wesbite.text

soupDetails = BeautifulSoup(markup = content, features = "html.parser")
movieTile = soupDetails.select(selector = "div.article_movie_title > h2")

movieList = []
for _ in movieTile:
    title = _.text.split("\n")[1]
    yearOfRelease = _.text.split("\n")[2]
    movieList.append({"Title": title, "Year Of Release": yearOfRelease})

print(movieList)

with open("100 Movies\movieList.txt", "w") as file:
    count = 0
    for movie in movieList:
        count += 1
        file.write(f"{count}: {movie['Title']} - {movie['Year Of Release']}\n")
