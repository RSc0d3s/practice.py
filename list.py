lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Toby"]
friends.insert(1, "Kelly") #index position + data to insert, all other elements will move to the right
friends.sort()
print(friends)
lucky_numbers.sort()
print(lucky_numbers)

friends2 = friends.copy()
print(friends2)
