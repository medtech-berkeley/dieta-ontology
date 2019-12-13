import operator
import requests

USER_KEY = "zxYm6ZIca0tAevWXz3SJLofbkBc5wughcvoiuUKQ"
USDA_URL = "https://api.nal.usda.gov/fdc/v1/search?api_key=" + USER_KEY
HEADERS = {"Content-Type":"application/json"}

def search_usda(food):
    data = '{"generalSearchInput":"' + food + '"}'
    response = requests.post(USDA_URL, headers=HEADERS, data=data)

    return response

def get_ingredients(usda_response):
    brands = usda_response.json()["foods"]

    all_brand_ingredients = []

    for brand in brands:
        if "ingredients" in brand:
            all_brand_ingredients.append(brand["ingredients"].split(','))

    return all_brand_ingredients

def ingredient_totals(all_brand_ingredients):
    all_ingredients = {}

    for brand in all_brand_ingredients:
        for ingredient in brand:
            if ingredient[0] == ' ':
                ingredient = ingredient[1:]
            if ingredient[-1] in ' .)':
                ingredient = ingredient[:-1]
            if ingredient not in all_ingredients:
                all_ingredients[ingredient] = 0

    for brand in all_brand_ingredients:
        for ingredient in brand:
            for key in all_ingredients:
                if key in ingredient:
                    all_ingredients[key] += 1

    return all_ingredients

def ingredient_frequencies(all_ingredients):
    ingredient_confidences = []
    max_freq = 0

    for key in all_ingredients:
        if all_ingredients[key] != 1:
            max_freq = max(max_freq, all_ingredients[key])
            ingredient_confidences.append([key, all_ingredients[key]])

    for ingredient in ingredient_confidences:
        ingredient[1] = (ingredient[1] / max_freq) * 100

    ingredient_confidences.sort(key=operator.itemgetter(1), reverse=True)

    print("likely ingredients:")

    for ingredient, relative_frequency in ingredient_confidences:
        print(ingredient, "with a confidence of",
              relative_frequency, "%")
