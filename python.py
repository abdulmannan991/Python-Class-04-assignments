import random

# Task #01
for i in range(1, 10, 2):  
    print(" " * ((10 - i) // 2) + "*" * i)

print("=====================")
# Task #02

for i in range(1,10,2):
    print(" " * ((10 - i) // 2)+ "*" * i)
   


for i in range(7, 0, -2):  
    print(" " * ((10 - i) // 2) + "*" * i)


print("=====================")

# Task #03
    
print("Welcome to the Guessing Game!")

random_num = str(random.randint(100, 999))

for _ in range(10):  # User gets 10 attempts
    user = input("\nGuess a 3-digit number: ")  # Get user input as string

    if len(user) != 3 or not user.isdigit():  # Ensure valid 3-digit number
        print("Please enter a valid 3-digit number.")
        continue

    feedback = ["❌", "❌", "❌"]  # Default to "Wrong"
    used_indices = set()  # Track correctly matched digits

    # First pass: Exact matches (Correct place)
    for i in range(3):
        if user[i] == random_num[i]:
            feedback[i] = "👌"  # Correct digit in the correct place
            used_indices.add(i)

    # Second pass: Misplaced matches (Wrong place)
    for i in range(3):
        if feedback[i] == "👌":  # Skip already matched digits
            continue
        for j in range(3):
            if i != j and user[i] == random_num[j] and j not in used_indices:
                feedback[i] = "👍"  # Correct digit in the wrong place
                used_indices.add(j)
                break

    # Display results
    print(" ".join(feedback), "or", " ".join(["Correct" if f == "👌" else "Ok" if f == "👍" else "Wrong" for f in feedback]))

    # If guessed correctly, end game
    if user == random_num:
        print("\n👌👌👌 or Correct Correct Correct or You Got IT!")
        break

print("\nThe correct number was:", random_num)
