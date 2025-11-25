import string

def check_strength(password):
    score = 0
    feedback = []
    
    # Optimization: Convert string to set for O(1) lookups
    special_chars = set(string.punctuation)
    
    # Optimization: Single pass flags
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False
    
    # Optimization: Iterate through password only once - O(N)
    for c in password:
        if c.isupper():
            has_upper = True
        elif c.islower():
            has_lower = True
        elif c.isdigit():
            has_digit = True
        elif c in special_chars:
            has_special = True
            
    # Calculate Score
    if len(password) >= 8:
        score += 2
    else:
        feedback.append("❌ Too short (minimum 8 characters)")
    
    if has_upper:
        score += 1
    else:
        feedback.append("❌ Add uppercase letters")
    
    if has_lower:
        score += 1
    else:
        feedback.append("❌ Add lowercase letters")
    
    if has_digit:
        score += 1
    else:
        feedback.append("❌ Add numbers")
    
    if has_special:
        score += 1
    else:
        feedback.append("❌ Add special characters (!@#$%)")
    
    return score, feedback

def display_strength(score):
    # Capping score at 6 for the visual bar to prevent errors
    safe_score = min(score, 6)
    bars = "█" * safe_score + "░" * (6 - safe_score)
    
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
    
    # Optimization: Use a list instead of string concatenation
    # String concatenation is O(N^2), List join is O(N)
    password_chars = []
    
    len_upper = len(upper)
    len_lower = len(lower)
    len_digits = len(digits)
    len_special = len(special)

    for i in range(length):
        if i % 4 == 0:
            password_chars.append(upper[i % len_upper])
        elif i % 4 == 1:
            password_chars.append(lower[i % len_lower])
        elif i % 4 == 2:
            password_chars.append(digits[i % len_digits])
        else:
            password_chars.append(special[i % len_special])
    
    return "".join(password_chars)

# --- Main Execution ---
print("=" * 50)
print("   PASSWORD STRENGTH CHECKER & GENERATOR (Optimized)")
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
        length_input = input("\nPassword length (default 12): ")
        # Safe integer conversion
        length = int(length_input) if length_input.isdigit() else 12
        
        new_pass = generate_password(length)
        print(f"\nGenerated Password: {new_pass}")
        
        score, _ = check_strength(new_pass)
        display_strength(score)
    
    elif choice == '3':
        print("\nStay secure!")
        break
    
    else:
        print("Invalid choice!")
