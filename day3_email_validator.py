emails = ["reny@gmail.com", "student.ai", "evangelin@yahoo.com", "wrong_email", "admin@google.com"]

valid_emails = []
invalid_emails = []

for email in emails:
    if "@" in email and email.endswith(".com"):
        valid_emails.append(email)
    else:
        invalid_emails.append(email)

print("Valid Emails:", valid_emails)
print("Invalid Emails:", invalid_emails)
