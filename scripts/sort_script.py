import json

# Path to json file
json_path = "../_data/"

# Specify the name of your JSON file
json_file_name = "hololive.json"

# Specify the property you want to sort by
property_to_sort_by = "gen"

# Read in the JSON file and parse it into a list of objects
with open(json_path + json_file_name, "r") as json_file:
    json_data = json.load(json_file)

# Sort the list of objects based on the specified property
sorted_data = sorted(json_data, key=lambda x: x[property_to_sort_by])

# Write the sorted list of objects out to a new JSON file
with open("sorted_" + json_file_name, "w") as sorted_json_file:
    json.dump(sorted_data, sorted_json_file, indent=4)