# coding=utf-8
from bs4 import BeautifulSoup
import requests
import re
import os

review_on_page = 22

max = int(input("Сколько страниц вы хотите спарсить? (по " + str(review_on_page - 1) + " отзыва на страницу) "))

j = 0
while j < max:

    url = 'https://tophotels.ru/hotel/al5325/reviews?fvote=2&page=' + str(j + 1)

    tonality = "m1"

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
        this_title = str(array_title[i]).replace('*', '')
        this_title = str(this_title).replace('?', '')
        if this_title == (''):
            this_title = "Нет названия: Страница " + str(j + 1) + ", отзыв " + str(i)
        filename = this_title[0:25] + ".txt"
        #"Страница " + str(j + 1) + ", отзыв " + str(i) + ".txt"
        path = "../m1"
        filepath = os.path.join(path, filename)
        F = open('SalakhievIska.json', 'a', encoding='utf-8')
        text = '{' + "\n"'"student_name": "Salakhiev Iskander",' + "\n"'"student_group": 651,' + "\n"'"student_number": 4,' + "\n"'"date": "' + "none" + '",' + "\n"'"Data source": "' + url + '",' + "\n"'"tonality": "' + tonality + '",' + "\n"'"filename": ' + filepath + '"' + "\n"'},' + "\n"
        F.write(text)
        F.close()
        F2 = open(filepath, 'w', encoding='utf-8')
        F2.write(str(array_post[i]))
        F2.close()
        i = i + 1

    j = j + 1

    print("Спарсили " + str(review_on_page - 1) + " отзывов")
