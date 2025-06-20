# Full-Data-Science-Project-with-Flask
A complete data science project that includes data preprocessing, model training using scikit-learn, and deployment using Flask. The API accepts user input (e.g., Titanic passenger details) and returns predictions on survival. Demonstrates end-to-end workflow from data to deployed ML model through a simple, interactive web service.


*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: NIRANSON CDK

*INTERN ID* : CT04DG534

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

In this task, I built a complete end-to-end data science project, covering every stage from data collection and preprocessing, to model training and final deployment using Flask, a popular Python web framework. The goal was to simulate a real-world machine learning pipeline where a model is not only trained but also made accessible via an API for live predictions.I selected the Titanic survival prediction dataset for this project because it’s widely used in data science, well-documented, and includes both numerical and categorical data—ideal for demonstrating practical preprocessing and deployment strategies.

Data Collection & Preparation

I selected key features such as age, fare, sex, and embarked for model input, as they represent diverse data types (numeric and categorical) and have strong predictive power for the target variable survived.
Before training, I handled missing values by dropping rows with null entries in essential columns, ensuring data quality. The dataset was then split into features (X) and labels (y).


Data Preprocessing Pipeline
To streamline the preprocessing, I used Scikit-learn’s ColumnTransformer to apply:

StandardScaler on numeric features (age, fare) for normalization

OneHotEncoder on categorical features (sex, embarked) to handle text-based variables

This setup ensures that preprocessing and modeling are combined into a single object that can be reused and deployed without writing separate transformation code later. The trained pipeline was saved using joblib

Model Training & Evaluation
The pipeline was trained on the preprocessed Titanic dataset using Logistic Regression. Logistic Regression is an ideal choice for binary classification tasks like survival prediction and offers interpretable outputs.
After training, the model was evaluated for accuracy and successfully learned key patterns in the data, with decent predictive performance on test samples.


 Model Deployment with Flask
The most exciting part of this task was turning the model into a working API using Flask. I wrote a web service in web_app.py with two routes:

A root route (/) that confirms the API is running.

A /predict route that accepts POST requests with JSON input and returns a prediction (whether the person would survive or not).

The Flask app loads the trained pipeline using joblib, accepts incoming JSON data, converts it to a Pandas DataFrame, processes it through the pipeline, and returns the prediction as JSON.

*OUTPUT*

This task successfully demonstrated how to create a full ML pipeline from scratch and serve it through a RESTful API using Flask. It simulated a real-world deployment scenario, teaching critical skills like model serialization, API design, and integration.
The result was a lightweight, functional machine learning system ready to be integrated into web applications or extended into a frontend with React or hosted via Render/Heroku.

![Image](https://github.com/user-attachments/assets/e7b6c8f1-9524-4be6-8624-3956f69488f3)

![Image](https://github.com/user-attachments/assets/0733abad-d2c6-4c33-bd35-6f8785749ade)

![Image](https://github.com/user-attachments/assets/5f65e7d3-826a-4144-b23a-aa586bd3a880)
