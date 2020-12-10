import random
import requests
from bs4 import BeautifulSoup

url = "https://www.imdb.com/chart/top/"


def main():
    bring = requests.get(url)
    html = bring.text
    soup = BeautifulSoup(html, "html.parser")
    movies_tags = soup.select("td.titleColumn")
    # movies_tag = movies_tags[0]
    content_movie_tags = soup.select("td.titleColumn a")
    # content_movie_tag = content_movie_tags[0]
    rating_tags = soup.select("td.posterColumn span[name=ir]")
    # rating_tag = rating_tags[0]

    def get_year(movie_tag):
        movies_tag_split = movie_tag.text.split()
        year = movies_tag_split[-1]
        return year

    years = [get_year(tag) for tag in movies_tags]
    actors_list = [tag["title"] for tag in content_movie_tags]
    titles = [tag.text for tag in movies_tags]
    rating = [tag["data-value"] for tag in rating_tags]

    number_movies = len(titles)

    while True:
        index = random.randrange(0, number_movies)
        print("Film No, Film Name, Film Year", titles[index])
        print(f'Rating : {float(rating[index]):.1f}')
        print("Actors: ", actors_list[index])

        user_input = input("Do you want to make another choice? (y/[n]): ")
        if user_input == "y":
            print("<------------------------------------>")

        elif user_input != "y":
            print("Have fun!")
            break


if __name__ == '__main__':
    main()

