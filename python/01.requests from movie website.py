import requests
from bs4 import BeautifulSoup

url = "https://www.empireonline.com/movies/features/best-movies-2/"

respone = requests.get(url)
website_html = respone.text

soup = BeautifulSoup(website_html, "html.parser")

all_movies = soup.find_all(name="h3", class_="listicleItem_listicle-item__title__BfenH")

movie_titles = [movie.getText() for movie in all_movies]

for movie in movie_titles[::-1]:
  print(movie)