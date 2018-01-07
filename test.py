import json, requests
import sqlite3

host = "http://127.0.0.1:8080/organizations"
database = "db.sqlite3"


response = requests.get(url=host)
#print (response)
data = json.loads(response.text)
print (data)
amount = len(data)


organization_keys, organization_parent_keys, organization_descriptions, organization_levels = [], [], [], []

for i in range(amount):
    for key, value in data[i].items():
        if key == "key":
            organization_keys.append(value)
        elif key == "parent_key":
            organization_parent_keys.append(value)
        elif key == "description":
            organization_descriptions.append(value)
        elif key == "level":
            organization_levels.append(value)    
        
connection = sqlite3.connect(database)        
cursor = connection.cursor()

cursor.execute("CREATE TABLE if not exists Jednostki(id text NOT NULL PRIMARY KEY, nazwa text NOT NULL, parent_id text, level integer);")
connection.commit()

for j in range(amount):
    query = "INSERT or REPLACE into Jednostki(id, nazwa, parent_id, level) values('{}', '{}', '{}', '{}')".format(organization_keys[j], organization_descriptions[j], organization_parent_keys[j], organization_levels[j])
    cursor.execute(query)

connection.commit()
connection.close()  
  