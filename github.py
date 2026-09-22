import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime


BOOKS_FILE = "books.json"
MEMBERS_FILE = "members.json"


# ---------------------------------------------------------
# FILE HANDLING
# ---------------------------------------------------------

def load_data(filename):
    if not os.path.exists(filename):
        return []

    try:
        with open(filename, "r") as file:
            return json.load(file)

    except (json.JSONDecodeError, FileNotFoundError):
        return []


def save_data(filename, data):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)


books = load_data(BOOKS_FILE)
members = load_data(MEMBERS_FILE)


# ---------------------------------------------------------
# MAIN APPLICATION
# ---------------------------------------------------------

class LibraryManagementSystem:

    def __init__(self, root):

        self.root = root

        self.root.title("Library Management System")
        self.root.geometry("1100x700")
        self.root.minsize(950, 600)

        self.setup_style()
        self.create_header()
        self.create_notebook()

        self.refresh_books()
        self.refresh_members()
        self.refresh_issue_list()


    # -----------------------------------------------------
    # STYLE
    # -----------------------------------------------------

    def setup_style(self):

        style = ttk.Style()

        try:
            style.theme_use("clam")
        except:
            pass

        style.configure(
            "TButton",
            font=("Arial", 10),
            padding=7
        )

        style.configure(
            "Treeview",
            font=("Arial", 10),
            rowheight=28
        )

        style.configure(
            "Treeview.Heading",
            font=("Arial", 10, "bold")
        )

        style.configure(
            "TLabel",
            font=("Arial", 10)
        )


    # -----------------------------------------------------
    # HEADER
    # -----------------------------------------------------

    def create_header(self):

        header = tk.Frame(
            self.root,
            bg="#2c3e50",
            height=80
        )

        header.pack(fill="x")
        header.pack_propagate(False)

        title = tk.Label(
            header,
            text="📚 LIBRARY MANAGEMENT SYSTEM",
            font=("Arial", 22, "bold"),
            bg="#2c3e50",
            fg="white"
        )

        title.pack(pady=22)


    # -----------------------------------------------------
    # NOTEBOOK
    # -----------------------------------------------------

    def create_notebook(self):

        self.notebook = ttk.Notebook(self.root)

        self.notebook.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.create_dashboard_tab()
        self.create_books_tab()
        self.create_members_tab()
        self.create_issue_tab()


    # -----------------------------------------------------
    # DASHBOARD
    # -----------------------------------------------------

    def create_dashboard_tab(self):

        self.dashboard_tab = ttk.Frame(self.notebook)

        self.notebook.add(
            self.dashboard_tab,
            text="Dashboard"
        )

        title = tk.Label(
            self.dashboard_tab,
            text="Library Dashboard",
            font=("Arial", 20, "bold")
        )

        title.pack(pady=30)

        cards_frame = tk.Frame(self.dashboard_tab)

        cards_frame.pack(pady=20)

        self.total_books_label = self.create_card(
            cards_frame,
            "Total Books",
            "0",
            "#3498db"
        )

        self.available_books_label = self.create_card(
            cards_frame,
            "Available Books",
            "0",
            "#27ae60"
        )

        self.issued_books_label = self.create_card(
            cards_frame,
            "Issued Books",
            "0",
            "#e67e22"
        )

        self.total_members_label = self.create_card(
            cards_frame,
            "Members",
            "0",
            "#8e44ad"
        )

        self.update_dashboard()


    def create_card(self, parent, title, value, color):

        frame = tk.Frame(
            parent,
            bg=color,
            width=200,
            height=130
        )

        frame.pack(side="left", padx=15)

        frame.pack_propagate(False)

        title_label = tk.Label(
            frame,
            text=title,
            font=("Arial", 12, "bold"),
            bg=color,
            fg="white"
        )

        title_label.pack(pady=(20, 5))

        value_label = tk.Label(
            frame,
            text=value,
            font=("Arial", 25, "bold"),
            bg=color,
            fg="white"
        )

        value_label.pack()

        return value_label


    def update_dashboard(self):

        total_books = len(books)

        available_books = sum(
            1 for book in books
            if book["status"] == "Available"
        )

        issued_books = sum(
            1 for book in books
            if book["status"] == "Issued"
        )

        total_members = len(members)

        self.total_books_label.config(
            text=str(total_books)
        )

        self.available_books_label.config(
            text=str(available_books)
        )

        self.issued_books_label.config(
            text=str(issued_books)
        )

        self.total_members_label.config(
            text=str(total_members)
        )


    # -----------------------------------------------------
    # BOOKS TAB
    # -----------------------------------------------------

    def create_books_tab(self):

        self.books_tab = ttk.Frame(self.notebook)

        self.notebook.add(
            self.books_tab,
            text="Books"
        )

        form_frame = ttk.LabelFrame(
            self.books_tab,
            text="Add New Book"
        )

        form_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            form_frame,
            text="Book ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.book_id_entry = ttk.Entry(
            form_frame,
            width=20
        )

        self.book_id_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form_frame,
            text="Title:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.book_title_entry = ttk.Entry(
            form_frame,
            width=25
        )

        self.book_title_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Label(
            form_frame,
            text="Author:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.book_author_entry = ttk.Entry(
            form_frame,
            width=20
        )

        self.book_author_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form_frame,
            text="Category:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10
        )

        self.book_category_entry = ttk.Entry(
            form_frame,
            width=25
        )

        self.book_category_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            form_frame,
            text="Add Book",
            command=self.add_book
        ).grid(
            row=2,
            column=0,
            columnspan=4,
            pady=10
        )

        # Search

        search_frame = ttk.Frame(self.books_tab)

        search_frame.pack(
            fill="x",
            padx=10,
            pady=5
        )

        ttk.Label(
            search_frame,
            text="Search:"
        ).pack(
            side="left",
            padx=5
        )

        self.search_entry = ttk.Entry(
            search_frame,
            width=40
        )

        self.search_entry.pack(
            side="left",
            padx=5
        )

        ttk.Button(
            search_frame,
            text="Search",
            command=self.search_books
        ).pack(
            side="left",
            padx=5
        )

        ttk.Button(
            search_frame,
            text="Show All",
            command=self.refresh_books
        ).pack(
            side="left",
            padx=5
        )

        # Table

        table_frame = ttk.Frame(self.books_tab)

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "id",
            "title",
            "author",
            "category",
            "status"
        )

        self.books_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.books_tree.heading(
            "id",
            text="Book ID"
        )

        self.books_tree.heading(
            "title",
            text="Title"
        )

        self.books_tree.heading(
            "author",
            text="Author"
        )

        self.books_tree.heading(
            "category",
            text="Category"
        )

        self.books_tree.heading(
            "status",
            text="Status"
        )

        self.books_tree.column(
            "id",
            width=100
        )

        self.books_tree.column(
            "title",
            width=250
        )

        self.books_tree.column(
            "author",
            width=200
        )

        self.books_tree.column(
            "category",
            width=150
        )

        self.books_tree.column(
            "status",
            width=120
        )

        scrollbar = ttk.Scrollbar(
            table_frame,
            orient="vertical",
            command=self.books_tree.yview
        )

        self.books_tree.configure(
            yscrollcommand=scrollbar.set
        )

        self.books_tree.pack(
            side="left",
            fill="both",
            expand=True
        )

        scrollbar.pack(
            side="right",
            fill="y"
        )

        ttk.Button(
            self.books_tab,
            text="Delete Selected Book",
            command=self.delete_book
        ).pack(pady=5)


    # -----------------------------------------------------
    # ADD BOOK
    # -----------------------------------------------------

    def add_book(self):

        book_id = self.book_id_entry.get().strip()
        title = self.book_title_entry.get().strip()
        author = self.book_author_entry.get().strip()
        category = self.book_category_entry.get().strip()

        if not book_id or not title or not author or not category:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all book fields."
            )

            return

        for book in books:

            if book["id"] == book_id:

                messagebox.showerror(
                    "Error",
                    "Book ID already exists."
                )

                return

        book = {
            "id": book_id,
            "title": title,
            "author": author,
            "category": category,
            "status": "Available",
            "issued_to": "",
            "issue_date": ""
        }

        books.append(book)

        save_data(
            BOOKS_FILE,
            books
        )

        messagebox.showinfo(
            "Success",
            "Book added successfully."
        )

        self.clear_book_fields()
        self.refresh_books()
        self.update_dashboard()


    def clear_book_fields(self):

        self.book_id_entry.delete(0, tk.END)
        self.book_title_entry.delete(0, tk.END)
        self.book_author_entry.delete(0, tk.END)
        self.book_category_entry.delete(0, tk.END)


    # -----------------------------------------------------
    # REFRESH BOOKS
    # -----------------------------------------------------

    def refresh_books(self):

        for item in self.books_tree.get_children():
            self.books_tree.delete(item)

        for book in books:

            self.books_tree.insert(
                "",
                "end",
                values=(
                    book["id"],
                    book["title"],
                    book["author"],
                    book["category"],
                    book["status"]
                )
            )

        self.update_dashboard()


    # -----------------------------------------------------
    # SEARCH BOOKS
    # -----------------------------------------------------

    def search_books(self):

        query = self.search_entry.get().strip().lower()

        for item in self.books_tree.get_children():
            self.books_tree.delete(item)

        for book in books:

            if (
                query in book["id"].lower()
                or query in book["title"].lower()
                or query in book["author"].lower()
                or query in book["category"].lower()
            ):

                self.books_tree.insert(
                    "",
                    "end",
                    values=(
                        book["id"],
                        book["title"],
                        book["author"],
                        book["category"],
                        book["status"]
                    )
                )


    # -----------------------------------------------------
    # DELETE BOOK
    # -----------------------------------------------------

    def delete_book(self):

        selected = self.books_tree.selection()

        if not selected:

            messagebox.showwarning(
                "Selection",
                "Please select a book."
            )

            return

        values = self.books_tree.item(
            selected[0],
            "values"
        )

        book_id = values[0]

        for book in books:

            if book["id"] == book_id:

                if book["status"] == "Issued":

                    messagebox.showerror(
                        "Error",
                        "Issued books cannot be deleted."
                    )

                    return

                books.remove(book)

                save_data(
                    BOOKS_FILE,
                    books
                )

                messagebox.showinfo(
                    "Success",
                    "Book deleted successfully."
                )

                self.refresh_books()
                self.update_dashboard()

                return


    # -----------------------------------------------------
    # MEMBERS TAB
    # -----------------------------------------------------

    def create_members_tab(self):

        self.members_tab = ttk.Frame(self.notebook)

        self.notebook.add(
            self.members_tab,
            text="Members"
        )

        form = ttk.LabelFrame(
            self.members_tab,
            text="Add Library Member"
        )

        form.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Member ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.member_id_entry = ttk.Entry(
            form,
            width=20
        )

        self.member_id_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Name:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.member_name_entry = ttk.Entry(
            form,
            width=25
        )

        self.member_name_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Phone:"
        ).grid(
            row=1,
            column=0,
            padx=10,
            pady=10
        )

        self.member_phone_entry = ttk.Entry(
            form,
            width=20
        )

        self.member_phone_entry.grid(
            row=1,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            form,
            text="Email:"
        ).grid(
            row=1,
            column=2,
            padx=10,
            pady=10
        )

        self.member_email_entry = ttk.Entry(
            form,
            width=25
        )

        self.member_email_entry.grid(
            row=1,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            form,
            text="Add Member",
            command=self.add_member
        ).grid(
            row=2,
            column=0,
            columnspan=4,
            pady=10
        )

        table_frame = ttk.Frame(
            self.members_tab
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "id",
            "name",
            "phone",
            "email"
        )

        self.members_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.members_tree.heading(
            "id",
            text="Member ID"
        )

        self.members_tree.heading(
            "name",
            text="Name"
        )

        self.members_tree.heading(
            "phone",
            text="Phone"
        )

        self.members_tree.heading(
            "email",
            text="Email"
        )

        self.members_tree.column(
            "id",
            width=120
        )

        self.members_tree.column(
            "name",
            width=200
        )

        self.members_tree.column(
            "phone",
            width=150
        )

        self.members_tree.column(
            "email",
            width=250
        )

        self.members_tree.pack(
            fill="both",
            expand=True
        )

        ttk.Button(
            self.members_tab,
            text="Delete Selected Member",
            command=self.delete_member
        ).pack(pady=5)


    # -----------------------------------------------------
    # ADD MEMBER
    # -----------------------------------------------------

    def add_member(self):

        member_id = self.member_id_entry.get().strip()
        name = self.member_name_entry.get().strip()
        phone = self.member_phone_entry.get().strip()
        email = self.member_email_entry.get().strip()

        if not member_id or not name or not phone or not email:

            messagebox.showwarning(
                "Missing Information",
                "Please fill all member fields."
            )

            return

        for member in members:

            if member["id"] == member_id:

                messagebox.showerror(
                    "Error",
                    "Member ID already exists."
                )

                return

        member = {
            "id": member_id,
            "name": name,
            "phone": phone,
            "email": email
        }

        members.append(member)

        save_data(
            MEMBERS_FILE,
            members
        )

        messagebox.showinfo(
            "Success",
            "Member added successfully."
        )

        self.member_id_entry.delete(0, tk.END)
        self.member_name_entry.delete(0, tk.END)
        self.member_phone_entry.delete(0, tk.END)
        self.member_email_entry.delete(0, tk.END)

        self.refresh_members()
        self.update_dashboard()


    # -----------------------------------------------------
    # REFRESH MEMBERS
    # -----------------------------------------------------

    def refresh_members(self):

        for item in self.members_tree.get_children():
            self.members_tree.delete(item)

        for member in members:

            self.members_tree.insert(
                "",
                "end",
                values=(
                    member["id"],
                    member["name"],
                    member["phone"],
                    member["email"]
                )
            )

        self.update_dashboard()


    # -----------------------------------------------------
    # DELETE MEMBER
    # -----------------------------------------------------

    def delete_member(self):

        selected = self.members_tree.selection()

        if not selected:

            messagebox.showwarning(
                "Selection",
                "Please select a member."
            )

            return

        values = self.members_tree.item(
            selected[0],
            "values"
        )

        member_id = values[0]

        for book in books:

            if book["issued_to"] == member_id:

                messagebox.showerror(
                    "Error",
                    "This member currently has an issued book."
                )

                return

        for member in members:

            if member["id"] == member_id:

                members.remove(member)

                save_data(
                    MEMBERS_FILE,
                    members
                )

                messagebox.showinfo(
                    "Success",
                    "Member deleted successfully."
                )

                self.refresh_members()
                self.update_dashboard()

                return


    # -----------------------------------------------------
    # ISSUE / RETURN TAB
    # -----------------------------------------------------

    def create_issue_tab(self):

        self.issue_tab = ttk.Frame(
            self.notebook
        )

        self.notebook.add(
            self.issue_tab,
            text="Issue / Return"
        )

        # Issue section

        issue_frame = ttk.LabelFrame(
            self.issue_tab,
            text="Issue Book"
        )

        issue_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            issue_frame,
            text="Book ID:"
        ).grid(
            row=0,
            column=0,
            padx=10,
            pady=10
        )

        self.issue_book_entry = ttk.Entry(
            issue_frame,
            width=25
        )

        self.issue_book_entry.grid(
            row=0,
            column=1,
            padx=10,
            pady=10
        )

        ttk.Label(
            issue_frame,
            text="Member ID:"
        ).grid(
            row=0,
            column=2,
            padx=10,
            pady=10
        )

        self.issue_member_entry = ttk.Entry(
            issue_frame,
            width=25
        )

        self.issue_member_entry.grid(
            row=0,
            column=3,
            padx=10,
            pady=10
        )

        ttk.Button(
            issue_frame,
            text="Issue Book",
            command=self.issue_book
        ).grid(
            row=1,
            column=0,
            columnspan=4,
            pady=10
        )

        # Return section

        return_frame = ttk.LabelFrame(
            self.issue_tab,
            text="Return Book"
        )

        return_frame.pack(
            fill="x",
            padx=10,
            pady=10
        )

        ttk.Label(
            return_frame,
            text="Book ID:"
        ).pack(
            side="left",
            padx=10
        )

        self.return_book_entry = ttk.Entry(
            return_frame,
            width=25
        )

        self.return_book_entry.pack(
            side="left",
            padx=10
        )

        ttk.Button(
            return_frame,
            text="Return Book",
            command=self.return_book
        ).pack(
            side="left",
            padx=10
        )

        # Issued books table

        table_frame = ttk.LabelFrame(
            self.issue_tab,
            text="Currently Issued Books"
        )

        table_frame.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        columns = (
            "book_id",
            "title",
            "member_id",
            "member_name",
            "issue_date"
        )

        self.issue_tree = ttk.Treeview(
            table_frame,
            columns=columns,
            show="headings"
        )

        self.issue_tree.heading(
            "book_id",
            text="Book ID"
        )

        self.issue_tree.heading(
            "title",
            text="Book Title"
        )

        self.issue_tree.heading(
            "member_id",
            text="Member ID"
        )

        self.issue_tree.heading(
            "member_name",
            text="Member Name"
        )

        self.issue_tree.heading(
            "issue_date",
            text="Issue Date"
        )

        self.issue_tree.column(
            "book_id",
            width=100
        )

        self.issue_tree.column(
            "title",
            width=250
        )

        self.issue_tree.column(
            "member_id",
            width=120
        )

        self.issue_tree.column(
            "member_name",
            width=200
        )

        self.issue_tree.column(
            "issue_date",
            width=150
        )

        self.issue_tree.pack(
            fill="both",
            expand=True
        )


    # -----------------------------------------------------
    # ISSUE BOOK
    # -----------------------------------------------------

    def issue_book(self):

        book_id = self.issue_book_entry.get().strip()
        member_id = self.issue_member_entry.get().strip()

        if not book_id or not member_id:

            messagebox.showwarning(
                "Missing Information",
                "Enter Book ID and Member ID."
            )

            return

        selected_book = None

        for book in books:

            if book["id"] == book_id:
                selected_book = book
                break

        if selected_book is None:

            messagebox.showerror(
                "Error",
                "Book not found."
            )

            return

        if selected_book["status"] == "Issued":

            messagebox.showerror(
                "Error",
                "This book is already issued."
            )

            return

        selected_member = None

        for member in members:

            if member["id"] == member_id:
                selected_member = member
                break

        if selected_member is None:

            messagebox.showerror(
                "Error",
                "Member not found."
            )

            return

        selected_book["status"] = "Issued"
        selected_book["issued_to"] = member_id

        selected_book["issue_date"] = datetime.now().strftime(
            "%Y-%m-%d %H:%M"
        )

        save_data(
            BOOKS_FILE,
            books
        )

        messagebox.showinfo(
            "Success",
            f"Book issued to {selected_member['name']}."
        )

        self.issue_book_entry.delete(
            0,
            tk.END
        )

        self.issue_member_entry.delete(
            0,
            tk.END
        )

        self.refresh_books()
        self.refresh_issue_list()
        self.update_dashboard()


    # -----------------------------------------------------
    # RETURN BOOK
    # -----------------------------------------------------

    def return_book(self):

        book_id = self.return_book_entry.get().strip()

        if not book_id:

            messagebox.showwarning(
                "Missing Information",
                "Enter Book ID."
            )

            return

        selected_book = None

        for book in books:

            if book["id"] == book_id:
                selected_book = book
                break

        if selected_book is None:

            messagebox.showerror(
                "Error",
                "Book not found."
            )

            return

        if selected_book["status"] == "Available":

            messagebox.showerror(
                "Error",
                "This book is not currently issued."
            )

            return

        selected_book["status"] = "Available"
        selected_book["issued_to"] = ""
        selected_book["issue_date"] = ""

        save_data(
            BOOKS_FILE,
            books
        )

        messagebox.showinfo(
            "Success",
            "Book returned successfully."
        )

        self.return_book_entry.delete(
            0,
            tk.END
        )

        self.refresh_books()
        self.refresh_issue_list()
        self.update_dashboard()


    # -----------------------------------------------------
    # REFRESH ISSUE LIST
    # -----------------------------------------------------

    def refresh_issue_list(self):

        for item in self.issue_tree.get_children():
            self.issue_tree.delete(item)

        for book in books:

            if book["status"] == "Issued":

                member_name = "Unknown"

                for member in members:

                    if member["id"] == book["issued_to"]:

                        member_name = member["name"]

                        break

                self.issue_tree.insert(
                    "",
                    "end",
                    values=(
                        book["id"],
                        book["title"],
                        book["issued_to"],
                        member_name,
                        book["issue_date"]
                    )
                )


# ---------------------------------------------------------
# PROGRAM START
# ---------------------------------------------------------

if __name__ == "__main__":

    root = tk.Tk()

    app = LibraryManagementSystem(root)

    root.mainloop()

LibraryManagementSystem