course = ' python "ProgrAmming'
numbers = [1, 2, 3, 4, 5, 6]
digit = "23445"

full = f"{course} {digit}"
print(full.find("mm"))
replaced = full.replace("m", "s")
print(replaced.strip())
# full.find("mm") == "p" if print("find it!") else print("not")
print("find it!") if full.find("s") != -1 else print("not found!")
print("pro" in course)
print("swift" not in  course.lower()) # sensitive