# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re

max = int(input("Сколько страниц спарсить? "))

max = max * 5

j = 0
while j < max:

    url = 'https://www.tripadvisor.ru/Hotel_Review-g187497-d1146187-Reviews-or' + str(
        j) + '-g187497-d1146187-Reviews-Pension_Picasso-Barcelona_Catalonia.html'

    tonality = "m1"

    array_title = []
    array_post = []

    html = requests.get(url)

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

    i = 0
    while i < 5:
        filename = str(array_title[i]) + ".txt"
        F = open('AVKashtanov.json', 'a', encoding='utf-8')
        text = '{' + "\n"'"student_name": "Kashtanov Artem",' + "\n"'"student_group": 651,' + "\n"'"student_number": 4,' + "\n"'"date": "' + "none" + '",' + "\n"'"Data source": "' + url + '",' + "\n"'"tonality": "' + tonality + '",' + "\n"'"filename": "m1/' + filename + '"' + "\n"'},' + "\n"
        F.write(text)
        F.close()
        F2 = open(filename, 'w', encoding='utf-8')
        F2.write(str(array_post[i]))
        F2.close()
        i = i + 1

    j = j + 5
    print("Спарсено +1 страница!")