from flask import Flask, render_template, request
#from phishing_detector import PhishingDetector
#import joblib

# Load the pre-trained model
#model = joblib.load('path/to/pretrained/model.pkl')

# Use the loaded model for prediction
#def make_prediction(url):
   # features = vectorizer.transform([url])  # Convert the URL into features using the vectorizer
    #prediction = model.predict(features)  # Make prediction using the loaded model
    #return prediction[0]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') 

def make_prediction(url):
    detector = PhishingDetector()
    prediction = detector.predict(url)
    return prediction

@app.route('/predict', methods=['POST'])
def predict():
    # Your prediction logic goes here
    # Retrieve the URL from the form data and perform the necessary processing
    url = request.form['url']

    # Make the prediction and obtain the result
    prediction = make_prediction(url)

    # Render the template with the prediction result
    return render_template('index.html', prediction=prediction)

