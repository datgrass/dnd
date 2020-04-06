from bs4 import BeautifulSoup
import requests
import re
import json

#downloading our page data
page = requests.get('https://www.dnd-spells.com/spells')
soup = BeautifulSoup(page.content, 'html.parser')

#getting the attribute we want
rows = []
table = soup.find('table') #selecting a table of spells
tr = table.find_all('tr') #finding all table rows from our previously found html attribute

#looping through every 'tr' while removing blank spaces and then adding them to a list
for row in tr:
    content = row.get_text()
    content = content.split('\n')
    del content[0]
    del content[0]
    if len(content) != 9: #some rows are longer than others, so we need to be mindful of this
        del content[1]
        del content[1]
        x = len(content) - 1
        del content[x] #the last two spaces were blank
        del content[x - 2]
    else:
        del content[8]
    rows.append(content)

#looping through the new rows and concatenating all of our classes into one field
for row in rows:
    if len(row) != 8:
        new_row = row[:5] #getting the first 6 values of the row because they are guaranteed to be correct
        class_ls = []
        for i in range(6, len(row) - 1): #looping through each class by getting its index in the list
            dnd_class = re.search('\S+', row[i]) #removing all non-whitespace characters
            class_ls.append(dnd_class.group(0)) #appending them to a list for later use
        new_row.append(class_ls) #adding the newly formed list
        new_row.append(row[len(row) - 1]) #adding the final value in the original row
        rows[rows.index(row)] = new_row #replacing the row by finding its index within the list
    elif row[6] != 'Class': #making sure we aren't grabbing our header rows
        class_ls = []
        dnd_class = re.search('\S+', row[6]).group(0)
        class_ls.append(dnd_class)
        rows[rows.index(row)][6] = class_ls

with open('spells.json', 'w') as outfile:
    json.dump(rows, outfile)