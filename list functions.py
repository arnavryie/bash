
lucky_numbers = [4 , 8  ,15 ,16 ,23 , 42 ]
friends = ["kevin" , "karen " , "jim" , "oscar ",  "tobby "]
friends.extend(lucky_numbers)
friends.append("creed")
friends.insert(1, "kelly")
friends.remove("jim")
friends.pop()

print(friends)
print(friends.index("kevin"))

friends2 = friends.copy()
print(friends2)

lucky_numbers.reverse()
print(lucky_numbers)

