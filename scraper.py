import requests
from bs4 import BeautifulSoup
from time import sleep


# for Cookie
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '}

# 1-6 pages


def get_url():
    for count in range(1, 6):
        url = f"https://scrapingclub.com/exercise/list_basic/?page={count}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "lxml")
        data = soup.find_all("div", class_="w-full rounded border")
        for i in data:
            obj_url = "https://scrapingclub.com" + i.find("a").get("href")
            yield obj_url


# inside of those pages
for obj_url in get_url():
    sleep(3)
    response = requests.get(obj_url, headers=headers)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="my-8 w-full rounded border")
    name = data.find("h3", class_="card-title").text
    img_url = "https://scrapingclub.com" + data.find("img").get("src")
    price = data.find("h4", class_="my-4 card-price").text
    description = data.find("p", class_="card-description").text
    print(name + "\n", img_url + "\n", price + "\n", description + "\n")
