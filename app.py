course_title = "Python for Machine Learning"
documentation = """
Feature Extraction Pipeline:
- Extracts token prefixes
- Inspects first and last characters
"""

print(documentation)

first_char = course_title[0]
last_char = course_title[-1]
print(f"First character: {first_char}")
print(f"Last character: {last_char}")

prefix = course_title[0:6]
suffix = course_title[-8:]
full_copy = course_title[:]

print(f"Prefix: {prefix}")
print(f"Suffix: {suffix}")
print(f"Copy: {full_copy}")