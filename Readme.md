# Project 1: Simple To-Do List Engine

A straightforward command-line application that acts as a basic to-do list manager. This project showcases how to store data in the computer's memory, add new entries dynamically based on what the user types, and loop through the data to print it out clearly.

---

## How It Works

The program handles data management by breaking the tasks down into three simple steps:

1. Dynamic Storage: The script initializes a standard Python list containing initial baseline tasks. This list stays active in the system's memory while the program runs.
2. State Modification: When the user chooses option 1, the program collects their input and uses the `.append()` method to add the new task text right onto the end of the list.
3. Reading Data: When the user chooses option 2, the program checks if the list is empty. If it has items, it loops through the array using the `enumerate()` function to automatically number and display each task in sequence.

---

## Code Requirements Met

- Array Storage: Uses a standard Python list (`my_tasks`) to retain task data throughout the session.
- Input Collection: Uses the `.strip()` method on inputs to ensure accidental blank spaces do not mess up the choice selection or task names.
- Loop Engine: Implements a continuous `while True` loop to keep the menu active until the user manually inputs option 3 to exit.
- Sequence Iteration: Uses a `for` loop combined with `enumerate()` to dynamically display the list index along with the task text.

---

## How to Run the Program

1. Open your terminal window or the built-in VS Code terminal panel.
2. Navigate to the folder where your project is saved.
3. Run the following command:
   ```bash
   python todo_engine.py

https://github.com/user-attachments/assets/c8052021-be61-4bda-b844-bb3f6e22ffa9

---

# Project 2: Expense Tracker

A real-time command-line application designed to track running financial expenses using an Input-Process-Output (IPO) setup. The program continuously accepts number entries from a user, validates the data to ensure accuracy, adds it to a central counter, and outputs a finalized summary report when closed.

---

## How It Works

The script operates on a continuous processing cycle divided into three clear steps:

1. Keeping State: Before the calculation cycle begins, a tracking variable named `total` is set to 0 outside the loop. This ensures the program maintains memory across multiple entry cycles without wiping the running sum.
2. Error Proofing: To protect the system from crashing due to typing mistakes, the script wraps data translation inside a try-except defensive shield. If a user inputs text instead of a number, the system safely catches the error and alerts the user rather than terminating.
3. The Kill Switch: The program constantly monitors entries for a sentinel value. Typing the exact string 'quit' triggers a loop break, exiting the cycle gracefully to finalize the calculations.

---

## Code Requirements Met

- Outer Initialization: The accumulator variable lives entirely outside the loop structure to prevent data loss.
- Continuous Loop Engine: Implements a `while True` loop to handle an infinite amount of entries sequentially.
- Defensive Shielding: Incorporates a `try...except ValueError` block to handle bad data types without dropping the active execution process.
- Logic and Output Separation: Holds the final print reporting block outside the loop, meaning data formatting only runs once processing is finished.

---

## How to Run the Tracker

1. Open your terminal panel or the built-in VS Code terminal.
2. Navigate to the directory holding your project files.
3. Execute the script with the following command:
   ```bash
   python tracker.py

https://github.com/user-attachments/assets/560caed2-00ef-4aec-9f6f-46c85bc3ba48

---

# Project 3: Cryptographically Secure Password Generator

A cybersecurity-focused tool built to generate completely random, highly secure passwords based on modern NIST standards. The application takes a target length from the user, validates it, selects characters using secure hardware-level noise, and calculates the exact mathematical strength of the resulting password before displaying it.

---

## How It Works

The generator manages security through a strict three-phase process:

1. Length Boundaries: The program forces the user to input a password length between 15 and 64 characters. This adheres to modern security practices that focus on absolute length over complicated character rules to prevent computer guessing attacks.
2. Secure Selection Engine: Instead of using standard, predictable random functions, the script imports the built-in `secrets` module to choose characters. It loops for the exact length specified, pulling a highly unpredictable character from a combined pool of letters, numbers, and punctuation during each cycle.
3. Entropy Calculations: Before printing the password, the program uses the formula $E = L \times \log_2(R)$ to measure its information entropy. This provides an exact mathematical score of the password's strength, ensuring it meets enterprise safety standards.

---

## Code Requirements Met

- NIST Alignment: Restricts choices to a safe 15 to 64 character window using standard `if` condition gates.
- Advanced Randomness: Uses `secrets.choice()` to ensure the password cannot be mathematically guessed by hacking software.
- Memory Control: Assembles individual characters inside a temporary list first, then uses `"".join()` to bundle them into a single string instantly, which protects system memory from slowing down.
- Math Application: Employs the `math.log2()` function to programmatically verify and display the bit entropy of the output.

---

## How to Run the Generator

1. Open your terminal screen or use the built-in terminal tab in VS Code.
2. Navigate to the folder where your project files live.
3. Run the following command:
   ```bash
   python password_generator.py

https://github.com/user-attachments/assets/764d1456-0d45-46d9-9d6f-5d9e6a326a3f

---
# Project 4: General Knowledge Quiz

A dynamic command line quiz game built using an Input-Process-Output structure. The program asks the user three separate questions, checks their answers using conditional logic, tracks their points, and prints a final rank report at the end.

---

## How It Works

The program runs through three clear phases to manage the game logic:

1. Setting the Score: At the very start, a score variable is created and set to 0 so the program can track points correctly as the user answers questions.
2. Cleaning and Checking Input: When a user types an answer, the program automatically strips off any accidental spaces using .strip() and changes the letters to lowercase using .lower(). This ensures that capitalization or simple typing differences do not break the checking logic.
3. Point System: Using an if-else gate, the script updates the score by adding 1 (score = score + 1) if the clean answer matches the correct answer. If the answer is wrong, it prints an incorrect message and leaves the score exactly as it was.

---

## Code Requirements Met

- State Management: The score tracker is initialized outside of the question steps to keep the total count active.
- Input Cleaning: Uses both .strip() and .lower() to catch user typing variations.
- Logic Routing: Uses if-else conditional blocks to route the user down the correct or incorrect path.
- F-Strings: Uses dynamic string formatting to print the final score smoothly into the console report.

---

## How to Run the Quiz

1. Open your terminal window or the built-in VS Code terminal panel.
2. Navigate to the directory containing your project.
3. Run the following command:
   ```bash
   python quiz_game.py

https://github.com/user-attachments/assets/3a17014d-a74e-42a3-b80d-3fedbaeb3f36





