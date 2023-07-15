import requests
from bs4 import BeautifulSoup
import sys

sys.stdout.reconfigure(encoding='utf-8')

url = "https://weather.com/weather/monthly/l/0f33b2879c4bf88b28c66d9c21e0658ebf8832d6df964432ccf14f81e5d1c119"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

unit_selector = soup.find("section", {"data-testid": "unitSelectorSection"})
celsius_button = unit_selector.find("li", {"class": "UnitSelector--UnitSelectorInactiveTab--3dgsa"})
celsius_button['class'] = "UnitSelector--UnitSelectorActiveTab--1q2d_ TabList--tabSelected--3Vj3p"
celsius_button['aria-selected'] = "true"
selected_unit = celsius_button.text.strip()

month = 'Jun'
select_element = soup.find('select', id='month-picker')
option_element = select_element.find('option', text=month)
select_element['value'] = option_element['value']
# print(html_content.encode('utf-8'))
# print(soup.prettify())

temp_elements = soup.find_all("span", {"data-testid": "TemperatureValue"})
temperatures = [temp.text.strip() for temp in temp_elements]
DateTime_elements = soup.find_all("span" , {"data-testid": "CalendarDateCell"})
Date_Time = [Date.text.strip() for Date in DateTime_elements]
print(Date_Time , temperatures)
# for temp in temperatures:
    # print(temp)