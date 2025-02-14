from bs4 import BeautifulSoup

with open("Beautiful Soup\\website.html", "r", encoding="utf-8") as website:
    content = website.read()

print(content)
soupDetails = BeautifulSoup(markup = content, features='html.parser')
print()
print(soupDetails.title,"\n") #Return the whole HTML element
print(soupDetails.title.name,"\n") #Returns the HTML tag name
print(soupDetails.title.string,"\n") #Return the content of that HTML element
print(soupDetails.li,"\n")  #Return the first li element
print(soupDetails.a,"\n") #Returns the first a element
print()
print(soupDetails)  #Returns the HTML file
print(soupDetails.prettify())   #Returns the HTML file but indented