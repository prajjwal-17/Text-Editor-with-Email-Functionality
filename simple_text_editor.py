# simple_text_editor_with_email.py

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def open_file(filename):
    if os.path.exists(filename):
        with open(filename, 'r') as file:
            content = file.read()
            print("File opened successfully.\n")
    else:
        content = ""
        print("File does not exist. Creating a new file.\n")
    return content

def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    print("File saved successfully.\n")

def send_email(sender_email, app_password, recipient_email, subject, message):
    """Send an email using SMTP."""
    try:
    
        email_message = MIMEMultipart()
        email_message['From'] = sender_email
        email_message['To'] = recipient_email
        email_message['Subject'] = subject
        email_message.attach(MIMEText(message, 'plain'))

        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)
            server.sendmail(sender_email, recipient_email, email_message.as_string())

        print("Email sent successfully.\n")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    # Step 1: Get the filename
    filename = input("Enter the filename to open or create: ")
    
    # Step 2: Open and read the file
    content = open_file(filename)
    print("Current Content:\n" + content)
    
    # Step 3: Edit the content
    print("Type your new content below. Type 'SAVE' on a new line to save and exit.")
    lines = []
    while True:
        line = input()
        if line.strip().upper() == "SAVE":
            break
        lines.append(line)
    
    new_content = "\n".join(lines)
    write_file(filename, new_content)

    # Step 4: Option to Send Email
    send_email_option = input("Would you like to send this content via email? (yes/no): ").strip().lower()
    if send_email_option == 'yes':
        sender_email = input("Enter your email: ")
        app_password = input("Enter your email app password: ")
        recipient_email = input("Enter the recipient's email: ")
        subject = input("Enter the email subject: ")
        
        send_email(sender_email, app_password, recipient_email, subject, new_content)

if __name__ == "__main__":
    main()
