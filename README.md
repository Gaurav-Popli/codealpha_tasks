# CodeAlpha Python Programming Internship

Welcome to my **CodeAlpha Python Programming Internship** repository!

This repository contains three Python projects developed during the **CodeAlpha Internship (10 October 2026 – 10 November 2026)**. These projects demonstrate fundamental Python programming concepts, logical problem-solving, file automation, and rule-based chatbot development.

## Internship Information

| Detail | Information |
|---|---|
| Organization | CodeAlpha |
| Domain | Python Programming |
| Internship Batch | October – November 2026 |
| Programming Language | Python 3 |
| Tasks Completed | 3 |
| Repository | `codealpha_tasks` |

---

## Projects

### Task 1: Hangman Game

A command-line word guessing game built using Python. The player must guess a randomly selected word before running out of attempts.

**Key Features:**
- Random word selection from a predefined list
- Six incorrect attempts allowed
- Interactive letter-by-letter guessing
- Input validation for alphabetic characters
- Detection of previously guessed letters
- Real-time word progress and remaining attempts
- Win and loss messages

**Technologies:** Python, `random` module

**Run the project:**

```bash
python Task_1_Hangman_Game/hangman.py
```

### Task 2: File Organizer

A Python automation script that automatically organizes JPEG image files into a dedicated folder.

**Key Features:**
- Accepts a user-defined source directory
- Creates a `JPEG_Images` folder automatically
- Detects `.jpg` and `.jpeg` files (case-insensitive)
- Moves matching images into the destination folder
- Displays the total number of files moved
- Supports the current working directory as the default location
- Handles invalid source directory paths

**Technologies:** Python, `os`, `shutil`

**Run the project:**

```bash
python Task_2_File_Organizer/file_organizer.py
```

**Note:** This script moves files rather than copying them. Use a test directory before organizing important files. Files with duplicate names in the destination may cause conflicts.

### Task 3: Rule-Based Chatbot

A simple interactive chatbot developed using Python that responds to predefined user queries using conditional statements.

**Key Features:**
- Responds to greetings such as `hello`, `hi`, and `hey`
- Answers basic conversational questions
- Provides information about CodeAlpha
- Case-insensitive text processing
- Handles unknown inputs with a default response
- Continuous interactive conversation
- Supports exit commands including `bye`, `exit`, and `quit`

**Technologies:** Python, conditional statements, string processing

**Run the project:**

```bash
python Task_3_Rule_Based_Chatbot/chatbot.py
```

---

## Repository Structure

```text
codealpha_tasks/
│
├── Task_1_Hangman_Game/
│   └── hangman.py
│
├── Task_2_File_Organizer/
│   └── file_organizer.py
│
├── Task_3_Rule_Based_Chatbot/
│   └── chatbot.py
│
└── README.md
```

## Installation and Setup

**Prerequisites:**
- Python 3 installed
- Terminal or command prompt
- Git (optional, for cloning)

**Step 1: Clone the repository**

```bash
git clone https://github.com/YOUR_USERNAME/codealpha_tasks.git
```

**Step 2: Navigate to the repository**

```bash
cd codealpha_tasks
```

**Step 3: Run any project**

For example:

```bash
python Task_1_Hangman_Game/hangman.py
```

All three projects use Python's standard library and require no additional package installation.

---

## Concepts and Skills Demonstrated

- Python fundamentals
- Functions, loops, and conditional statements
- Lists and string manipulation
- Input validation and user interaction
- Random word generation
- File handling and directory operations
- Task automation
- Rule-based conversational logic
- Problem-solving and algorithmic thinking

## Acknowledgment

I would like to thank **CodeAlpha** for providing the opportunity to gain hands-on experience through practical Python programming tasks.

These projects were developed as part of the CodeAlpha Python Programming Internship.

---

**CodeAlpha | Python Programming Internship | October–November 2026**
