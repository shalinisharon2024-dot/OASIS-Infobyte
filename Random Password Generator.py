"""
Oasis Infobyte Python Programming Internship
Task: Random Password Generator
Description: Generates highly secure, customizable passwords using 
letters, digits, and punctuation based on user preferences.
"""

import random
import string

def generate_password():
    print("=" * 45)
    print("     SECURE RANDOM PASSWORD GENERATOR     ")
    print("=" * 45)
    
    # Get password length with validation
    while True:
        try:
            length = int(input("Enter desired password length (minimum 6): "))
            if length < 6:
                print("❌ Password length must be at least 6 characters for security.")
                continue
            break
        except ValueError:
            print("❌ Invalid input! Please enter a valid integer.")

    # Get character set preferences
    print("\nConfigure Character Sets:")
    use_letters = input("Include letters (A-Z, a-z)? (y/n): ").strip().lower() == 'y'
    use_numbers = input("Include numbers (0-9)? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols (!@#$%^&*...)? (y/n): ").strip().lower() == 'y'

    # Build character pool dynamically
    character_pool = ""
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation

    # Fallback validation if no pool is selected
    if not character_pool:
        print("\n⚠️ No character sets selected! Defaulting to letters and numbers.")
        character_pool = string.ascii_letters + string.digits

    # Generate password securely
    password = "".join(random.choice(character_pool) for _ in range(length))

    print("\n" + "-" * 45)
    print(f"🔐 GENERATED PASSWORD:\n   {password}")
    print("-" * 45)

if __name__ == "__main__":
    generate_password()