import requests
import bs4

#
# url = 'http://github.com'
# r = requests.get(url)
#
# r_html = r.text #r_html contain HTML
#
# soup = bs4.BeautifulSoup(r_html,features="lxml")
#
# title = soup.find('summary').text
#
# # print(r_html)
# print(title)
#
#

sauce = requests.get("https://niebezpiecznik.pl")
soup = bs4.BeautifulSoup(sauce.text, features="html.parser")

titles = soup.find_all()

# print(soup.find("h2").text)

for title in soup.find_all("h2"):
    print(title.string)

