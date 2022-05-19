import json
from pathlib import Path
from utils import hash_password, validate_password
from commons import get_file_path, get_file

new_user = {
    "diary_name": "Quibs",
    "firstname": "Jonathan",
    "lastname": "Martins",
    "email": "dej@gmail.com",
    "password": "1234"
}


def save_users(new_user):
    new_user['password'] = hash_password(new_user['password'])
    file_path = get_file_path("users_info")

    users = get_file("users_info")

    if [u for u in users if u['email'] == new_user['email']]:
        print(f"User with email address '{new_user['email']}' already exists")
        return

    users.append(new_user)

    with open(file_path, mode='w') as file:
        json.dump(users, file)


def validate_user(email, password):
    users = get_file("users_info")
    if [u for u in users if u['email'] == email and validate_password(password, u['password'])]:
        return
    else:
        print("Invalid password!")

    # return validate_password(password, hashed_password)


if __name__ == '__main__':
    print(Path.cwd())
    print(Path.home())
    print(get_file_path("users_info"))
    save_users(new_user)
    print(get_file("users_info"))
    validate_user("dej@gmail.com", "1234")

    # save_users(new_user)
