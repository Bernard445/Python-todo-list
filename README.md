This project is a simple command-line To-Do List Application built using Python.
It allows users to add, view, and delete tasks, while practicing core Python concepts such as:

Variables & lists

Functions

Loops

Conditionals

User input

Error handling (try / except / else / finally)

This project was created as part of a Python assignment.

🔧 Features
✔ Add Tasks

Users can enter any task, and it will be stored in a Python list.

✔ View Tasks

Displays all saved tasks, with numbering.
If there are no tasks, the program alerts the user.

✔ Delete Tasks

Users can delete a task by entering its task number.
The program validates the number and uses full error handling.

✔ Quit

The user can exit the program cleanly.

🛠️ How It Works

When the program runs, the user sees a menu:

Welcome
1. Add Task
2. View Task
3. Delete Task
4. Quit


The user types 1, 2, 3, or 4 to choose an option.
If they enter something invalid, they are shown an error and asked again.

All tasks are stored in a list:

tasks = []

🧪 Error Handling

This project includes:

try / except to catch invalid inputs

else to run code only when input is valid

finally to run cleanup messages

Empty-list checks

Menu validation (invalid options show an error)

📂 Project Structure
todo_app.py
README.md


You only need one .py file for this assignment.

▶️ How to Run the Program

Install Python (if not already installed).

Open VS Code.

Open the folder containing the project.

Run the file in the terminal:

python todo_app.py


Use the menu to add, view, or delete tasks.

📘 Example
Welcome
1. Add Task
2. View Task
3. Delete Task
4. Quit
Enter your choice: 1
Please enter your task: Buy groceries
Task added!

Enter your choice: 2
Your tasks:
1. Buy groceries
