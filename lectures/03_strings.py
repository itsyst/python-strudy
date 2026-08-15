"""
Lecture: Strings
"""

course = 'python "ProgrAmming"'
digit = "23445"

full = f"{course} {digit}"
print("Full:", full)
print("Find 'mm':", full.find("mm"))
print("Replace m→s:", full.replace("m", "s").strip())
print("'pro' in course:", "pro" in course)
print("'swift' not in lower:", "swift" not in course.lower())
