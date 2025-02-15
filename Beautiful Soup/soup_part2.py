from bs4 import BeautifulSoup

with open("Beautiful Soup\website.html", "r", encoding = "utf-8") as website:
    content = website.read()
    
soupDetails = BeautifulSoup(markup = content, features = "html.parser")
links = soupDetails.find_all(name = "a") #Find all elements having the "a" tag and returns a list
print(links) 
print()

para = soupDetails.find(name = "p") #Retruns the first HTML element having "p" tag
print(para)
print()

for _ in links:
    print(_.getText())      #Returns in bs4 format
    print(_.text)           #Returns the content of the tag in pure string format
    print(_.get("href"))    #Retruns the links of the anchor tag
    
"""
.text is a better way as it converts your text into an string, while .getText() method is returned in the form of method,
so In my opinion, I would say .text is much better way because you don't have to then convert the text to string 
manually if you want

.string does also returns the same thing, but then you would have to  convert the text to string manually as it returns
in the type of bs4.element.NavigableString which can't be used as an normal string
"""
print()
specificSearch = soupDetails.find(name = "h1", id="name")
print(specificSearch.text) #Returns the text of the element with id "name" and tag
print(specificSearch.get("id")) #Returns the id of the element with id "name"
print()

specificSearch_2 = soupDetails.find(name = "h3", class_ = "heading") #class is a keyword in python so class_ is used
print(specificSearch_2.text) #Returns the text of the element with class "heading"
print(specificSearch_2.get("class")) #Returns the class of the element with class "
print()

companyURL = soupDetails.select_one(selector = "p a")  
"""select_one returns the first searched while select returns all"""
print(companyURL)
print(companyURL.text) #Returns the text of the element with tag "a" inside the tag
print(companyURL.get("href")) #Returns the link of the element with tag "a" inside

"""
find_all() uses arguments such as tag, class, id, etc.
select() is used with CSS syntax: # = id, . = class, > = children, etc. You can also search for multiple classes.
"""

headings = soupDetails.select(".heading")
print(headings) #Returns all elements with class "heading" in a list format