# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import os

review_on_page = 22

max = int(input("Сколько страниц вы хотите спарсить? (по " + str(review_on_page - 1) + " отзыва на страницу) "))

j = 0
while j < max:

    url = 'https://tophotels.ru/hotel/al4780/reviews?fvote=1&frecommend=1&page=' + str(j + 1)

    tonality = "p1"

    array_title = []
    array_post = []

    html = requests.get(url)

    soup = BeautifulSoup(html.text, "html.parser")

    soup_title = soup.find_all("p", class_='bth__cnt bold mb5')
    for x in soup_title:
        x.find("p")
        title = x.text
        array_title.append(title)

    soup_post = soup.find_all("p", class_='bth__cnt mb10')
    for y in soup_post:
        y.find("p")
        post = y.text
        array_post.append(post)

    i = 0
    while i < (review_on_page-1):
        filename = str(array_title[i]).replace('*', '').replace('?', '').replace('"', '').replace('/', '').replace('-', ' ').replace('\r', '').replace('\n', '') + ".txt"
        F = open('AVKashtanov.json', 'a', encoding='utf-8')
        text = '{' + "\n"'"student_name": "Kashtanov Artem",' + "\n"'"student_group": 651,' + "\n"'"student_number": 19,' + "\n"'"date": "' + "none" + '",' + "\n"'"Data source": "' + url + '",' + "\n"'"tonality": "' + tonality + '",' + "\n"'"filename": "p1/' + filename + '"' + "\n"'},' + "\n"
        F.write(text)
        F.close()
        F2 = open(filename, 'w', encoding='utf-8')
        F2.write(str(array_post[i]))
        F2.close()
        i = i + 1

    j = j + 1

    print("Спарсили " + str(review_on_page - 1) + " отзывов")