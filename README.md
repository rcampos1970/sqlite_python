# Simple SQLAlchemy Example

This is a simple Python script that demonstrates the use of SQLAlchemy to create a SQLite database, define a table (`Person`), and populate it with random data.

## Requirements
- Python 3.x
- SQLAlchemy

## Setup
1. Install the required dependencies using the following command:
   ```bash
   pip install sqlalchemy
   ```

2. Run the script:
   ```bash
   python your_script_name.py
   ```

## Code Explanation
- The script defines a `Person` class representing a table with columns for SSN, first name, last name, gender, and age.
- It uses SQLAlchemy to create a SQLite database (`mydb.db`) and generates random data to populate the `people` table.
- Finally, it queries all records from the `Person` table and prints the results.

Feel free to modify the script and use it as a starting point for your SQLAlchemy projects.
