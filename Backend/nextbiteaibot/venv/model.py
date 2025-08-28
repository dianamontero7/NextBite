#  colab logic converted

import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


# model and data loading

embedding_model = SentenceTransformer('all-MiniLM-L6-v2')
model = genai.GenerativeModel('gemini-2.5-flash')

# loading and preprocessing recipe data 

recipes = pd.read_json("recipes.json")
recipes = recipes.dropna(subset=['ingredients', 'directions'])
recipes['ingredients'] = recipes['ingredients'].apply(lambda ings: [i.lower().strip() for i in ings])
recipes['ingredient_text'] = recipes['ingredients'].apply(lambda x: ', '.join(x))
recipes['directions'] = recipes['directions'].apply(lambda steps: ' '.join(steps))
recipes = recipes[recipes['categories'].apply(lambda cats: any('easy' in c.lower() or 'quick' in c.lower() for c in cats))]

# converts ingredient text to embeddings (numerical vector)

recipes['embedding'] = recipes['ingredient_text'].apply(lambda text: embedding_model.encode(text))

# finds similar recipes based on user ingredients

def find_similar_recipes(user_ingredients):
    user_text = ', '.join(user_ingredients).lower()

    # retrieve
    user_vector = embedding_model.encode(user_text)
    similarities = recipes['embedding'].apply(lambda vec: cosine_similarity([user_vector], [vec])[0][0])
    top_idxs = np.argsort(similarities)[-3:][::-1]
    return recipes.iloc[top_idxs][['title', 'ingredients', 'directions']]

# generates recipes with Gemini

def generate_recipe_gemini(ingredients, similar_recipes, conditions=None, meal_size=None, meal_type=None, servings=None, exclude=None):
    ingredient_text = ', '.join(ingredients)
    condition_lines = []
    if conditions:
        for cond in conditions:
            c = cond.lower()
            if c == 'vegetarian':
                condition_lines.append("Avoid all meat, poultry, and seafood.")
            elif c == 'vegan':
                condition_lines.append("Avoid meat, dairy, eggs, or animal products.")
            elif c == 'gluten-free':
                condition_lines.append("Avoid wheat, barley, rye, or anything with gluten.")
            elif c == 'dairy-free':
                condition_lines.append("Avoid all dairy ingredients.")
            elif c == 'kid-friendly':
                condition_lines.append("Keep the recipe fun, simple, and not spicy.")
            elif c == 'health-conscious':
                condition_lines.append("Use whole ingredients and healthy cooking methods.")

    if exclude:
        condition_lines.append(f"Exclude these ingredients: {', '.join(exclude)}.")

    
    if meal_size:
        condition_lines.append(f"Make the recipe portion size {meal_size.lower()}.")
    if meal_type:
        condition_lines.append(f"This should be a {meal_type.lower()} recipe.")
    if servings:
        condition_lines.append(f"Adjust ingredients for {servings} servings.")


    condition_text = "\n".join(condition_lines)

    # context
    context = ""
    for _, row in similar_recipes.iterrows():
        context += f"Title: {row['title']}\nIngredients: {', '.join(row['ingredients'])}\nDirections: {row['directions']}\n\n"

    # generate 
    prompt = (
        f"You are a helpful cooking assistant.\n"
        f"User has the ingredients: {ingredient_text}.\n"
        f"{condition_text}\n\n"
        f"Here are similar recipes:\n{context}\n"
        f"Create a NEW, fun, quick, beginner-friendly recipe with ingredients and step-by-step directions."
    )

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error: {str(e)}"