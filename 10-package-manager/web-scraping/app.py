#pip install beautifulsoup4
from bs4 import BeautifulSoup
import requests

response = requests.get("https://academy.especializati.com.br/cursos")
# print(response.text)
soup = BeautifulSoup(response.text, "html.parser")

courses = soup.select("div.card-course__content h1")
for course in courses:
    print(course.get_text())