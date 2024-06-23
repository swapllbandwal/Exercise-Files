import json

file_path = "groceries.json"

with open(file_path , "r") as file:
    parsed_data = json.load(file)
    print("parsed data ", parsed_data)
    print("carrots value is", parsed_data["carrots"])