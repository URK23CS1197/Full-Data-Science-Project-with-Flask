import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "age": 22,
    "fare": 7.25,
    "sex": "male",
    "embarked": "S"
}

response = requests.post(url, json=data)
print(response.json())
