# user_access_details = [{"username": "Jonathan", "password": "pass123"},
#                        {"username": "Mercy", "password": "kolo123"},
#                        {"username": "Funke", "password": "sample123"}]




# user_access_details = {
#     "favourite_food": ["rice", "beans", "dodo"],
#     "favourite_players": {"Arsenal": "Bukayo", "Chelsea": "Lukaku", "Dekanorbs": "Shege"},
#     "favourite_girl": "Funke",
#     "favourite_music": ["last last", "buga", "azonto"],
#     "favourite_language": {"Programming": "Python", "Dialect": "Yoruba", "Slang": "Breakfast"}
# }


# def type_checker(type):
#     for value in user_access_details.values():
#         if isinstance(value, type):
#             print(value)
#     """Loop through the dictionary"""
#     """Check the type of each value per key"""
#     """Print - This is a {type}"""
#     """Congratulate yourself"""


# def lst_checker(username, password):
#     """Code to be written here"""
#     for details in user_access_details:
#         pass
#     """Validate if username and password exists in our dummy list database"""











contact_details = {
    "full_name": "Tony Akanji",
    "address": ["Yaba", "Shomolu", "Okpara"],
    "phone_number": ["08088893600"],
    "class": {"cohort10": "dekanorbs", "cohort9": "bright_light"}
}



def add_details(phonenumber):
    [value.append(phonenumber) for key, value in contact_details.items() if isinstance(value, list) and key == "phone_number"]




if __name__ == "__main__":
    add_details("08023340908")
    # add_number("08023340908")
    print(contact_details)
    # print(lst_checker("Jonathan", "pass13"))
