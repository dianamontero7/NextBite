# fastapi server

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from model import find_similar_recipes, generate_recipe_gemini
from db import recipes_collection
from datetime import datetime 

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# request data model 

class ChatRequest(BaseModel):
    ingredients: list
    conditions: list = []

# defining the POST endpoint 

@app.post("/chat")
async def get_recipe(data: ChatRequest):

    similar = find_similar_recipes(data.ingredients)
    ai_recipe = generate_recipe_gemini(data.ingredients, similar, data.conditions)

    # stores in mongodb

    recipe_doc = {
        "ingredients": data.ingredients,
        "conditions": data.conditions,
        "recipe": ai_recipe,
        "created_at": datetime.utcnow()
    }

    await recipes_collection.insert_one(recipe_doc)

    return {"recipe": ai_recipe}
