from validator_collection import validators, checkers

# U = input("What's your email address? ")
# try:
#     email_address = validators.email(U)
#     print("valid")
# except:
#     print("Invalid")

U = input("What's your email address? ")
email_address = checkers.is_email(U)
if email_address:
    print("valid")
else:
    print("Invalid")