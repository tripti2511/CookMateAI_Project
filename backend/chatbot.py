# Import necessary libraries
from flask import Flask, request, jsonify
import pandas as pd
import random

# Initialize Flask app
app = Flask(__name__)

# Load recipes dataset (make sure you have recipes.csv in backend/)
# Columns: Dish, Ingredients, Time (minutes), Tips
recipes_df = pd.read_csv("recipes.csv")

# Function to find recipe by dish name
def get_recipe(dish_name):
    dish_name = dish_name.lower()
    matched = recipes_df[recipes_df['Dish'].str.lower() == dish_name]
    if not matched.empty:
        recipe = matched.iloc[0]
        return {
            "Dish": recipe['Dish'],
            "Ingredients": recipe['Ingredients'],
            "Time": recipe['Time'],
            "Tips": recipe['Tips']
        }
    else:
        return {"error": "Dish not found in database."}

# Basic AI chatbot logic
@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_message = data.get("message", "")
    
    if "recipe" in user_message.lower():
        # Extract dish name
        dish_name = user_message.lower().replace("recipe for", "").strip()
        response = get_recipe(dish_name)
    elif "time" in user_message.lower():
        dish_name = user_message.lower().replace("time for", "").strip()
        recipe = get_recipe(dish_name)
        response = {"Time": recipe.get("Time", "Dish not found")}
    else:
        # Default generic responses
        responses = [
            "I can help you with recipes, cooking time, and tips!",
            "Ask me about any dish and I'll give you the recipe and tips."
        ]
        response = {"message": random.choice(responses)}
    
    return jsonify(response)

# Run the app
if __name__ == "__main__":
    app.run(debug=True)
