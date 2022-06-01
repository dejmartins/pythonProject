temp_file = open("temp.txt", mode='r')
print("first line", file=temp_file)
print("second line", file=temp_file)
print(temp_file.readlines())
temp_file.close()

# with open('my_file.txt', mode='w') as f:
#     f.write("Jonathan Martins\n")
#     f.write("Joan Martins\n")
#     f.write("Judah Martins\n")
#     f.write("Jack Martins\n")

# with open('my_file.txt', mode='r+') as f:
    # db = f.readlines()
    # print(db)
    # for names in f:
    #     print(names)


# family_members = ["Jerry Martins", "John Martins", "Jindu Martins"]
# with open('my_file.txt', mode='a+') as names:
#     for members in family_members:
#         names.write(members)
#         names.write("\n")


# with open('my_file.txt', mode='a+') as f:
#     print(f.tell())


# with open('my_file.txt', mode='r') as f:
#     family_members = f.readlines()
# family_members.insert(1, "Jane Martins\n")
# family_members.insert(3, "Jacintha Martins\n")
#
# with open('my_file.txt', mode='w') as f:
#     familyMembers = "".join(family_members)
#     f.write(familyMembers)

with open('my_file.txt', mode='r+') as f:
    for lines in f:
        print(lines)