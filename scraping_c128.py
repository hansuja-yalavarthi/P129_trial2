from bs4 import BeautifulSoup
import requests
import pandas as pd

START_URL = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"
webpage = requests.get(START_URL, verify = False)
headers = ["Star Name", "Distance", "Mass", "Radius"]
soup = BeautifulSoup(webpage.content, "html.parser")
tables = soup.find_all('table', attrs = {"class" : "wikitable sortable"})[2]
table_rows = tables.find_all('tr')

temp_list = []
for rows in table_rows:
    table_data = rows.find_all('td')
    row = [data.text.strip() for data in table_data]
    temp_list.append(row)

names = []
distance = []
mass = []
radius = []

for table_data in range(1, len(temp_list)):
    data = temp_list[table_data]
    names.append(data[0])
    distance.append(data[5])
    mass.append(data[7])
    radius.append(data[8])

star_data = zip(names, distance, mass, radius)
star_data_list = pd.DataFrame(star_data, columns = headers)
star_data_list.to_csv("data_p128.csv", index = False)
print("Data scraped!")
