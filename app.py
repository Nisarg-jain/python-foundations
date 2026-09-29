# 1. Applicant profile criteria
has_high_income = False
has_good_credit = True
has_criminal_record = False

# 2. Conjunction (and) validation
if has_high_income and has_good_credit:
    print("Loan Approved: Met both income and credit requirements.")
else:
    print("Loan Rejected: Requires both high income and good credit.")

# 3. Negation (not) with conjunction (and)
if has_good_credit and not has_criminal_record:
    print("Secondary Review Approved: Good credit standing with clear record.")
else:
    print("Secondary Review Rejected: Failed credit or background check.")

# 4. Short-circuit evaluation demonstration
# If the first value is truthy, 'or' returns it immediately without reading the second
fallback_user = None
current_user = fallback_user or "Default_User_Session"
print(f"Active Session: {current_user}")