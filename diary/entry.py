import json
from commons import get_file_path, get_file

entry = {
    "date": "May 14, 2022 07:00:37",
    "title": "How I met my wife",
    "body": "I just fell in love the first time I set my eyes on her"
}


def save_entry():
    file_path = get_file_path("entries")

    with file_path.open(mode='w') as file:
        json.dump(entry, file)


def get_entry_by():
    pass


def delete_entry():
    pass


if __name__ == '__main__':
    print(get_file_path("entries"))
    save_entry()
    print(get_file("entries"))
