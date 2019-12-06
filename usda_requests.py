
import requests
headers = {"Content-Type":"application/json"}
data = '{"generalSearchInput":"Cheddar cheese"}'
url = "https://api.nal.usda.gov/fdc/v1/search?api_key=zxYm6ZIca0tAevWXz3SJLofbkBc5wughcvoiuUKQ"
response = requests.post(url, headers=headers, data=data)
response.json()