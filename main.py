import tkinter as tk
from tkinter import ttk
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector

class RecruitmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recruitment Application")
        self.root.geometry("800x600")

        # Connect to MySQL Database
        self.db = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="recruiteapp"
        )
        self.cursor = self.db.cursor()

        # Create the main menu
        self.create_menu()

    def create_menu(self):
        # Create the main menu frame
        self.menu_frame = ttk.Frame(self.root)
        self.menu_frame.pack(pady=20)

        # Buttons to navigate between screens
        candidates_button = ttk.Button(self.menu_frame, text="Candidates", command=self.show_candidates)
        candidates_button.grid(row=0, column=0, padx=10)

        jobs_button = ttk.Button(self.menu_frame, text="Job Posts", command=self.show_job_posts)
        jobs_button.grid(row=0, column=1, padx=10)

    def show_candidates(self):
        # Destroy the current frame
        if hasattr(self, 'content_frame'):
            self.content_frame.destroy()

        # Create the candidates frame
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(pady=20)

        # Fetch data from the candidates table in the database, including job post information
        query = """
        SELECT candidates.candidate_id, candidates.name, candidates.email, candidates.phone, job_posts.title
        FROM candidates
        LEFT JOIN job_posts ON candidates.job_post_id = job_posts.job_id
        """
        self.cursor.execute(query)
        candidates_data = self.cursor.fetchall()

        # Display candidates in a treeview
        columns = ("ID", "Name", "Email", "Phone", "Job Post")
        tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
        for candidate_data in candidates_data:
            tree.insert("", "end", values=candidate_data)
        tree.grid(row=0, column=0)

    def show_job_posts(self):
        # Destroy the current frame
        if hasattr(self, 'content_frame'):
            self.content_frame.destroy()

        # Create the job posts frame
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(pady=20)

        # Fetch data from the job_posts table in the database
        self.cursor.execute("SELECT * FROM job_posts")
        job_posts = self.cursor.fetchall()

        # Display job posts in a treeview
        columns = ("ID", "Title", "Description", "Location", "Actions")
        tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        for col in columns:
            tree.heading(col, text=col)
        for job_post in job_posts:
            tree.insert("", "end", values=(job_post[0], job_post[1], job_post[2], job_post[3], job_post[0]))
        tree.grid(row=0, column=0)

        # Add buttons to add, update, and delete job posts
        add_button = ttk.Button(self.content_frame, text="Add Job Post", command=self.show_add_job_post_form)
        add_button.grid(row=1, column=0, pady=10, padx=5)


        delete_button = ttk.Button(self.content_frame, text="Delete Job Post", command=lambda: self.confirm_delete_job_post(tree))
        delete_button.grid(row=2, column=0, pady=10, padx=5)

        tree.bind("<Double-1>", lambda event: self.show_update_job_post_form(tree))

    def add_job_post(self, title, description, location):
        try:
            # Insert a new job post into the database
            query = "INSERT INTO job_posts (title, description, location) VALUES (%s, %s, %s)"
            values = (title, description, location)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the job posts screen to show the new job post
            self.show_job_posts()

            # Provide user feedback
            messagebox.showinfo("Success", "Job post added successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def confirm_delete_job_post(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            return

        # Ask for confirmation before deletion
        confirmation = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this job post?")
        if confirmation:
            # Delete the selected job post
            job_id = tree.item(selected_item)["values"][0]
            self.delete_job_post(job_id)

    def delete_job_post(self, job_id):
        try:
            # Delete the job post from the database
            query = "DELETE FROM job_posts WHERE job_id = %s"
            self.cursor.execute(query, (job_id,))
            self.db.commit()

            # Refresh the job posts screen to reflect the deletion
            self.show_job_posts()

            # Provide user feedback
            messagebox.showinfo("Success", "Job post deleted successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def show_add_job_post_form(self):
        # Create a frame for the form
        form_frame = ttk.Frame(self.content_frame)
        form_frame.grid(row=2, column=0, pady=10)

        # Form fields with labels and entry widgets
        title_label = ttk.Label(form_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = ttk.Entry(form_frame, width=40)
        title_entry.grid(row=0, column=1, padx=5, pady=5)

        description_label = ttk.Label(form_frame, text="Description:")
        description_label.grid(row=1, column=0, padx=5, pady=5)
        description_entry = ttk.Entry(form_frame, width=40)
        description_entry.grid(row=1, column=1, padx=5, pady=5)

        location_label = ttk.Label(form_frame, text="Location:")
        location_label.grid(row=2, column=0, padx=5, pady=5)
        location_entry = ttk.Entry(form_frame, width=40)
        location_entry.grid(row=2, column=1, padx=5, pady=5)

        # Button to submit the form
        submit_button = ttk.Button(form_frame, text="Submit", command=lambda: self.add_job_post(
            title_entry.get(), description_entry.get(), location_entry.get()))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def show_update_job_post_form(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            return

        # Retrieve job post details based on the selected item
        job_id = tree.item(selected_item)["values"][0]
        query = "SELECT * FROM job_posts WHERE job_id = %s"
        self.cursor.execute(query, (job_id,))
        job_post_details = self.cursor.fetchone()

        # Create a frame for the update form
        update_frame = ttk.Frame(self.content_frame)
        update_frame.grid(row=2, column=0, pady=10)

        # Form fields with labels and entry widgets pre-filled with existing data
        title_label = ttk.Label(update_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5)
        title_entry = ttk.Entry(update_frame, width=40)
        title_entry.grid(row=0, column=1, padx=5, pady=5)
        title_entry.insert(0, job_post_details[1])

        description_label = ttk.Label(update_frame, text="Description:")
        description_label.grid(row=1, column=0, padx=5, pady=5)
        description_entry = ttk.Entry(update_frame, width=40)
        description_entry.grid(row=1, column=1, padx=5, pady=5)
        description_entry.insert(0, job_post_details[2])

        location_label = ttk.Label(update_frame, text="Location:")
        location_label.grid(row=2, column=0, padx=5, pady=5)
        location_entry = ttk.Entry(update_frame, width=40)
        location_entry.grid(row=2, column=1, padx=5, pady=5)
        location_entry.insert(0, job_post_details[3])

        # Button to submit the update form
        submit_button = ttk.Button(update_frame, text="Update", command=lambda: self.update_job_post(
            job_id, title_entry.get(), description_entry.get(), location_entry.get()))
        submit_button.grid(row=3, column=0, columnspan=2, pady=10)

    def update_job_post(self, job_id, title, description, location):
        try:
            # Update the job post in the database
            query = "UPDATE job_posts SET title=%s, description=%s, location=%s WHERE job_id=%s"
            values = (title, description, location, job_id)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the job posts screen to show the updated job post
            self.show_job_posts()

            # Provide user feedback
            messagebox.showinfo("Success", "Job post updated successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RecruitmentApp(root)
    root.mainloop()
