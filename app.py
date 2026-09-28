first_name = "Nisarg"
last_name = "Jain"

# Formatted string (f-string) interpolation
message = f"{first_name} [{last_name}] is training neural networks"
print(message)

# General function vs string methods
raw_query = "   Natural Language Processing with Python   "
print(len(raw_query))

cleaned_query = raw_query.strip()
print(cleaned_query.upper())
print(cleaned_query.lower())

# Finding indices and replacement (returns new string)
print(cleaned_query.find("Language"))
modified_query = cleaned_query.replace("Python", "PyTorch")
print(modified_query)

# Membership test with 'in' operator (boolean)
has_nlp = "Language" in cleaned_query
print(f"Contains 'Language': {has_nlp}")