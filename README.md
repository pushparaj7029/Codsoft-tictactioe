Tic‑Tac‑Toe AI (Python)
An unbeatable Tic‑Tac‑Toe game built using the Minimax algorithm. This project was created as part of an internship task in the domain of Artificial Intelligence.

📌 Project Overview
This project implements a fully playable Tic‑Tac‑Toe game where:

The human player plays as X

The AI agent plays as O

The AI uses the Minimax algorithm to ensure it never loses

All moves and results are saved automatically in a file named response.txt

The goal of this project is to understand:

Game theory

Adversarial search

Minimax decision-making

Basic AI implementation in Python

🧠 How the AI Works (Minimax Algorithm)
The Minimax algorithm is a recursive search strategy used in two‑player turn‑based games. The AI assumes:

It should maximize its chances of winning

The human opponent will minimize the AI’s chances

The algorithm explores all possible future game states and assigns scores:

+1 → AI wins

–1 → Human wins

0 → Draw

The AI then chooses the move that leads to the highest guaranteed score, making it unbeatable.

📁 Features
✅ Human vs AI gameplay ✅ AI uses Minimax (no randomness) ✅ AI is unbeatable ✅ Clean console interface ✅ All moves saved to response.txt ✅ Easy to understand and modify

▶️ How to Run the Game
1. Install Python
Make sure Python 3.x is installed on your system.

2. Save the project files
main.py → contains the game code

response.txt → will be created automatically

3. Run the game
Open a terminal and run:

Code
python main.py
📄 File Logging (response.txt)
Every game automatically logs:

Human moves

AI moves

Final result

Game start

Example log:

Code
New Game Started
Human played at position 4
AI played at position 0
Human played at position 8
AI played at position 2
Result: AI wins
This is useful for:

Debugging

Analysis

Internship documentation

🕹️ Game Controls
The board positions are numbered like this:

Code
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8
Enter a number (0–8) to place your move.

📚 Technologies Used
Python 3

Minimax Algorithm

File Handling

Basic Game Theory

🧩 Future Improvements
You can extend this project by adding:

Alpha‑Beta pruning (faster AI)

GUI using Tkinter or Pygame

Web version using JavaScript

Difficulty levels (Easy, Medium, Hard)

Scoreboard system

✅ Author
This project was developed as part of an internship task in Artificial Intelligence.
