# Step 1: Ask for a password and count it's length

password = input("Enter a password to check: ")
length = len(password)
print("Your password is", length, "characters long.")

#Step 2: Decide if the passowrd is long enough

if length < 8:
  print("Too short! 😣 Aim for at least 12 characters.")
elif length < 12:
  print ("Okay length, but longer is stronger.")
else:
  print("Great length! ✔️")
