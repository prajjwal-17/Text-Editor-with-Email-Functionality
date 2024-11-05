# gui_text_editor_with_email.py

import tkinter as tk
from tkinter import filedialog, messagebox, simpledialog
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor with Email")

        # Initialize text area
        self.text_area = tk.Text(self.root, wrap="word", undo=True)
        self.text_area.pack(expand=1, fill="both")

        # Create a menu bar
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # File menu
        file_menu = tk.Menu(self.menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=file_menu)

        # Email menu
        email_menu = tk.Menu(self.menu_bar, tearoff=0)
        email_menu.add_command(label="Send Email", command=self.send_email)
        self.menu_bar.add_cascade(label="Email", menu=email_menu)

    def open_file(self):
        """Open a file for editing."""
        file_path = filedialog.askopenfilename(defaultextension=".txt",
                                               filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.root.title(f"Simple Text Editor - {file_path}")
            with open(file_path, 'r') as file:
                content = file.read()
            self.text_area.delete(1.0, tk.END)  # Clear current text area
            self.text_area.insert(tk.END, content)

    def save_file(self):
        """Save the current text to a file."""
        file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                                 filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            with open(file_path, 'w') as file:
                content = self.text_area.get(1.0, tk.END)
                file.write(content)
            self.root.title(f"Simple Text Editor - {file_path}")
            messagebox.showinfo("File Saved", "Your file has been saved successfully.")

    def send_email(self):
        """Send the editor's content as an email."""
        sender_email = simpledialog.askstring("Email", "Enter your email:")
        app_password = simpledialog.askstring("Password", "Enter your email app password:", show='*')
        recipient_email = simpledialog.askstring("Recipient", "Enter the recipient's email:")
        subject = simpledialog.askstring("Subject", "Enter the subject of the email:")

        if not (sender_email and app_password and recipient_email and subject):
            messagebox.showwarning("Missing Information", "Please fill out all fields.")
            return

        # Prepare the email message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = recipient_email
        message["Subject"] = subject

        content = self.text_area.get(1.0, tk.END)
        message.attach(MIMEText(content, "plain"))

        try:
            # Send the email using SMTP
            with smtplib.SMTP("smtp.gmail.com", 587) as server:
                server.starttls()  # Secure the connection
                server.login(sender_email, app_password)
                server.sendmail(sender_email, recipient_email, message.as_string())
            
            messagebox.showinfo("Email Sent", "The email was sent successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.geometry("600x400")  # Set default window size
    root.mainloop()
