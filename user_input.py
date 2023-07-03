# ----------------
# -- User Input --
# ----------------

fName = input("What's Your First Name?")
mName = input("What's Your Middle Name?")
lName = input("What's Your Last Name?")

fName = fName.strip().capitalize() # chain method 
mName = mName.strip().capitalize() # chain method 
lName = lName.strip().capitalize() # chain method 

print(f"Hello {fName} {mName:.1s} {lName} Happy To See You.")
