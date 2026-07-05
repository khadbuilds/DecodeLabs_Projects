import secrets
import string
import math

print("Enterprise Random Password Generator (NIST 2024)")

while True:
    try:
        user_input = input("Enter desired password length (15 to 64 characters): ")
        length = int(user_input)
        
        if length < 15 or length > 64:
            print("Security Error: Length must be between 15 and 64 characters.")
            continue
            
        break
        
    except ValueError:
        print("Input Error: Please enter a valid whole number.")

character_pool = string.ascii_letters + string.digits + string.punctuation
pool_size = len(character_pool)

# Changed to a standard for-loop (how a student would actually write it)
password_list = []
for i in range(length):
    random_char = secrets.choice(character_pool)
    password_list.append(random_char)

final_password = "".join(password_list)

entropy = length * math.log2(pool_size)

print("\n--- System Report ---")
print(f"Generated Password: {final_password}")
print(f"Password Length: {length} characters")
print(f"Pool Size: {pool_size} characters")
print(f"Shannon Entropy: {entropy:.2f} bits")

if entropy >= 100:
    print("Security Status: Enterprise Grade")
else:
    print("Security Status: Strong")