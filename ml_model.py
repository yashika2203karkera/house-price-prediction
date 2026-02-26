from flask import Flask, render_template, request
from pymongo import MongoClient
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# -----------------------------
# Load and Train Model Once
# -----------------------------
client = MongoClient("mongodb://localhost:27017/")
db = client["house_price_db"]
collection = db["houses"]

data = list(collection.find())
df = pd.DataFrame(data)

if "_id" in df.columns:
    df.drop("_id", axis=1, inplace=True)

df = df[["bedrooms", "bathrooms", "sqft_lot", "price"]]
df = df.dropna()

X = df[["bedrooms", "bathrooms", "sqft_lot"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

# -----------------------------
# Routes
# -----------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():
    bedrooms = float(request.form["bedrooms"])
    bathrooms = float(request.form["bathrooms"])
    sqft_lot = float(request.form["sqft_lot"])

    user_data = pd.DataFrame([[bedrooms, bathrooms, sqft_lot]],
                             columns=["bedrooms", "bathrooms", "sqft_lot"])

    prediction = model.predict(user_data)

    return render_template("index.html",
                           prediction_text=f"Predicted House Price: {round(prediction[0], 2)}")


if __name__ == "__main__":
    app.run(debug=True)


# pip install flask pandas numpy scikit-learn
# python -m ensurepip --upgrade