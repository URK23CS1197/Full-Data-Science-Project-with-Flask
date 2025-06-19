
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
import joblib


df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')
df = df.dropna(subset=['age', 'fare', 'sex', 'embarked'])

X = df[['age', 'fare', 'sex', 'embarked']]
y = df['survived']

numeric_features = ['age', 'fare']
categorical_features = ['sex', 'embarked']

preprocessor = ColumnTransformer([
    ('num', StandardScaler(), numeric_features),
    ('cat', OneHotEncoder(), categorical_features)
])

pipeline = Pipeline([
    ('preprocess', preprocessor),
    ('classifier', LogisticRegression())
])

pipeline.fit(X, y)
joblib.dump(pipeline, 'titanic_model.pkl')
