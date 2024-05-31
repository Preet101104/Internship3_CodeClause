import pandas as pd
import numpy as np
import pickle
from flask import Flask, render_template, request
from sklearn.cluster import KMeans

# Load the clustering model
with open('clustering_model.pkl', 'rb') as file:
    clustering_model = pickle.load(file)

# Initialize Flask app
app = Flask(__name__)

# Define the input page
@app.route('/')
def input_page():
    return render_template('input.html')

# Define the prediction page
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input data from the form
    age = float(request.form['age'])
    income = float(request.form['income'])
    purchase_history = float(request.form['purchase_history'])

    # Create a dataframe with the input data
    input_data = pd.DataFrame([[age, income, purchase_history]], columns=['age', 'income', 'purchase_history'])

    # Apply the clustering model to the input data
    segment = clustering_model.predict(input_data)

    # Display the predicted segment
    return render_template('prediction.html', segment=segment[0])

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
