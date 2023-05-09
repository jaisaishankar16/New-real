from pymongo import MongoClient

# create a MongoDB client instance
client = MongoClient('mongodb://localhost:27017/')

# connect to the database
db = client['my_database']

# retrieve the required data from the collection
data = db['my_collection'].find({}, {'value': 1})

# create the select tag
select_tag = '<select name="location">\n'

# loop through the data and create options for the select tag
for item in data:
    select_tag += f'<option value="{item["value"]}">{item["value"]}</option>\n'

# close the select tag
select_tag += '</select>'

# print the select tag
print(select_tag)
