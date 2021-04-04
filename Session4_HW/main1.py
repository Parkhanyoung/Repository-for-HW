import requests
from bs4 import BeautifulSoup
import csv
from mod1 import module

file = open('movie2.csv', mode= 'w', newline= "")
writer = csv.writer(file)
writer.writerow(['title', 'img', 'score', 'direct', 'actor', 'opendate'])

movie_URL = f'https://movie.naver.com/movie/running/current.nhn'
movie_html = requests.get(movie_URL)
movie_soup = BeautifulSoup(movie_html.text, 'html.parser')
movie_object = movie_soup.find('ul', {'class': 'lst_detail_t1'})
movie_list_box = movie_object.find_all('li')

module(movie_list_box)