from bs4 import BeautifulSoup
import requests
import re

url = 'https://www.tripadvisor.ru/Hotel_Review-or100-g187497-d7142609-Reviews-Hotel_The_Serras-Barcelona_Catalonia.html'

tonality = "p1"

array_title = []
array_post = []

html = requests.get(url)
print(html.status_code)

soup = BeautifulSoup(html.text, "html.parser")


soup_title = soup.find_all("a", class_='hotels-review-list-parts-ReviewTitle__reviewTitleText--3QrTy')
for x in soup_title:
	x.find("span")
	title = x.text
	array_title.append(title)

soup_post = soup.find_all("q", class_='hotels-review-list-parts-ExpandableReview__reviewText--3oMkH')
for y in soup_post:
	y.find("span")
	post = y.text
	array_post.append(post)

		
for i in array_title:
	filename = i+".txt"
	F = open('AVKashtanov.json', 'a', encoding='utf-8')
	text = '{'+"\n"'"student_name": "Kashtanov Artem",'+ "\n"'"student_group": 651,'+ "\n"'"student_number": 4,'+ "\n"'"date": "'+"none"+'",'+ "\n"'"Data source": "'+url+'",'+ "\n"'"tonality": "'+tonality+'",'+ "\n"'"filename": "p1//'+filename+'"'+ "\n"'},'+"\n"
	F.write(text)
	F.close()

