# findTheFish
a project for finding phishing websites using ML on IBM Cloud

# Phishing Website Detection using ML on IBM Cloud

This project aims to detect phishing websites using machine learning techniques on IBM Cloud. It includes a Flask web application and a command-line interface (CLI) application that make API calls to a trained model hosted on IBM Cloud. The project utilizes IBM Auto AI and the scikit-learn library to analyze and benchmark various machine learning algorithms for phishing URL detection.

## Features

- Flask web app: Provides a user-friendly interface for entering URLs and receiving predictions on whether they are phishing websites.
- CLI application: Allows users to make API calls to the trained model via the command line, providing predictions on the input URLs.
- Machine learning model: Trained using IBM Auto AI and scikit-learn, the model predicts whether a given URL is a phishing website.
- IBM Cloud deployment: The trained model is hosted on IBM Cloud, providing API endpoints for the web app and CLI application to interact with.

## Installation

1. Clone the repository:
git clone https://github.com/your-username/phishing-detection.git
cd phishing-detection


2. Install the required dependencies:
pip install -r requirements.txt


3. Configure the IBM Cloud credentials:
- Sign up for an IBM Cloud account (if you don't have one already).
- Create an instance of the Watson Machine Learning service.
- Retrieve the API key and endpoint URL for your Watson Machine Learning instance.
- Update the `config.ini` file with your credentials.

4. Run the Flask web app:
python app.py


5. Access the web app:
Open your browser and visit `http://localhost:5000`.

## Usage

### Web App

- Open the web app in your browser.
- Enter a URL in the provided input field.
- Click the "Predict" button to receive the prediction result.

### CLI Application

- Open a terminal.
- Run the CLI application with the following command:
python cli.py --url <url>
