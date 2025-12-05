# Sentiment Analyzer – Python + Flask

This project implements a simple sentiment analyzer based on predefined lists of positive and negative words.  
The application was initially built as a terminal script and later migrated to a web interface using Flask.  
The main goal was to build confidence working with applied logic, pure functions, HTTP routes, and the integration between a Python backend and a minimalist HTML interface.

---

## Project Objective

The project was developed to practice:

- Structuring logic into reusable functions.
- Basic text processing in Python.
- Separation of business logic and interface.
- Creating a minimal web application using Flask.
- Implementing forms and handling POST requests.

The focus is not to replicate advanced NLP techniques, but to build a functional application that receives user input, processes data, and returns a structured result.

---

## How the Algorithm Works

The algorithm follows a simple logic:

1. Receives a sentence typed by the user.
2. Splits the sentence into words.
3. Removes basic punctuation.
4. Normalizes each word to lowercase.
5. Checks whether the word is in the list of positive or negative terms.
6. Counts how many positive and negative words appear.
7. Determines the sentiment based on the counts:
   - more positive words → "Positive"
   - more negative words → "Negative"
   - equal amounts → "Neutral"

This logic was isolated into a pure function, enabling reuse and simplifying integration with the web layer.

---

## Technologies Used

- Python 3  
- Flask  
- Basic HTML  
- Simple data structures (lists, strings)  
- Pure functions and control flow

---

## Running the Project

### Clone the repository

git clone git@github.com:Gustavo-Barcellos/sentiment-analyser.git
cd sentiment-analyser

### Create a virtual environment (optional but recommended)

python3 -m venv venv
source venv/bin/activate

### Install dependencies

pip install -r requirements.txt

### Run the Flask server

python3 app.py

### Access the application

http://localhost:5000

---

## Key Points Worked on During Development

- Converting a CLI script into a web application.
- Correct use of routes and HTTP methods in Flask.
- Removal of dependency on global variables in the algorithm.
- Understanding request/response flow and handling form data.
- Minimal folder organization for a real web project.
- Creating an analysis function independent of the environment in which it runs.

These points demonstrate practical backend fundamentals and data-handling skills applicable in larger projects and technical interviews.

---

## Final Considerations

This project served as practical training in logic, basic web development, and code organization.  
The structure is intentionally simple, focusing on clarity and on understanding each step of the process: input → processing → output.
