import csv
import json

# Collect user input
Lname = input("What is your last name: ")
Fname = input("What is your first name: ")
phone = input("What is your phone number: ")

# Write data to CSV
with open('info.csv', 'w', newline='') as csvfile:
    write = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    write.writerow(['Last Name', 'First Name', 'Phone'])
    write.writerow([Lname, Fname, phone])

# Function to convert CSV to JSON
def make_json(csvFilePath, jsonFilePath):
    data = []

    with open(csvFilePath, encoding='utf-8') as csvf:
        csvReader = csv.DictReader(csvf)
        
        for row in csvReader:
            data.append(row)

    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(data, indent=4))

# Paths to files
csvFilePath = 'info.csv'
jsonFilePath = 'info.json'

# Convert CSV to JSON
make_json(csvFilePath, jsonFilePath)