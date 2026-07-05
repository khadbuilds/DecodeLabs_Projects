# Project 4: General Knowledge Quiz

# Initialize the score variable to 0
score = 0

print("Welcome to the General Knowledge Quiz")

# --- Question 1 ---
user_answer1 = input("\nQuestion 1: What is the capital of France? ")
# Clean up the input by removing spaces and changing to lowercase
clean_answer1 = user_answer1.strip().lower()

if clean_answer1 == "paris":
    print("Correct! You got a point.")
    score = score + 1
else:
    print("Incorrect answer.")


# --- Question 2 ---
user_answer2 = input("\nQuestion 2: What planet is known as the Red Planet? ")
clean_answer2 = user_answer2.strip().lower()

if clean_answer2 == "mars":
    print("Correct! You got a point.")
    score = score + 1
else:
    print("Incorrect answer.")


# --- Question 3 ---
user_answer3 = input("\nQuestion 3: What is the largest ocean on Earth? ")
clean_answer3 = user_answer3.strip().lower()

if clean_answer3 == "pacific" or clean_answer3 == "pacific ocean":
    print("Correct! You got a point.")
    score = score + 1
else:
    print("Incorrect answer.")


# --- Final Results ---
print("\n--- Quiz Report ---")
print(f"Final Score: {score} out of 3 questions correct.")

if score == 3:
    print("Rank: Perfect Score!")
else:
    print("Rank: Completed.")