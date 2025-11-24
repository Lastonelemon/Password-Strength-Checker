import string

def check_strength(password):
    score = 0
    feedback = []
    
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
    
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")
    
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")
    
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("❌ Add numbers")
    
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%)")
    
    return score, feedback

def display_strength(score):
    bars = "█" * score + "░" * (6 - score)
    
    if score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"
    
    print(f"\n[{bars}] {score}/6")
    print(f"Strength: {strength}")

def generate_password(length=12):
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits
    special = "!@#$%^&*"
    
    password = ""
    for i in range(length):
        if i % 4 == 0:
            password += upper[i % len(upper)]
        elif i % 4 == 1:
            password += lower[i % len(lower)]
        elif i % 4 == 2:
            password += digits[i % len(digits)]
        else:
            password += special[i % len(special)]
    
    return password

print("=" * 50)
print("   PASSWORD STRENGTH CHECKER & GENERATOR")
print("=" * 50)

while True:
    print("\n1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")
    
    choice = input("\nEnter choice: ")
    
    if choice == '1':
        password = input("\nEnter password to check: ")
        score, feedback = check_strength(password)
        display_strength(score)
        
        if feedback:
            print("\nSuggestions:")
            for tip in feedback:
                print(f"  {tip}")
    
    elif choice == '2':
        length = input("\nPassword length (default 12): ")
        length = int(length) if length.isdigit() else 12
        
        new_pass = generate_password(length)
        print(f"\nGenerated Password: {new_pass}")
        
        score, _ = check_strength(new_pass)
        display_strength(score)
    
    elif choice == '3':
        print("\nStay secure!")
        break
    
    else:
        print("Invalid choice!")
