from functools import reduce

users = [{"username": "dejallday", "age": 23, "tweets": [], "verified": False},
         {"username": "kynsofficial", "age": 20, "tweets": ["Have you been productive since ASUU strike or it’s "
                                                            "just vibes ?",
                                                            "End the season please, we are totally finished  as a "
                                                            "football club, what’s this, man!",
                                                            "can you go two weeks without soda?"
                                                            ], "verified": False},
         {"username": "ozioma", "age": 18, "tweets": ["How has Chelsea not scored ffs",
                                                      "Nigerian parents behave like they don’t have money till it’s "
                                                      "time for masters or wedding"
                                                      ], "verified": True},
         {"username": "notgwera", "age": 16, "tweets": [], "verified": False},
         {"username": "mbahdeyforyou", "age": 26, "tweets": ["Burna boy shutting down the Madison Square Garden in "
                                                             "few hours time ",
                                                             "We shouldn’t be doing this but you still dey unhook bra"
                                                             ], "verified": True},
         {"username": "kevin", "age": 19, "tweets": [], "verified": False},
         {"username": "erigganewmoney", "age": 34, "tweets": ["From pandemic to elections",
                                                              "Nobody toast women pass Uber drivers",
                                                              "Be nice, the world is a small town",
                                                              "Will you cheat on your partner for $1m ?"],
          "verified": True},
         {"username": "pst_iren", "age": 40, "tweets": ["First date question: what are your views on Polygamy?"
                                                        "Marry your spec and frustrate the devil 😅"],
          "verified": False},
         {"username": "drfunmilayo", "age": 44, "tweets": ["Why does Britain not give Ramadan holidays in respect to "
                                                           "Muslim British citizens and residents in the UK?",
                                                           ], "verified": True},
         {"username": "babikamii", "age": 21, "tweets": [], "verified": False}
         ]

print("List of verified users(listcomp):")
verified_users_lc = [user["username"] for user in users if user["verified"] == True]
print(verified_users_lc)
print()

print("List of verified users(map):")
verified_users_mp = list(map(lambda user: user["username"], filter(lambda user: user["verified"], users)))
# verified_users_mp = list(filter(lambda user: user, map(lambda user: user["username"] if user["verified"] else False, users)))
print(verified_users_mp)

print()
print("Names of active users(listcomp):")
active_users_lc = [user["username"] for user in users if user["tweets"] != []]
print(active_users_lc)

print()
print("Names of active users(map):")
active_users_mp = list(map(lambda user: user["username"] if user["tweets"] != [] else "", users))
print([active_user for active_user in active_users_mp if active_user != ""])

print()
print("List of users below 25 and verified(listcomp)")
below_twenty_five = [user for user in users if user["age"] <= 25 and user["verified"] == True]
print(below_twenty_five)

print()
print("Average age of students(listcomp)")
students_age = [user["age"] for user in users]
average_age = reduce(lambda total, age: total + age, students_age)
print("Average age is", average_age / len(students_age))
print("Maximum age is", max(students_age))
print("Minimum age is", min(students_age))

print()
print("Names in ascending order")
print(sorted(users, key=lambda user: user["username"]))

print()
print("Names in descending order")
print(sorted(users, key=lambda user: user["username"], reverse=True))

print()
print("From youngest user to oldest")
print(sorted(users, key=lambda user: user["age"]))

print()
print("User with the longest username")
user_usernames = [user["username"] for user in users]
longest_username = reduce(lambda user, next_user: user if len(user) > len(next_user) else next_user, user_usernames)
print(longest_username)

print()
print("User with the most tweet")
# highest_no_of_users_tweets = max([(len(user["tweets"])) for user in users])
# for user in users:
#     if len(user["tweets"]) == highest_no_of_users_tweets:
#         print(user["username"])  
most_tweets = max(users, key=lambda user: len(user["tweets"]))["username"]
print(most_tweets)
