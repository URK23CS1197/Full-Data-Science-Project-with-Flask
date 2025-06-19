
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('titanic_model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({'Survived': bool(prediction)})
from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)  
@app.route('/')
def home():
    return "Titanic Survival Prediction API is running."


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    input_df = pd.DataFrame([data])
    model = joblib.load("titanic_model.pkl")
    prediction = model.predict(input_df)[0]
    return jsonify({'Survived': bool(prediction)})

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    app.run(debug=True)
