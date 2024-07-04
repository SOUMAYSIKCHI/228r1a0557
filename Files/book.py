import tkinter as tk
from tkinter import messagebox


class Book:
    def __init__(self, title, author, rating, summary, reviews, price):
        self.title = title
        self.author = author
        self.rating = rating
        self.summary = summary
        self.reviews = reviews
        self.price = price


class booknamed:
    def __init__(self, master):
        self.master = master
        self.master.title("Book Verse")

        # Dummy book data
        self.books = [
            Book(
                title="Book 1",
                author="Author 1",
                rating=4.3,
                summary="Summary of Book 1",
                reviews=["Great book!", "I loved it!", "Could be better."],
                price="$10"
            ),
            Book(
                title="Book 2",
                author="Author 2",
                rating=4.5,
                summary="Summary of Book 2",
                reviews=["Excellent read!", "Highly recommended!"],
                price="$15"
            ),
            Book(
                title="Book 3",
                author="Author 3",
                rating=4.0,
                summary="Summary of Book 3",
                reviews=["Good book!", "Enjoyed reading it."],
                price="$12"
            ),
            Book(
                title="Book 4",
                author="Author 3",
                rating=4.0,
                summary="Summary of Book 3",
                reviews=["Good book!", "Enjoyed reading it."],
                price="$12"
            ),
            Book(
                title="Book 5",
                author="Author 3",
                rating=4.0,
                summary="Summary of Book 3",
                reviews=["Good book!", "Enjoyed reading it."],
                price="$12"
            ),
            Book(
                title="Book 6",
                author="Author 3",
                rating=4.0,
                summary="Summary of Book 3",
                reviews=["Good book!", "Enjoyed reading it."],
                price="$12"
            ),
            # Add more books here
        ]

        self.create_widgets()

    def create_widgets(self):
        # Title
        lbl_title = tk.Label(self.master, text="Book Verse", font=("Helvetica", 24, "bold"), fg="blue")
        lbl_title.grid(row=0, column=0, columnspan=3, pady=10)

        # Book Grid
        row_num = 1
        col_num = 0
        for book in self.books:
            frame = tk.Frame(self.master, bd=2, relief=tk.RIDGE)
            frame.grid(row=row_num, column=col_num, padx=10, pady=10)

            lbl_book_title = tk.Label(frame, text=f"{book.title}", font=("Helvetica", 12, "bold"), fg="green")
            lbl_book_title.grid(row=0, column=0, columnspan=2, pady=5, sticky="w")

            lbl_author = tk.Label(frame, text=f"Author: {book.author}")
            lbl_author.grid(row=1, column=0, columnspan=2, pady=5, sticky="w")

            lbl_rating = tk.Label(frame, text=f"Rating: {book.rating}")
            lbl_rating.grid(row=2, column=0, columnspan=2, pady=5, sticky="w")

            lbl_price = tk.Label(frame, text=f"Price: {book.price}")
            lbl_price.grid(row=3, column=0, columnspan=2, pady=5, sticky="w")

            btn_buy = tk.Button(frame, text="Buy", command=lambda b=book: self.buy_ebook(b))
            btn_buy.grid(row=4, column=0, pady=5, padx=5, sticky="ew")

            btn_summary = tk.Button(frame, text="Summary", command=lambda b=book: self.get_summary(b))
            btn_summary.grid(row=4, column=1, pady=5, padx=5, sticky="ew")

            btn_reviews = tk.Button(frame, text="Reviews", command=lambda b=book: self.view_reviews(b))
            btn_reviews.grid(row=5, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            btn_rating = tk.Button(frame, text="Rating", command=lambda b=book: self.view_rating(b))
            btn_rating.grid(row=6, column=0, columnspan=2, pady=5, padx=5, sticky="ew")

            col_num += 1
            if col_num > 2:
                col_num = 0
                row_num += 1

    def buy_ebook(self, book):
        messagebox.showinfo("Buy eBook", f"You have bought '{book.title}' by {book.author} for {book.price}.")

    def get_summary(self, book):
        messagebox.showinfo("Book Summary", f"Summary of '{book.title}':\n\n{book.summary}")

    def view_reviews(self, book):
        reviews = "\n".join(book.reviews)
        messagebox.showinfo("Customer Reviews", f"Customer Reviews for '{book.title}':\n\n{reviews}")

    def view_rating(self, book):
        messagebox.showinfo("Book Rating", f"The rating for '{book.title}' is {book.rating}.")



win = tk.Tk()
win.geometry("600x1000")
win.resizable(False, False)
win.title("BOOK VERSE APP")
booknamed(win)
win.mainloop()