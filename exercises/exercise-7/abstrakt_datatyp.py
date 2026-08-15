# Create a mapping
lastnames = []

# Add some entries
lastnames.append(("Jonas", "Kvarnström"))
lastnames.append(("Peter", "Dalenius"))

print(lastnames)
# Look up a value
for entry in lastnames:
    print(entry[0], entry[1])
    if entry[0] == "Jonas":
        print(entry[1])


def createmap():
    return {}

def setmap(m, key, value):
    m[key] = value

def getmap(m, key):
    return m.get(key)

# Create a mapping
lastnames = createmap()

# Add some entries
setmap(lastnames, key="Jonas", value="Kvarnström")
setmap(lastnames, key="Peter", value="Dalenius")

# Look up a value
print("GETMAP:", getmap(lastnames, "Jonas"))
