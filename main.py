import requests
from bs4 import BeautifulSoup

user_date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD:\n")

response = requests.get(url=f"https://www.billboard.com/charts/hot-100/{user_date}")
response.raise_for_status
content = response.text

soup = BeautifulSoup(content, "html.parser")