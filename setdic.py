users = {}
emails = set()
phones = set()
i=1
while i==1:
    name = input("Enter name: ")
    email = input("Enter email: ")
    phone = input("Enter phone number: ")

    if email in emails:
        print(f"Email id is already exists! Try again.\n")
    elif phone in phones:
        print(f"Phone number is already exists  Try again.\n")
    else:
        users[name] = {
            'email': email,
            'phone': phone
        }

       
        emails.add(email)
        phones.add(phone)
    if i==1:
        i=int(input("Are you add new member press 1.Otherwires press any key."))

print(users)
print(emails)
print(phones)
   
