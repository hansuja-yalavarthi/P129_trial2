import csv
import pandas as pd

file1 = 'data_from_p127.csv'
file2 = 'data_from_p128.csv'
d1 = []
d2 = []

with open(file1,'r',encoding='utf8') as f:
    csv_reader =csv.reader(f)
    for i in csv_reader:
        d1.append(i)
        
with open(file2,'r',encoding='utf8') as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        d2.append(i)

header1 = d1[0]
header2 = d2[0]

planet_data_1 = d1[1:]
planet_data_2 = d2[1:]

headers = header1+ header2

planet_data =[]

for i in planet_data_1:
    planet_data.append(i)
for j in planet_data_2:
    planet_data.append(j)
with open("Data_merged.csv",'w',encoding='utf8') as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(headers)   
    csvwriter.writerows(planet_data)
    
df = pd.read_csv('merged_data_p129.csv')
df.tail(8)
print('Your both files merged sucessfully')