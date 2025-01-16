#1st method
print("----------------------------")
username = input("Enter your  username\n")
userid = input("enter your id\n")

print("You entered usermane is :",username)
print("You entered userid is :",userid)
print("----------------------------")


#dot method
print("----------------------------")
username = input("Enter your  username\n")
userid = input("enter your id\n")

print("User {} created with ID {} ",format(username,userid))
print("----------------------------")


# F method, it support python3
print("----------------------------")
username = input("Enter your  username\n")
userid = input("enter your id\n")

print(f"User {username} created with ID {userid}")
print("----------------------------")
