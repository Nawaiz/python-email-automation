import customtkinter as ctk
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Function to send email
def send_email(sender_email, sender_password, receiver_email, subject, body):
    try:
        # Create the email header
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = receiver_email
        msg['Subject'] = subject

        # Attach the body with HTML content
        msg.attach(MIMEText(body, 'html'))

        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print(f"Email sent to {receiver_email}")
        return True

    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")
        return False

# Main function to read emails from CSV and send the message
def send_bulk_emails(sender_email, sender_password, subject, body, csv_file_path):
    try:
        # Read the list of recipient emails from CSV file with specified encoding
        email_list = pd.read_csv(csv_file_path, encoding='UTF-8')

        for index, row in email_list.iterrows():
            receiver_email = row['email']
            if not send_email(sender_email, sender_password, receiver_email, subject, body):
                break

    except FileNotFoundError:
        print("The file was not found.")
    except pd.errors.EmptyDataError:
        print("The file is empty.")
    except pd.errors.ParserError:
        print("Error parsing the file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# GUI setup
def main():
    def on_send_button_click():
        sender_email = entry_sender_email.get()
        sender_password = entry_sender_password.get()
        subject = entry_subject.get()
        body = text_body.get("1.0", ctk.END)
        csv_file_path = entry_csv_file_path.get()

        send_bulk_emails(sender_email, sender_password, subject, body, csv_file_path)

    app = ctk.CTk()
    app.title("Bulk Email Sender")

    ctk.CTkLabel(app, text="Sender Email:").pack(padx=10, pady=5)
    entry_sender_email = ctk.CTkEntry(app, width=400)
    entry_sender_email.pack(padx=10, pady=5)

    ctk.CTkLabel(app, text="Sender Password:").pack(padx=10, pady=5)
    entry_sender_password = ctk.CTkEntry(app, width=400, show="*")
    entry_sender_password.pack(padx=10, pady=5)

    ctk.CTkLabel(app, text="Subject:").pack(padx=10, pady=5)
    entry_subject = ctk.CTkEntry(app, width=400)
    entry_subject.pack(padx=10, pady=5)

    ctk.CTkLabel(app, text="Body:").pack(padx=10, pady=5)
    text_body = ctk.CTkTextbox(app, width=400, height=200)
    text_body.pack(padx=10, pady=5)

    ctk.CTkLabel(app, text="CSV File Path:").pack(padx=10, pady=5)
    entry_csv_file_path = ctk.CTkEntry(app, width=400)
    entry_csv_file_path.pack(padx=10, pady=5)

    send_button = ctk.CTkButton(app, text="Send Emails", command=on_send_button_click)
    send_button.pack(padx=10, pady=20)

    app.mainloop()

if __name__ == "__main__":
    main()
