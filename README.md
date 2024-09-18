# CV Automation Tool

A Flask-based web application designed to automate the process of sending CVs (Curriculum Vitae) via email. This project simplifies the job application process by allowing users to send their CVs to multiple recipients effortlessly.

## Table of Contents

- [Project Description](#project-description)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Running the Application Locally](#running-the-application-locally)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Project Description

The CV Automation Tool is built using Flask and aims to streamline the job application process for users by enabling them to send their CVs directly from a web interface. It utilizes a Python email module to handle email sending functionalities, allowing for easy management of multiple recipients.

## Technologies Used

- **Python**: The programming language used to develop the application.
- **Flask**: A lightweight WSGI web application framework for Python.
- **SMTPLib**: A built-in Python module for sending emails.

## Installation

To get started with this project, ensure that you have Python and pip installed on your machine. Follow these steps to set up the project:

1. **Clone the repository:**
   bash
   git clone https://github.com/yourusername/cv-automation-tool.git
   cd cv-automation-tool
   

2. **Install Flask** (if not already installed):
   ```bash
   pip install Flask
  

3. **(Optional)** Create a `requirements.txt` file to manage dependencies:
   ```bash
   pip freeze > requirements.txt
   ```

## Running the Application Locally

To run the Flask application locally, follow these steps:

1. **Create your application files** if not already created:
   - `cv-automationScript.py`: The main Flask application file.
   - `your_email_module.py`: The module responsible for handling email functionalities.

2. **Open your terminal** and navigate to the directory where your files are located.

3. **Run the Flask application:**
   ```bash
   python cv-automationScript.py
   ```

4. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:5000/`. You can now use the application to send your CVs via email.

## Project Structure

cv-automation-tool/
│
├── cv-automationScript.py  # Main Flask application file
├── your_email_module.py     # Module for handling email functionalities
├── README.md                # Project documentation
└── requirements.txt         # (Optional) List of dependencies
```

## Contributing

Contributions are welcome! If you would like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push to your branch.
4. Create a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

```
