import requests
from bs4 import BeautifulSoup

url = "https://weather.com/weather/monthly/l/0f33b2879c4bf88b28c66d9c21e0658ebf8832d6df964432ccf14f81e5d1c119"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# تنظیم واحد سانتیگراد
unit_selector = soup.find("section", {"data-testid": "unitSelectorSection"})
celsius_button = unit_selector.find("li", {"class": "UnitSelector--UnitSelectorInactiveTab--3dgsa"})
celsius_button['class'] = "UnitSelector--UnitSelectorActiveTab--1q2d_ TabList--tabSelected--3Vj3p"
celsius_button['aria-selected'] = "true"

# چاپ واحد سانتیگراد
selected_unit = celsius_button.text.strip()
print(selected_unit)

# دریافت محتوای HTML
html_content = str(soup)
print(html_content.encode('utf-8'))

