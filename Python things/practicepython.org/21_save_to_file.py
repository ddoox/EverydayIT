import requests
import bs4


sauce = requests.get("https://niebezpiecznik.pl")
soup = bs4.BeautifulSoup(sauce.text, features="html.parser")

titles = soup.find_all()

with open("file.txt", "w") as open_file:  # auto close file
    for title in soup.find_all("h2"):
        open_file.write(title.string + "\n")


