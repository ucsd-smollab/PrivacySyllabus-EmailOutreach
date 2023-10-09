# Privacy Syllabus Project - Email Outreach Repository

This repository is part of the Privacy Syllabus Project. The goal of this repository is to gather syllabuses and related information for the study of privacy integration in university curricula.

## Contents

This repository contains three essential files:

### 1. `utils.py`

`utils.py` includes utility functions and constants used in the email outreach process. These functions handle various tasks, such as checking the validity of fields, constructing email subjects and bodies, and more. 

### 2. `constants.py`

`constants.py` defines constants, email templates, and subject lines used in the outreach emails. It centralizes the content of these emails for easy maintenance and customization.

### 3. `send_email_to_profs.py`

`send_email_to_profs.py` is the main script responsible for sending outreach emails to professors. It reads data from a CSV file (`Syllabus_Response.csv`), constructs emails based on the provided templates, and sends them via Gmail using Google API credentials. It also logs sent email IDs in a CSV file (`Sent_Email_History.csv`) to avoid duplicate outreach.

## Getting Started

To use this repository and perform email outreach to professors, follow these steps:

1. Clone this repository to your local machine.
2. Ensure you have the necessary Gmail API credentials (`credentials.json`) and configure them according to Google's API setup instructions.
3. Prepare your data in a CSV file named `Universities_with_Privacy_Content_And_Prof_Email.csv`. The CSV should include columns for instructor names, universities, instructor emails, and any additional information required for outreach.
4. Customize the email templates and subjects in `constants.py` to match your outreach goals.
5. Run the `send_email_to_profs.py` script to initiate the email outreach process. Ensure you have an active internet connection, and Google API permissions are correctly set up.

Please exercise caution and adhere to ethical guidelines when conducting email outreach. Be respectful of professors' responses and privacy.

## Contributors

- Kristen Vaccaro
- Aishwarya Manjunath

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

