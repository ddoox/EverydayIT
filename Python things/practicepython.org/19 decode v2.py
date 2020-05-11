import requests
import bs4


url = "http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture"

sauce = requests.get(url)
soup = bs4.BeautifulSoup(sauce.text, "lxml")

result = soup.find_all("p")

for i in result:
    print(i.get_text())  # return only what is in <p>
    # print(i)           # return whole <p>
