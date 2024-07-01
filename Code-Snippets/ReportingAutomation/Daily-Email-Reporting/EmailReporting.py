import smtplib
import pandas as pd
import schedule
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Email settings
recipient_email = "recipient email"
sender_email = "Sender Email"
smtp_server = "mail.yourdomain.com"
smtp_port = 587
smtp_user = "Sender Email"
smtp_password = "Your Sender Email Password"
file_path = r"C:\Users\YourUserName\YourFilePath\DailyEmailReporting\ProductData.csv"

def send_email(subject, body, to_email):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.attach(MIMEText(body, 'plain'))
    
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        logging.info("Email sent successfully")
    except Exception as e:
        logging.error(f"Failed to send email: {e}")

def read_and_process_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        total_available_qty = df['AvailableQty'].sum()
        avg_pallet_cost = df['PalletCost'].mean()
        avg_price = df['Price'].mean()
        return total_available_qty, avg_pallet_cost, avg_price
    except Exception as e:
        logging.error(f"Failed to read/process CSV file: {e}")
        return None, None, None

def job():
    total_available_qty, avg_pallet_cost, avg_price = read_and_process_csv(file_path)
    if total_available_qty is not None:
        body = f"Here's your daily report:\n" + \
               f"Total available quantity: {total_available_qty}\n" + \
               f"Average pallet cost: ${avg_pallet_cost:.2f}\n" + \
               f"Average product price: ${avg_price:.2f}"
        send_email("Daily Product Report", body, recipient_email)

# Schedule the job every day at specified time -- Update to test
schedule.every().day.at("07:00").do(job)

# Loop to keep the script running -- In terminal, use CTRL+C twice to terminate the script
try:
    while True:
        schedule.run_pending()
        time.sleep(60)
        logging.info("Awaiting next scheduled send...")
except KeyboardInterrupt:
    logging.info("Script terminated by user.")
    exit()
