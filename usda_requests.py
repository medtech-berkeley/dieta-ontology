import requests, operator

user_key = "zxYm6ZIca0tAevWXz3SJLofbkBc5wughcvoiuUKQ"
url = "https://api.nal.usda.gov/fdc/v1/search?api_key=" + user_key

headers = {"Content-Type":"application/json"}

food_input = input("Food input: ")

data = '{"generalSearchInput":"' + food_input + '"}'

response = requests.post(url, headers=headers, data=data)
brands = response.json()["foods"]

ingredients = []

for brand in brands:
    if "ingredients" in brand:
        ingredients.append(brand["ingredients"].split(','))

length = len(ingredients)
all_ingredients = {}
for x in ingredients:
    for ingredient in x:
        if ingredient[0] == ' ':
            ingredient = ingredient[1:]
        if ingredient[-1] in ' .)':
            ingredient = ingredient[:-1]
        if ingredient not in all_ingredients:
            all_ingredients[ingredient] = 0

for x in ingredients:
    for ingredient in x:
        for key in all_ingredients:
            if key in ingredient:
                all_ingredients[key] += 1

confidence = []
max_freq = 0
for key in all_ingredients.keys():
    if all_ingredients[key] != 1:
        max_freq = max(max_freq, all_ingredients[key])
        confidence.append([key, all_ingredients[key]])

for l in confidence:
    l[1] = (l[1] / max_freq) * 100

confidence.sort(key=operator.itemgetter(1), reverse=True)
print("likely ingredients:")
for x in range(len(confidence)):
    print(confidence[x][0], "with a confidence of", confidence[x][1], "%")
