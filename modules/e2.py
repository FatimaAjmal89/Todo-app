import csv

with open("../new/weather.csv", 'r') as file:
    data = list(csv.reader(file))

city = input("Enter a city: ")


for row in data[1:]:
    if row[0] == city:
        print(row[1])
