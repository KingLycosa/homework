import requests
from bs4 import BeautifulSoup

r = requests.get("http://nytimes.com")
soup = BeautifulSoup(r.text, "html.parser")
titles = soup.findAll("h2", {"class": "story-heading"})

for title in titles:
	if title.findAll("a"):
		print(title.a.text.strip())
	else:
		print(title.text)
