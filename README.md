# Book-Tracker-CLI-application

# Book Tracker CLI Project

## Project Overview

This is a **Command Line Interface (CLI)** application built in Python that helps users manage a collection of books and authors. It uses an **SQLite database** via **SQLAlchemy ORM** to store data. Users can add books, view books, search for authors, and perform various CRUD (Create, Read, Update, Delete) operations.

---

## Features

SQLAlchemy ORM for database management  
CLI with menu-driven interface  
3 related tables: `Book`, `Author`, `Genre`  
Seed script to prepopulate the database  
Debug script for development  
Helper functions for core logic  
Organized project structure  
Pipenv for environment management

---

## Project Structure

Book-Tracker-CLI/
├── Pipfile
├── Pipfile.lock
├── README.md (Master README)
├── lib/
│ ├── cli.py
│ ├── debug.py
│ ├── helpers.py
│ ├── seed.py
│
├── models/
│ ├── init.py
│ ├── book.py
│ ├── author.py
│ ├── genre.py
│
└── Readmes/
  |--  Readme for each file

---

## Getting Started

### 1. Install Dependencies

```bash
pipenv install
This installs:

SQLAlchemy

ipdb (for debugging)

2️. Set Your PYTHONPATH
Before running any scripts, set the PYTHONPATH so Python knows where to look for modules.

bash
Copy
Edit
export PYTHONPATH=.


3️. Run the Seed Script
bash
Copy
Edit
python lib/seed.py
 It should add the database with sample data.

4️. Run the CLI
bash
Copy
Edit
python lib/cli.py
 Interact with the app through the terminal!

5️. Run the Debug Script (Optional)
bash
Copy
Edit
python lib/debug.py
 Drops into an interactive debugging shell (ipdb).

 Helpful Commands
Command	Description
python lib/seed.py	Seed the database with data
python lib/cli.py	Run the CLI application
python lib/debug.py	Open a debug shell (if needed)
export PYTHONPATH=.	Set Python module search path
pipenv install	Install dependencies
