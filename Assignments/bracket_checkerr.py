set_of_brackets = input(str("Input a set of brackets: "))


def brackets_checker():
    if set_of_brackets.count('(') == set_of_brackets.count(')'):
        if set_of_brackets.count('[') == set_of_brackets.count(']'):
            if set_of_brackets.count('{') == set_of_brackets.count('}'):
                print(True)
            else:
                print(False)
        else:
            print(False)
    else:
        print(False)


if set_of_brackets.startswith('{') and set_of_brackets.endswith('}'):
    brackets_checker()
elif set_of_brackets.startswith('[') and set_of_brackets.endswith(']'):
    brackets_checker()
elif set_of_brackets.startswith('(') and set_of_brackets.endswith(')'):
    brackets_checker()
else:
    print(False)
