# basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(basket)                      # show that duplicates have been removed

# 'orange' in basket                 # fast membership testing

# 'crabgrass' in basket


# # Demonstrate set operations on unique letters from two words

# a = set('abracadabra')
# b = set('alacazam')

# a                                  # unique letters in a

# a - b                              # letters in a but not in b

# a | b                              # letters in a or b or both

# a & b                              # letters in both a and b

# a ^ b            

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel.pop(1)
print(tel)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]

thisdict.update({"color": "red"})
thisdict.pop("model")
print(thisdict)
thisdict.popitem()
print(thisdict)

thisset = {"apple", "banana", "cherry"}

thisset.add("orange")

print(thisset)
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}

thisset.update(tropical)

print(thisset)