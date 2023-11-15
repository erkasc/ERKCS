print("List Iteration")
l = ["nandhini","jaya","priya"]
for i in l:
    print(i)

# Iterating over a tuple (immutable)
print("\nTuple Iteration")
t = ("preethi", "baby", "sheela")
for i in t:
    print(i)

# Iterating over a String
print("\nString Iteration")
s = "jaya"
for i in s:
    print(i)
# Iterating over dictionary
print("\nDictionary Iteration")
d = dict()
d['jaya'] = 123
d['priya'] = 345
for i in d:
    print("%s  %d" % (i, d[i]))
