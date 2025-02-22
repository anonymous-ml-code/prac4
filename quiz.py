# words = ["aye", "bee", "sea", "bee"]
# words.remove("bee")
# print(words.pop())


# def process(x, y=2, z=3):
#     return x + y + z
#
#
# print(process(x=3, z=3))


# values =[1,2,3,2]
# values.remove(2)
# print(values)

# before =[1, 4, 0, -1]
# after = before.sort()
# print(before[0])


# before = [1, 4, 0, -1]
# after = sorted(before)  # This returns a sorted list without modifying the original list
# print(after[0])

# words =["aye","bee","sea","bee"]
# words .remove("bee")
# print(words)
# print(words.pop())
# print(words)


# things = list("one two three")
# # *-unpack
# print("{}{}{}{}".format(*things))

# b = [word for word in "one*two*three".split('*')]

b = []
for word in "one*two*three".split('*'):
    b.extend(word)

print(b)
print("*".join(b))
