import os
from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS
from your_email_module import send_email, read_config  # Import your email functions

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Ensure the uploads directory exists
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/send-cv', methods=['POST'])
def send_cv():
    try:
        subject = request.form['subject']
        body = request.form['body']
        recipient_emails = request.form['recipient-emails'].splitlines()
        cv_file = request.files['cv-file']

        # Save the file temporarily
        cv_path = os.path.join('uploads', cv_file.filename)
        cv_file.save(cv_path)

        # Read email configuration
        email_config = read_config()

        # Send the email
        for recipient in recipient_emails:
            send_email(subject, body, recipient, cv_path, 
                       email_config['sender_email'], 
                       email_config['sender_password'], 
                       email_config['smtp_server'], 
                       int(email_config['smtp_port']))
        
        # Remove the temporary file
        os.remove(cv_path)
        
        return jsonify({'status': 'success', 'message': 'Emails sent successfully'})
    
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
