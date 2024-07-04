import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests

# Function to fetch answer from Wolfram Alpha API
def get_answer(question):
    app_id = 'UKHHE9-GGJV3KG49R'  # Replace with your actual Wolfram Alpha App ID
    base_url = "http://api.wolframalpha.com/v1/result"
    params = {
        'appid': app_id,
        'i': question
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()  # Raises HTTPError for bad responses
        return response.text
    except requests.exceptions.RequestException as e:
        return f"Error: {e}"

# Function to handle ask button click
def ask_question():
    question = question_entry.get("1.0", tk.END).strip()
    if not question:
        messagebox.showwarning("Input Error", "Please enter a question.")
        return

    response = get_answer(question)
    response_text.insert(tk.END, f"Q: {question}\nA: {response}\n\n")
    question_entry.delete("1.0", tk.END)

# Creating the main window
root = tk.Tk()
root.title("Question Answer Interface")
root.geometry("600x400")

# Creating the input field for questions
question_label = tk.Label(root, text="Enter your question:")
question_label.pack(pady=10)

question_entry = tk.Text(root, height=3, width=70)
question_entry.pack(pady=5)

ask_button = tk.Button(root, text="Ask", command=ask_question)
ask_button.pack(pady=10)

# Creating a scrolled text box to display the responses
response_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=70, height=15)
response_text.pack(pady=10)

# Running the application
root.mainloop()
