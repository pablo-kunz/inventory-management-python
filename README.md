# Hardware Store Inventory System 🔧

**Project — Programming 1**
Universidad Tecnológica Nacional (UTN) — Programming Technician Degree

**Developed by:** Pablo Kunz

---

## Description

Console-based inventory management application built in Python for a hardware store. Allows managing tools and their stock levels through a structured menu, applying functions, dictionaries, error handling, and input validation.

---

## Project Structure
├── main.py         # Entry point: menu and program flow
└── inventory.py    # Core logic: load, search, update and report functions

---

## Requirements

- Python 3.x (no external libraries required)

---

## How to Run

1. Clone or download this repository.
2. Make sure both files are in the same folder.
3. Run from the terminal:

```bash
python3 main.py
```

---

## Features

1. Initial stock load — add multiple tools at once
2. Display full inventory
3. Search tool by name
4. Report out-of-stock tools
5. Add new product
6. Update stock — register sales (decrease) or restocking (increase)
7. Exit

---

## Key Concepts Applied

- Modular design separating logic (`inventory.py`) from program flow (`main.py`)
- Functions for each menu option
- Dictionaries to store tool data (`name`, `quantity`)
- `try/except` for robust input validation
- Duplicate name detection (case-insensitive)
- Negative stock prevention

---

## Example Output
========== MAIN MENU ==========

Initial tool stock load
Display inventory
Check stock
Out-of-stock report
Add new product
Update stock (Sale / Restock)
Exit
================================
