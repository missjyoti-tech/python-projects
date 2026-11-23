print("="*20)
print("PASSWORD STRENGTH CHECKER")
print("="*20)

password = input ("Enter a password:")
special ="!@#$%^&*()"
score = 0
suggestions = []

if len(password)>=8:
    score +=1
else:
    suggestions.append("USe at least 8 characters")
    
 
if any(char.isupper() for char in password):
    score +=1
else:
    suggestions.append("Add uppercase letters")
    
    
if any(char.islower() for char in password):
    score+=1
else:
    suggestions.append("Add lowercase letters")
   
if any(char.isdigit() for char in password):
    score+=1
else:
   suggestions.append("Add numbers")
   
if any(char in special for char in password):
    score +=1
else:
    suggestions.append("Add special characters")

print("\nPassword Analysis")
if score<=2:
    print("Strength : Weak")
elif score<=4:
    print("Strength : Medium")
else:
    print("Strength : Strong")

print("\nSuggestions:")
if len(suggestions)==0:
    print("Your password is Strong! No suggestions needed.")
else:
    for item in suggestions:
        print("-",item)

    
