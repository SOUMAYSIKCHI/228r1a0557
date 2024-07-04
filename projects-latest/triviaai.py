import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

# Function to fetch a trivia question
def get_trivia_question():
    base_url = "https://opentdb.com/api.php"
    params = {
        'amount': 50,
        'type': 'multiple'
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        question = data['results'][0]['question']
        correct_answer = data['results'][0]['correct_answer']
        return f"{question}\nCorrect Answer: {correct_answer}"
    else:
        return "Error: Unable to get the question"

# Function to handle ask button click
def ask_question():
    response = get_trivia_question()
    response_text.insert(tk.END, f"Q: {response}\n\n")

# Creating the main window
root = tk.Tk()
root.title("Trivia Question Interface")
root.geometry("600x400")

# Creating the input field for questions
ask_button = tk.Button(root, text="Get Trivia Question", command=ask_question)
ask_button.pack(pady=20)

# Creating a scrolled text box to display the responses
response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
response_text.pack(pady=10)

# Running the application
root.mainloop()
