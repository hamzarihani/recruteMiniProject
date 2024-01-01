import customtkinter
import tkinter as tk
from tkinter import ttk
from tkinter import Scrollbar
from tkinter import simpledialog
from tkinter import messagebox
import mysql.connector
from tkinter import Toplevel
import ttkbootstrap as ttkb
from ttkbootstrap.constants import *

class RecruitmentApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Recruitment Application")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_position = (screen_width - 1300) // 2
        y_position = (screen_height - 700) // 2

        self.root.geometry(f"{1300}x{700}+{x_position}+{y_position}")
        self.add_job_post_window_open = False 
        self.update_job_post_window_open = False
        self.add_candidate_window_open = False
        self.update_candidate_window_open = False

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
        SELECT candidat.ID_candidat, candidat.nom_prenom, candidat.email, candidat.telephone,
            candidat.competence, candidat.diplome, candidat.experience, candidat.location, candidat.status, candidat.note, poste.titre
        FROM candidat
        LEFT JOIN poste ON candidat.ID_poste = poste.ID_poste
        """
        self.cursor.execute(query)
        candidates_data = self.cursor.fetchall()

        # Display candidates in a treeview
        columns = ("REF", "Name", "Email", "Phone", "Skills", "Diploma", "Experience", "Location", "Status", "Note", "Poste")
        # tree = ttk.Treeview(self.content_frame, columns=columns, show="headings")
        tree = ttk.Treeview(self.content_frame, columns=columns, show="headings", height=20)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=110)
        tree.column(columns[0], width=40)

        for candidate_data in candidates_data:
            tree.insert("", "end", values=candidate_data)

        tree.grid(row=0, column=0)

        # Add buttons to add and delete candidates
        add_button = ttkb.Button(self.content_frame, text="Add Candidate", width=16, bootstyle=SUCCESS, command=self.show_add_candidate_form)
        add_button.grid(row=1, column=0, pady=10, padx=5)

        delete_button = ttkb.Button(self.content_frame, text="Delete Candidate", width=16, bootstyle=DANGER, command=lambda: self.confirm_delete_candidate(tree))
        delete_button.grid(row=2, column=0, pady=10, padx=5)

        tree.bind("<Double-1>", lambda event: self.show_update_candidate_form(tree))

    def show_add_candidate_form(self):
        # Check if the window is already open
        if self.add_candidate_window_open:
            # You may show a message or take some action if the window is already open
            messagebox.showinfo("Info", "Add Candidate form is already open.")
            return

        # Set the variable to True since the window is about to be opened
        self.add_candidate_window_open = True
        # Create a new Toplevel window for the form
        add_candidate_window = Toplevel(self.root)
        add_candidate_window.title("Add Candidate Form")

        # Bind the window's protocol to set the variable to False when the window is closed
        add_candidate_window.protocol("WM_DELETE_WINDOW", lambda: self.on_add_candidate_window_close())

        # Calculate the position to center the window on the screen
        screen_width = add_candidate_window.winfo_screenwidth()
        screen_height = add_candidate_window.winfo_screenheight()
        window_width = 600  # Set your desired window width
        window_height = 500  # Set your desired window height

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Use the geometry method to set the size and position of the window
        add_candidate_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame for the form inside the new window
        form_frame = ttk.Frame(add_candidate_window)
        form_frame.pack(pady=10)

        # Form fields with labels and entry widgets
        name_label = ttk.Label(form_frame, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        name_entry = ttk.Entry(form_frame, width=40)
        name_entry.grid(row=1, column=0, padx=5, pady=5)

        email_label = ttk.Label(form_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        email_entry = ttk.Entry(form_frame, width=40)
        email_entry.grid(row=3, column=0, padx=5, pady=5,sticky="w")

        phone_label = ttk.Label(form_frame, text="Phone:")
        phone_label.grid(row=4, column=0, padx=5, pady=5,sticky="w")
        phone_entry = ttk.Entry(form_frame, width=40)
        phone_entry.grid(row=5, column=0, padx=5, pady=5,sticky="w")

        competence_label = ttk.Label(form_frame, text="Skills:")
        competence_label.grid(row=6, column=0, padx=5, pady=5,sticky="w")
        competence_entry = ttk.Entry(form_frame, width=40)
        competence_entry.grid(row=7, column=0, padx=5, pady=5,sticky="w")

        # Diploma field as a dropdown select
        diploma_label = ttk.Label(form_frame, text="Diploma:")
        diploma_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        diploma_entry = tk.StringVar()
        diploma_combobox = ttk.Combobox(form_frame, width=37, textvariable=diploma_entry, state="readonly")
        # Add your diploma options to the combobox
        diploma_combobox['values'] = ("Sans_diplome","Bac", "Bac+3", "Bac+5")  # Replace with your actual options
        diploma_combobox.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        diploma_combobox.set(diploma_combobox['values'][0]) 

        experience_label = ttk.Label(form_frame, text="Experience:")
        experience_label.grid(row=0, column=1, padx=5, pady=5,sticky="w")
        experience_entry = ttk.Entry(form_frame, width=40)
        experience_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")

        location_label = ttk.Label(form_frame, text="Location:")
        location_label.grid(row=2, column=1, padx=5, pady=5,sticky="w")
        location_entry = ttk.Entry(form_frame, width=40)
        location_entry.grid(row=3, column=1, padx=5, pady=5,sticky="w")

        # status_label = ttk.Label(form_frame, text="Status:")
        # status_label.grid(row=4, column=1, padx=5, pady=5,sticky="w")
        # status_entry = ttk.Entry(form_frame, width=40)
        # status_entry.grid(row=5, column=1, padx=5, pady=5,sticky="w")

        # Status field as a dropdown select
        status_label = ttk.Label(form_frame, text="Status:")
        status_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        status_entry = tk.StringVar()
        status_combobox = ttk.Combobox(form_frame, width=37, textvariable=status_entry, state="readonly")
        # Add your status options to the combobox
        status_combobox['values'] = ("Poubelle","Pourquoi_Pas", "Serieux")  # Replace with your actual options
        status_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        status_combobox.set(status_combobox['values'][0]) 

        # note_label = ttk.Label(form_frame, text="Note:")
        # note_label.grid(row=6, column=1, padx=5, pady=5,sticky="w")
        # note_entry = ttk.Entry(form_frame, width=40)
        # note_entry.grid(row=7, column=1, padx=5, pady=5,sticky="w")

        # note field as a dropdown select
        note_label = ttk.Label(form_frame, text="note:")
        note_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        note_entry = tk.StringVar()
        note_combobox = ttk.Combobox(form_frame, width=37, textvariable=note_entry, state="readonly")
        # Add your note options to the combobox
        note_combobox['values'] = ("1","2", "3","4","5")  # Replace with your actual options
        note_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        note_combobox.set(note_combobox['values'][0]) 

       # Poste field as a dropdown select
        poste_label = ttk.Label(form_frame, text="Poste:")
        poste_label.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        poste_entry = tk.StringVar()
        poste_combobox = ttk.Combobox(form_frame, width=37, textvariable=poste_entry, state="readonly")
        # Fetch existing postes from the database and set them as values
        postes_query = "SELECT ID_poste, titre FROM poste"
        self.cursor.execute(postes_query)
        poste_options = [(poste[0], poste[1]) for poste in self.cursor.fetchall()]
        poste_combobox['values'] = [poste[0] for poste in poste_options]
        poste_combobox['values'] = poste_options
        poste_combobox['state'] = "readonly"
        poste_combobox.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        poste_combobox.set(poste_options[0])  # Set the default selection
        print(poste_options[0])


        # Add more fields as needed

        # Button to submit the form
        submit_button = ttkb.Button(form_frame, text="Submit", bootstyle=PRIMARY, command=lambda: self.add_candidate(add_candidate_window,
            name_entry.get(), email_entry.get(), phone_entry.get(),
            competence_entry.get(), diploma_entry.get(), experience_entry.get(),
            location_entry.get(), status_entry.get(), note_entry.get(),
            poste_entry.get()))
        submit_button.grid(row=12, column=0, pady=20)

        # Button to cancel the form
        cancel_button = ttkb.Button(form_frame, text="Cancel", bootstyle=SECONDARY, command=lambda:self.cancel_add_candidate(add_candidate_window))
        cancel_button.grid(row=12, column=1)

    
    def on_add_candidate_window_close(self):
        # Set the variable to False when the window is closed
        self.add_candidate_window_open = False

    def cancel_add_candidate(self, window):
        # Set the variable to True since the window is closed
        self.add_candidate_window_open = False
        # Destroy the Toplevel window
        window.destroy()

    def show_update_candidate_form(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a candidate to update.")
            return

        # Set the variable to True since the window is about to be opened
        self.update_candidate_window_open = True

        # Retrieve candidate details based on the selected item
        candidate_id = tree.item(selected_item)["values"][0]
        query = "SELECT * FROM candidat WHERE ID_candidat = %s"
        self.cursor.execute(query, (candidate_id,))
        candidate_details = self.cursor.fetchone()

        # Create a new Toplevel window for the update form
        update_candidate_window = Toplevel(self.root)
        update_candidate_window.title("Update Candidate Form")

        # Bind the window's protocol to set the variable to False when the window is closed
        update_candidate_window.protocol("WM_DELETE_WINDOW", lambda: self.on_update_candidate_window_close())

        # Calculate the position to center the window on the screen
        screen_width = update_candidate_window.winfo_screenwidth()
        screen_height = update_candidate_window.winfo_screenheight()
        window_width = 600  # Set your desired window width
        window_height = 500  # Set your desired window height

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Use the geometry method to set the size and position of the window
        update_candidate_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")
        # Create a frame for the form inside the new window
        update_frame = ttk.Frame(update_candidate_window)
        update_frame.pack(pady=10)

        name_label = ttk.Label(update_frame, text="Name:")
        name_label.grid(row=0, column=0, padx=5, pady=5,sticky="w")
        name_entry = ttk.Entry(update_frame, width=40)
        name_entry.grid(row=1, column=0, padx=5, pady=5)
        name_entry.insert(0, candidate_details[1])

        email_label = ttk.Label(update_frame, text="Email:")
        email_label.grid(row=2, column=0, padx=5, pady=5,sticky="w")
        email_entry = ttk.Entry(update_frame, width=40)
        email_entry.grid(row=3, column=0, padx=5, pady=5,sticky="w")
        email_entry.insert(0, candidate_details[2])

        phone_label = ttk.Label(update_frame, text="Phone:")
        phone_label.grid(row=4, column=0, padx=5, pady=5,sticky="w")
        phone_entry = ttk.Entry(update_frame, width=40)
        phone_entry.grid(row=5, column=0, padx=5, pady=5,sticky="w")
        phone_entry.insert(0, candidate_details[3])

        competence_label = ttk.Label(update_frame, text="Skills:")
        competence_label.grid(row=6, column=0, padx=5, pady=5,sticky="w")
        competence_entry = ttk.Entry(update_frame, width=40)
        competence_entry.grid(row=7, column=0, padx=5, pady=5,sticky="w")
        competence_entry.insert(0, candidate_details[4])

        # Diploma field as a dropdown select
        diploma_label = ttk.Label(update_frame, text="Diploma:")
        diploma_label.grid(row=8, column=0, padx=5, pady=5, sticky="w")
        diploma_entry = tk.StringVar()
        diploma_combobox = ttk.Combobox(update_frame, width=37, textvariable=diploma_entry, state="readonly")
        # Add your diploma options to the combobox
        diploma_combobox['values'] = ("Sans_diplome","Bac", "Bac+3", "Bac+5")  # Replace with your actual options
        diploma_combobox.grid(row=9, column=0, padx=5, pady=5, sticky="w")
        diploma_combobox.set(candidate_details[5]) 

        experience_label = ttk.Label(update_frame, text="Experience:")
        experience_label.grid(row=0, column=1, padx=5, pady=5,sticky="w")
        experience_entry = ttk.Entry(update_frame, width=40)
        experience_entry.grid(row=1, column=1, padx=5, pady=5,sticky="w")
        experience_entry.insert(0, candidate_details[6])

        location_label = ttk.Label(update_frame, text="Location:")
        location_label.grid(row=2, column=1, padx=5, pady=5,sticky="w")
        location_entry = ttk.Entry(update_frame, width=40)
        location_entry.grid(row=3, column=1, padx=5, pady=5,sticky="w")
        location_entry.insert(0, candidate_details[7])

        # Status field as a dropdown select
        status_label = ttk.Label(update_frame, text="Status:")
        status_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        status_entry = tk.StringVar()
        status_combobox = ttk.Combobox(update_frame, width=37, textvariable=status_entry, state="readonly")
        # Add your status options to the combobox
        status_combobox['values'] = ("Poubelle","Pourquoi_Pas", "Serieux")  # Replace with your actual options
        status_combobox.grid(row=5, column=1, padx=5, pady=5, sticky="w")
        status_combobox.set(candidate_details[8]) 

        # note field as a dropdown select
        note_label = ttk.Label(update_frame, text="note:")
        note_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        note_entry = tk.StringVar()
        note_combobox = ttk.Combobox(update_frame, width=37, textvariable=note_entry, state="readonly")
        # Add your note options to the combobox
        note_combobox['values'] = ("1","2", "3","4","5")  # Replace with your actual options
        note_combobox.grid(row=7, column=1, padx=5, pady=5, sticky="w")
        note_combobox.set(candidate_details[9])

       # Poste field as a dropdown select
        poste_label = ttk.Label(update_frame, text="Poste:")
        poste_label.grid(row=8, column=1, padx=5, pady=5, sticky="w")
        poste_entry = tk.StringVar()
        poste_combobox = ttk.Combobox(update_frame, width=37, textvariable=poste_entry, state="readonly")

        # Fetch existing postes from the database and set them as values
        postes_query = "SELECT ID_poste, titre FROM poste"
        self.cursor.execute(postes_query)
        poste_options = [(poste[0], poste[1]) for poste in self.cursor.fetchall()]

        # Set the fetched postes as values for the combobox
        poste_combobox['values'] = poste_options

        # Set the selected value based on the candidate's details
        selected_poste_id = candidate_details[10]
        selected_poste = next((poste for poste in poste_options if poste[0] == selected_poste_id), None)

        poste_combobox['state'] = "readonly"
        poste_combobox.grid(row=9, column=1, padx=5, pady=5, sticky="w")
        if selected_poste:
            poste_combobox.set(selected_poste[1])
        print(selected_poste)


        # Button to submit the update form
        submit_button = ttkb.Button(update_frame, text="Update", command=lambda: self.update_candidate(
            update_candidate_window, candidate_id, name_entry.get(), email_entry.get(), phone_entry.get(),
            competence_entry.get(), diploma_entry.get(), experience_entry.get(),
            location_entry.get(), status_entry.get(), note_entry.get(), poste_combobox.get()))
        submit_button.grid(row=13, column=0, pady=20)


        # Button to cancel the form
        cancel_button = ttkb.Button(update_frame, text="Cancel", bootstyle=SECONDARY, command=lambda:self.cancel_update_candidate(update_candidate_window))
        cancel_button.grid(row=13, column=1)

    def update_candidate(self, window, candidate_id, name, email, phone, competence, diploma, experience, location, status, note, poste_id):
        try:
            if diploma == "Sans_diplome":
                diplomeNum = 0
            elif diploma == "Bac":
                diplomeNum = 1
            elif diploma == "Bac+3":
                diplomeNum = 3
            elif diploma == "Bac+5":
                diplomeNum = 5
            else:
                # Handle other cases or set a default value
                diplomeNum = 0 
            # Update the candidate information in the database
            query = """
                UPDATE candidat
                SET nom_prenom = %s, email = %s, telephone = %s, competence = %s, 
                    diplome = %s, diplomeNum = %s, experience = %s, location = %s, status = %s, note = %s, ID_poste = %s
                WHERE ID_candidat = %s
            """
            values = (name, email, phone, competence, diploma, diplomeNum, experience, location, status, note, poste_id, candidate_id)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the candidates screen to show the updated information
            self.show_candidates()
            self.cancel_update_candidate(window)

            # Provide user feedback
            messagebox.showinfo("Success", "Candidate information updated successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def on_update_candidate_window_close(self):
        # Set the variable to False when the window is closed
        self.update_candidate_window_open = False

    def cancel_update_candidate(self, window):
        # Set the variable to True since the window is closed
        self.update_candidate_window_open = False
        # Destroy the Toplevel window
        window.destroy()


    def add_candidate(self, window, name, email, phone, competence, diploma, experience, location, status, note, poste):
        try:
            if diploma == "Sans_diplome":
                diplomeNum = 0
            elif diploma == "Bac":
                diplomeNum = 1
            elif diploma == "Bac+3":
                diplomeNum = 3
            elif diploma == "Bac+5":
                diplomeNum = 5
            else:
                # Handle other cases or set a default value
                diplomeNum = 0 
            # Insert a new candidate into the database
            query = """
                INSERT INTO candidat (nom_prenom, email, telephone, competence, diplome, diplomeNum, experience, location, status, note, ID_poste)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (name, email, phone, competence, diploma, diplomeNum, experience, location, status, note, poste)
            print(values)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the candidates screen to show the new candidate
            self.show_candidates()
            self.add_candidate_window_open = False

            # Close the add candidate window
            window.destroy()

            # Provide user feedback
            messagebox.showinfo("Success", "Candidate added successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def confirm_delete_candidate(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a candidate to delete.")
            return

        # Ask for confirmation before deleting
        confirmation = messagebox.askyesno("Confirmation", "Are you sure you want to delete the selected candidate?")
        if confirmation:
            self.delete_candidate(tree)

    def delete_candidate(self, tree):
        try:
            # Get the candidate ID from the selected item in the treeview
            selected_item = tree.selection()
            candidate_id = tree.item(selected_item)["values"][0]

            # Delete the candidate from the database
            query = "DELETE FROM candidat WHERE ID_candidat = %s"
            self.cursor.execute(query, (candidate_id,))
            self.db.commit()

            # Refresh the candidates screen to show the updated list
            self.show_candidates()

            # Provide user feedback
            messagebox.showinfo("Success", "Candidate deleted successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")


    def show_job_posts(self):
        # Destroy the current frame
        if hasattr(self, 'content_frame'):
            self.content_frame.destroy()

        # Create the job posts frame
        self.content_frame = ttk.Frame(self.root)
        self.content_frame.pack(pady=10)

        # Fetch data from the job_posts table in the database
        self.cursor.execute("SELECT * FROM poste")
        job_posts = self.cursor.fetchall()

        # Display job posts in a treeview
        columns = ("REF", "Title", "Description", "Mission", "Skils","Diploma","Experience","Salary","Location")
        tree = ttkb.Treeview(self.content_frame, columns=columns, show="headings", height=20)
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=130)
        tree.column(columns[0], width=40)
        for job_post in job_posts:
            tree.insert("", "end", values=(job_post[0], job_post[1], job_post[2], job_post[3], job_post[4],job_post[5],job_post[6],job_post[7],job_post[8]))
        tree.grid(row=0, column=0)


         # Add buttons to add, update, and delete job posts
        add_button = ttkb.Button(self.content_frame, text="Add", bootstyle=SUCCESS, width=16, command=self.show_add_job_post_form)
        #add_button.grid(row=1, column=0)
        add_button.grid(row=1, column=0, pady=10, padx=5)

        delete_button = ttkb.Button(self.content_frame, text="Delete", bootstyle=DANGER,width=16, command=lambda: self.confirm_delete_job_post(tree))
        #delete_button.grid(row=2, column=0)
        delete_button.grid(row=2, column=0, pady=10, padx=5)


        tree.bind("<Double-1>", lambda event: self.show_update_job_post_form(tree))


    def add_job_post(self,window, title, description, post, skills, diploma, experience, salary, location):
        try:
            # Insert a new job post into the database
            query = """
            INSERT INTO poste (titre, description, mission, competence, diplome, experience, salaire, location)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            values = (title, description, post, skills, diploma, experience, salary, location)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the job posts screen to show the new job post
            self.show_job_posts()
            self.cancel_add_job_post(window)
            self.add_job_post_window_open = False

            # Provide user feedback
            messagebox.showinfo("Success", "Job post added successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

    def confirm_delete_job_post(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            messagebox.showinfo("Info", "Please select a post to delete.")
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
            query = "DELETE FROM poste WHERE ID_poste = %s"
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
        # Check if the window is already open
        if self.add_job_post_window_open:
            # You may show a message or take some action if the window is already open
            messagebox.showinfo("Info", "Add Job Post form is already open.")
            return

        # Set the variable to True since the window is about to be opened
        self.add_job_post_window_open = True

        # Create a new Toplevel window
        add_job_post_window = Toplevel(self.root)
        add_job_post_window.title("Add Post Form")

        # Bind the window's protocol to set the variable to False when the window is closed
        add_job_post_window.protocol("WM_DELETE_WINDOW", lambda: self.on_add_job_post_window_close())

        # Calculate the position to center the window on the screen
        screen_width = add_job_post_window.winfo_screenwidth()
        screen_height = add_job_post_window.winfo_screenheight()
        window_width = 600  # Set your desired window width
        window_height = 400  # Set your desired window height

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Use the geometry method to set the size and position of the window
        add_job_post_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame for the form inside the new window
        form_frame = ttk.Frame(add_job_post_window)
        form_frame.pack(pady=10)

        # Form fields with labels and entry widgets
        title_label = ttk.Label(form_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        title_entry = ttk.Entry(form_frame, width=40)
        title_entry.grid(row=1, column=0, padx=5, pady=5)

        description_label = ttk.Label(form_frame, text="Description:")
        description_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        description_entry = ttk.Entry(form_frame, width=40)
        description_entry.grid(row=3, column=0, padx=5, pady=5)

        post_label = ttk.Label(form_frame, text="Post:")
        post_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        post_entry = ttk.Entry(form_frame, width=40)
        post_entry.grid(row=5, column=0, padx=5, pady=5)

        skills_label = ttk.Label(form_frame, text="Skills:")
        skills_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        skills_entry = ttk.Entry(form_frame, width=40)
        skills_entry.grid(row=7, column=0, padx=5, pady=5)

        diploma_label = ttk.Label(form_frame, text="Diploma:")
        diploma_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        diploma_entry = ttk.Entry(form_frame, width=40)
        diploma_entry.grid(row=1, column=1, padx=5, pady=5)

        experience_label = ttk.Label(form_frame, text="Experience:")
        experience_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        experience_entry = ttk.Entry(form_frame, width=40)
        experience_entry.grid(row=3, column=1, padx=5, pady=5)

        salary_label = ttk.Label(form_frame, text="Salary:")
        salary_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        salary_entry = ttk.Entry(form_frame, width=40)
        salary_entry.grid(row=5, column=1, padx=5, pady=5)

        location_label = ttk.Label(form_frame, text="Location:")
        location_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        location_entry = ttk.Entry(form_frame, width=40)
        location_entry.grid(row=7, column=1, padx=5, pady=5)

        # Button to submit the form
        submit_button = ttkb.Button(form_frame, text="Submit", command=lambda: self.add_job_post(add_job_post_window,
            title_entry.get(), description_entry.get(), post_entry.get(),
            skills_entry.get(), diploma_entry.get(), experience_entry.get(),
            salary_entry.get(), location_entry.get()))
        submit_button.grid(row=8, column=0, pady=10)

        # Button to cancel the form
        cancel_button = ttkb.Button(form_frame, text="Cancel", style="TButton", bootstyle=DANGER, command=lambda: self.cancel_add_job_post(add_job_post_window))
        cancel_button.grid(row=8, column=1, pady=10)


    def on_add_job_post_window_close(self):
        # Set the variable to False when the window is closed
        self.add_job_post_window_open = False

    def cancel_add_job_post(self, window):
        # Set the variable to True since the window is closed
        self.add_job_post_window_open = False
        # Destroy the Toplevel window
        window.destroy()

    def show_update_job_post_form(self, tree):
        # Get the selected item from the treeview
        selected_item = tree.selection()
        if not selected_item:
            return

        # Retrieve job post details based on the selected item
        job_id = tree.item(selected_item)["values"][0]
        query = "SELECT * FROM poste WHERE ID_poste = %s"
        self.cursor.execute(query, (job_id,))
        job_post_details = self.cursor.fetchone()

        # Check if the update window is already open
        if self.update_job_post_window_open:
            messagebox.showinfo("Info", "Update Job Post form is already open.")
            return

        # Set the variable to True since the window is about to be opened
        self.update_job_post_window_open = True

        # Create a new Toplevel window
        update_job_post_window = Toplevel(self.root)
        update_job_post_window.title("Update Post Form")

        # Bind the window's protocol to set the variable to False when the window is closed
        update_job_post_window.protocol("WM_DELETE_WINDOW", lambda: self.on_update_job_post_window_close())

        # Calculate the position to center the window on the screen
        screen_width = update_job_post_window.winfo_screenwidth()
        screen_height = update_job_post_window.winfo_screenheight()
        window_width = 600  # Set your desired window width
        window_height = 400  # Set your desired window height

        x_position = (screen_width - window_width) // 2
        y_position = (screen_height - window_height) // 2

        # Use the geometry method to set the size and position of the window
        update_job_post_window.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Create a frame for the update form inside the new window
        update_frame = ttk.Frame(update_job_post_window)
        update_frame.pack(pady=10)

        # Form fields with labels and entry widgets pre-filled with existing data
        title_label = ttk.Label(update_frame, text="Title:")
        title_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")
        title_entry = ttk.Entry(update_frame, width=40)
        title_entry.grid(row=1, column=0, padx=5, pady=5)
        title_entry.insert(0, job_post_details[1])

        description_label = ttk.Label(update_frame, text="Description:")
        description_label.grid(row=2, column=0, padx=5, pady=5, sticky="w")
        description_entry = ttk.Entry(update_frame, width=40)
        description_entry.grid(row=3, column=0, padx=5, pady=5)
        description_entry.insert(0, job_post_details[2])

        post_label = ttk.Label(update_frame, text="Post:")
        post_label.grid(row=4, column=0, padx=5, pady=5, sticky="w")
        post_entry = ttk.Entry(update_frame, width=40)
        post_entry.grid(row=5, column=0, padx=5, pady=5)
        post_entry.insert(0, job_post_details[3])

        skills_label = ttk.Label(update_frame, text="Skills:")
        skills_label.grid(row=6, column=0, padx=5, pady=5, sticky="w")
        skills_entry = ttk.Entry(update_frame, width=40)
        skills_entry.grid(row=7, column=0, padx=5, pady=5)
        skills_entry.insert(0, job_post_details[4])

        diploma_label = ttk.Label(update_frame, text="Diploma:")
        diploma_label.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        diploma_entry = ttk.Entry(update_frame, width=40)
        diploma_entry.grid(row=1, column=1, padx=5, pady=5)
        diploma_entry.insert(0, job_post_details[5])

        experience_label = ttk.Label(update_frame, text="Experience:")
        experience_label.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        experience_entry = ttk.Entry(update_frame, width=40)
        experience_entry.grid(row=3, column=1, padx=5, pady=5)
        experience_entry.insert(0, job_post_details[6])

        salary_label = ttk.Label(update_frame, text="Salary:")
        salary_label.grid(row=4, column=1, padx=5, pady=5, sticky="w")
        salary_entry = ttk.Entry(update_frame, width=40)
        salary_entry.grid(row=5, column=1, padx=5, pady=5)
        salary_entry.insert(0, job_post_details[7])

        location_label = ttk.Label(update_frame, text="Location:")
        location_label.grid(row=6, column=1, padx=5, pady=5, sticky="w")
        location_entry = ttk.Entry(update_frame, width=40)
        location_entry.grid(row=7, column=1, padx=5, pady=5)
        location_entry.insert(0, job_post_details[8])

        # Button to submit the update form
        submit_button = ttkb.Button(update_frame, text="Update", command=lambda: self.update_job_post(update_job_post_window,
            job_id, title_entry.get(), description_entry.get(), post_entry.get(),
            skills_entry.get(), diploma_entry.get(), experience_entry.get(),
            salary_entry.get(), location_entry.get()))

        submit_button.grid(row=8, column=0, pady=10)

        # Button to cancel the update form
        cancel_button = ttkb.Button(update_frame, text="Cancel", style="TButton", bootstyle=DANGER, command=lambda: self.cancel_update_job_post(update_job_post_window))
        cancel_button.grid(row=8, column=1, pady=10)

    def cancel_update_job_post(self, window):
        # Set the variable to False since the window is closed
        self.update_job_post_window_open = False
        # Destroy the Toplevel window
        window.destroy()

    def on_update_job_post_window_close(self):
        # Set the variable to False when the window is closed
        self.update_job_post_window_open = False


    def update_job_post(self,window, job_id, title, description, mission, competence, diplome, experience, salaire, location):
        try:
            # Update the job post in the database
            query = "UPDATE poste SET titre=%s, description=%s, mission=%s, competence=%s, diplome=%s, experience=%s, salaire=%s, location=%s WHERE ID_poste=%s"
            values = (title, description, mission, competence, diplome, experience, salaire, location, job_id)
            self.cursor.execute(query, values)
            self.db.commit()

            # Refresh the job posts screen to show the updated job post
            self.show_job_posts()
            self.cancel_update_job_post(window)
            self.update_job_post_window_open = False

            # Provide user feedback
            messagebox.showinfo("Success", "Job post updated successfully!")

        except Exception as e:
            # Handle exceptions
            messagebox.showerror("Error", f"An error occurred: {str(e)}")



if __name__ == "__main__":
    root = tk.Tk()
    app = RecruitmentApp(root)
    root.mainloop()
