#step 3: the patient arrives, we start a list of symptoms

print("Welcome to Password Triage")
print ("Every password is a patient. Lets assess yours.\n")

password = input("Enter a password to assess: ")
length = len(password)

symptoms = []

if length < 8:
    symptoms.append("too short (under 8 characters)")
elif length < 12:
    symptoms.append("A bit short (under12 characters)")
if len(symptoms) == 0:
    print("\n No symptoms found. The patient is healthy!")
else:
  print("\n Symptoms found:")
  for symptom in symptoms:
    print("-", symptom)
