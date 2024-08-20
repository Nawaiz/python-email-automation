import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
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

        # Attach the image
        # with open(image_path, 'rb') as img_file:
        #     img = MIMEImage(img_file.read())
        #     img.add_header('Content-ID', '<thumbnail>')
        #     msg.attach(img)

        # Setup the SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()

        print(f"Email sent to {receiver_email}")

    except Exception as e:
        print(f"Failed to send email to {receiver_email}. Error: {e}")

# Main function to read emails from CSV and send the message
def main():
    sender_email = "pronawaiz1@gmail.com"
    sender_password = " " # <--- write here app password created of gmail
    subject = "Thumbnail Designer"
    body = '''
    <html>
    <body>
        <p>Hey, It's <b>Premium and Affordable Thumbnail Designing Offer</b> to the Creators who are finding high quality thumbnails.<br>
        <br>
        
        I will Transform Your Channel By Editing and redesigning <b><mark>Eye-Catching THUMBNAILS</mark></b><br>
        <br>
        I will make your <mark><b>1st 1 Thumbnail For Free</b> </mark>. After that If you like my Work You can Hire me on your long term goals.<br>
        <br>
        As you know, If your videos Have <b><mark>Engaging Thumbnails</mark></b> viewers will click on it and increase Click-through rate.<br>
        <br>
        Investing in High Quality Thumbnail will Increase your views and Subscriber.<br>
        <br>
        I have over <b>2 Years of Experience</b> in Graphic Designing and Youtube Thumbnails designing. <br>
        <br>
        I would love to Discuss how I can  help to enhance your channel visuals. Please Reply to this email. <br>
        <br>
        <br>
        <b><mark>PREMIUM OFFER</b><mark>
        <ul>
        <li> Rate Will be <mark><b>AFFORDABLE</b></mark> so don't worry</li>
        </ul>
        Best Regards,
        Nawaiz Ahmad <br>
        Cell No Or Whatsapp: <a href="tel:+923132295918">+923132295918</a><br>
        My Portfolio: <a href="https://pronawaiz.wixsite.com/my-site">Portfolio</a> <br>
        Instagram: <a href="https://www.instagram.com/nawaizahmad2021/">Nawaiz Ahmad</a>
        <br>
       Thanks for Checking my <b>Email</b>.<br>
        </p>
    </body>
    </html>
    '''
  

    try:
        # Read the list of recipient emails from CSV file with specified encoding
        email_list = pd.read_csv('email.csv', encoding='UTF-8')

        for index, row in email_list.iterrows():
            receiver_email = row['email']
            send_email(sender_email, sender_password, receiver_email, subject, body)

    except FileNotFoundError:
        print("The file 'email.csv' was not found.")
    except pd.errors.EmptyDataError:
        print("The file 'email.csv' is empty.")
    except pd.errors.ParserError:
        print("Error parsing the file 'email2.csv'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
