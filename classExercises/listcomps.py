# lst = [num for num in range(1, 11)]
# evens = [num for num in range(1, 11) if num % 2 == 0]
# evens_and_squared_odds = [num if num % 2 == 0 else num **2 for num in range(1, 11)]
# lst_input = [int(input("Enter a number: ")) for num in range(1, 4)]
#
# print(lst)
# print(evens)
# print(evens_and_squared_odds)
# print(lst_input)


#
# gen = (num for num in range(1, 11))
# print(list(gen))


# s1 = {1, 2, 3, 4, 5, 6}
# s2 = {4, 5, 6, 7, 8, 9}
#
# s1 |= s2
# s1 &= s2
#
# print(s1.isdisjoint(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# print(s1 ^ s2)

dict_play = {"name": "Tolani", "age": 32, "influenced": "Samson"}
# dict_play.clear()
# print(dict_play.get("name", "Samson"))


# print(dict_play["name"])
# dict_play.pop("name")
# print(dict_play)
# dict_play.popitem()
# print(dict_play)

dict_play.update({"surname": "Joe"})
print(dict_play)

{}.fromkeys(['DEJ', 'JOE', 'KAP'], "UNKNOWN")
print(dict_play)
