file_path = "groceries.txt"
with open(file_path, "r") as file:
    data = file.read()
    print(data)
    parsed_data = data.split(", ")
    print("parsed data ", parsed_data)
    print("item at index 3 ", parsed_data[3])