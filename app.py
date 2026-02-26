# app.py
import os
from pymongo import MongoClient
from flask import Flask, render_template, request, jsonify

# ------------------------------
# MongoDB connection (safe)
# ------------------------------
mongo_uri = os.environ.get("MONGO_URI")  # set this in terminal/session
if not mongo_uri:
    raise ValueError("MONGO_URI not set. Please set environment variable.")

client = MongoClient(mongo_uri)
db = client['house_price_db']  # replace with your DB name

# ------------------------------
# Flask app setup
# ------------------------------
app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('index.html')

# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Try JSON first
        if request.is_json:
            data = request.get_json()
        else:
            # Fallback to form data
            data = request.form.to_dict()

        if not data:
            return jsonify({"error": "No valid data provided"}), 400

        # Example ML prediction (replace with your model)
        predicted_values = [1, 2, 3, 4, 5, 6]  # placeholder

        # Always return valid JSON
        return jsonify({
            "prediction": predicted_values
        })

    except Exception as e:
        # Catch unexpected errors
        return jsonify({"error": "Server error", "details": str(e)}), 500

# Run the app
if __name__ == '__main__':
    app.run(debug=True)