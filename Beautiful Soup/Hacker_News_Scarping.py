from bs4 import BeautifulSoup
import requests
from functools import reduce

website = requests.get("https://news.ycombinator.com/news")
website.raise_for_status()
content = website.text

soupDetails = BeautifulSoup(markup = content, features = "html.parser")

websiteTitle = soupDetails.title
print(f"Website : {websiteTitle.text}\n")

newTitles = soupDetails.select(selector = "span.titleline > a" )    
""" Retruns a list of all anchor tags containing the Headlines """

print(f"Headline: {newTitles[0].text}") #Returning only the first headlines
print(f"Link: {newTitles[0].get('href')}") #Returns the link
scoreTop = soupDetails.select_one(selector = "span.subline > span.score")
print(f"Score Today: {scoreTop.text.split()[0]}")

titleList = []
linkList = []
for _ in newTitles:
    titleList.append(_.text)
    linkList.append(_.get('href'))
scoreList = [x.text.split()[0] for x in soupDetails.select(selector = "span.subline > span.score")]
print(f"\n{titleList}\n{linkList}\n{scoreList}\n")

maxScore = reduce(lambda x,y :x if int(x) > int(y) else y, scoreList)
# print(maxScore)
indexVal = scoreList.index(maxScore)
mostUpVotes = f"""Most Upvoted Headline: {titleList[indexVal]}
Link: {linkList[indexVal]}
Total Upvotes {maxScore}"""
print(mostUpVotes)