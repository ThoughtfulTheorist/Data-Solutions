This project sends a daily email report summarizing product data from a CSV file. The report includes the total available quantity, average pallet cost, and average product price.

## Getting Started

Follow these instructions to set up and run the project on your local machine.

### Prerequisites

Ensure you have the following software installed on your machine:
- Python 3.6 or higher
- `pandas` library
- `schedule` library

You can install the required Python libraries using the following command:

```bash
pip install pandas schedule
```

### Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/ThoughtfulTheorist/DailyEmailReporting
    cd daily-email-reporting
    ```

2. **Configure the script**:
    Open the `EmailReporting.py` file and update the email settings and file path with your information:
    ```python
    recipient_email = "recipient@example.com"
    sender_email = "sender@example.com"
    smtp_server = "smtp.yourdomain.com"
    smtp_port = 587
    smtp_user = "smtp_user"
    smtp_password = "smtp_password"
    file_path = r"C:\path\to\your\ProductData.csv"
    ```

### Running the Script

To run the script, execute the following command in your terminal:
```bash
python EmailReporting.py
```

The script is scheduled to run daily at 07:00 AM. You can change the schedule by modifying the time in the `schedule.every().day.at("07:00").do(job)` line in the script.

### Logging

The script uses basic logging to provide information about its execution. Log messages include details about email sending status and any errors encountered during CSV file processing.

### Terminating the Script

To stop the script, use `CTRL+C` twice in the terminal.

## License

This project is licensed under the Apache License 2.0. See the [LICENSE](LICENSE) file for more details.