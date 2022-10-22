import csv
from email import header
data=[]
with open("archive_dataset.csv","r") as f:
    csv_reader=csv.reader(f)
    for row in csv_reader:
        data.append(row)


headers=data[0]
planet_data=data[1:]

for datapoint in planet_data:
    datapoint[2]=datapoint[2].lower()

#sortin planet names in alphabetical ordr
planet_data.sort(key=lambda planet_data:planet_data[2])

#convertin to lowercase


with open("sorted_dataset.csv","a+")as f:
    csv_writer=csv.writer(f)
    csv_writer.writerow(headers)
    csv_writer.writerow(planet_data)

with open("sorted_dataset.csv") as input,open('sorted_dataset1.csv','w',newline='') as output:
    writer=csv.writer(output)
    for row in csv.reader(input): 
        if any(field.strip() for field in row): 
            writer.writerow(row)