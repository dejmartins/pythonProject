import json

config_dict = {
    "name": "Adeola",
    "bool": True,
    "age": [21, 22, 23]
}

# with open("config.json", mode='w') as file_obj:
#     json.dump(config_dict, file_obj, indent=4)
    # con = json.load(file_obj)
with open("config.json", mode='r') as file_obj:
    con = json.load(file_obj)
    print(con)