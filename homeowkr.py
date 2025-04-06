import pgzrun
users = {
    "alex": "1234",
    "mia": "password",
    "sam": "letmein"
}

input_username = input("enter your username") 
input_password = input("Please enter the password")


#for user in users:
 #  if user==input_username:
  #   if users[user]==input_password:
   #     print("Access granted")
if input_username in users:
    if users[input_username]==input_password:
        print("Access granted")
    else:
        print("Invalid password")
else:
    print("Invalid username")