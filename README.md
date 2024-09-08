
# 📧 CV Automation Tool

This Python script simplifies the process of sending your CV to multiple email addresses. Designed specifically for job seekers, it automates the task of sending customized emails with attachments, allowing users to efficiently apply to various job positions without the repetitive hassle of manual email composition. Just configure your details once, and the tool takes care of the rest.

## 🚀 Features

- **Automated Email Sending**: Send your CV to multiple recipients in one go.
- **Customizable Email Body & Subject**: Easily modify the email content for each application.
- **Attachment Handling**: Automatically attach your CV or any file of your choice.
- **Configurable SMTP Settings**: Works with any email service that supports SMTP, including Gmail, Outlook, Yahoo, and more.
- **Error Handling**: Handles SMTP connection issues and provides detailed error messages for easier troubleshooting.

## 🛠️ Requirements

- Python 3.x
- Required libraries: 
  - `smtplib`
  - `email.mime`
  - `configparser`

Install the dependencies using the following command:

```bash
pip install -r requirements.txt
```

## ⚙️ Configuration

Before using the tool, you need to configure your email settings.

1. Create a `config.ini` file in the same directory as the script with the following structure:

   ```ini
   [EmailConfiguration]
   sender_email = your-email@example.com
   sender_password = your-email-password
   smtp_server = smtp.example.com
   smtp_port = 465
   ```

2. Replace `your-email@example.com` with your email address.
3. Replace `your-email-password` with your email password or app-specific password.
4. Set the correct `smtp_server` and `smtp_port` based on your email provider (Gmail, Outlook, etc.).

## 💻 Usage

1. **Edit the Script**: Open the script and customize the `subject` and `body` for the email. For example:

   ```python
   subject = "Application for [Job Title]"
   body = "Dear Hiring Manager,\n\nI am excited to apply for the [Job Title] position at [Company Name]..."
   ```

2. **CV Attachment**: Place your CV in the specified location, and make sure to update the `cv_path` in the script:

   ```python
   cv_path = "path/to/your/CV.pdf"
   ```

3. **Send Emails**: Add the list of recipient email addresses to the `recipient_emails` list in the script. You can include multiple addresses for bulk applications:

   ```python
   recipient_emails = ["hr@company1.com", "recruiter@company2.com"]
   ```

4. **Run the Script**: 

   Simply run the script using Python:

   ```bash
   python cv_automation.py
   ```

   The script will automatically send your CV to each email address in the list.

## ⚠️ Important Notes

- **Email Provider Limitations**: Some email providers (like Gmail) may have restrictions on how many emails you can send at once. Be aware of your provider's email sending limits to avoid being flagged as spam.
- **Password Security**: If you're using Gmail, you may need to create an App Password or enable "Less Secure Apps" to allow the script to work.

## 📝 Example

An example run of the script looks like this:

```bash
Email sent successfully to hr@company1.com
Email sent successfully to recruiter@company2.com
Emails sent successfully.
```

---

By using this tool, job seekers can save time and effort, focusing on what matters most—landing the next opportunity!
