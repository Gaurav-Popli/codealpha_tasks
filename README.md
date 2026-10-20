# Hangman Game | CodeAlpha Python Internship

## Overview

Hangman is a command-line word guessing game developed using Python as part of the **CodeAlpha Python Programming Internship (October–November 2026)**.

The objective is to guess a randomly selected hidden word, one letter at a time, before exhausting the maximum number of incorrect attempts.

## Features

- **Random Word Selection:** Randomly chooses a word from a predefined list of five words.
- **Limited Attempts:** Players have a maximum of six incorrect guesses.
- **Input Validation:** Accepts only single alphabetic characters.
- **Duplicate Guess Detection:** Prevents repeated guesses.
- **Progress Tracking:** Displays correctly guessed letters and hides remaining letters.
- **Guess History:** Shows all previously guessed letters.
- **Win/Loss Detection:** Displays appropriate messages when the player wins or loses.

## Technologies Used

- **Language:** Python 3
- **Library:** `random` (Python Standard Library)
- **Interface:** Command Line Interface (CLI)

No external packages are required.

## How to Run

1. Install Python 3 on your computer.
2. Download or clone this repository.
3. Open a terminal in the project directory.
4. Run the following command:

```bash
python hangman.py
```

## Sample Gameplay

```text
===================
Welcome to Hangman Game
===================
Guess the hidden word! You have 6 incorrect attempts.

Word: _ _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: None

Guess a letter: p
Correct guess!

Word: p _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: p

Guess a letter: z
Wrong guess!

Word: p _ _ _ _ _
Incorrect guesses left: 5
Guessed letters: p, z
```

*Sample output illustrates gameplay; the actual word is randomly selected.*

## How It Works

1. The program randomly selects a secret word.
2. The player enters one letter per turn.
3. Correct guesses reveal matching letters in the hidden word.
4. Incorrect guesses reduce the remaining attempts.
5. Repeated guesses and invalid inputs do not consume attempts.
6. The player wins by identifying all letters or loses after six incorrect guesses.

## Project Structure

```text
CodeAlpha_Hangman_Game/
├── hangman.py
└── README.md
```

## Internship Details

- **Organization:** CodeAlpha
- **Domain:** Python Programming
- **Task:** Task 1 – Hangman Game
- **Batch:** 10 October 2026 – 10 November 2026
- **Project Type:** Python CLI Application

## Learning Outcomes

This project demonstrates fundamental Python programming concepts, including:

- Functions and control flow
- Loops and conditional statements
- Lists and strings
- Random selection
- User input validation
- Basic game logic

## Acknowledgment

Developed as part of the CodeAlpha Python Programming Internship to strengthen practical programming and problem-solving skills.
