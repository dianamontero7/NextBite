# NextBite.ai

NextBite is an AI-driven application designed to help individuals transform leftover ingredients into creative recipes, aiming to reduce food waste. By leveraging Google's Gemini 2.5 Flash model, the platform generates personalized recipes based on user inputs. This model is a large language model optimized for understanding instructions and generating human-like text, making it perfect for recipe creation and natural language interactions.

The application exists to promote sustainability, help users cook creatively with what they have on hand, and make AI-assisted cooking accessible to everyone.

# Developers: Diana Montero & Joshua Moore

# Description of AI Model
Gemini 2.5 Flash, combined with embeddings and a Retrieval-Augmented Generation (RAG) system, allows NextBite to create smart, personalized recipes. The RAG system works like this: first, it finds recipes that are similar to your ingredients from the database using embeddings (which help the AI understand the meaning of the ingredients). Then, it feeds these similar recipes to Gemini, so the AI can generate a new, personalized recipe that makes sense with what you have and any dietary conditions.

# Installation Instructions - set up project locally 

## Clone the repository

- git clone https://github.com/dianamontero7/NextBite.git
- cd NextBite

## Set up the backend

- Navigate to the Backend/nextibiteaibot directory
- Create a virtual environment and activate it
   - python -m venv venv
   - source venv/bin/activate

- Install dependencies
   - pip install -r requirements.txt

- Run the backend server
   - uvicorn main:app --reload 

## Setup the frontend

- Navigate to the Frontend directory
- Install dependencies
   - npm install
- Start the frontend development server
   - npm run dev

# Usage Guide

- **User interaction:** Input available leftover ingredients and dietary preferences (optional)
- **Backend Processing:** Handles requests, finds similar recipes, and communicates with the Gemini AI model to generate new recipes
- **Frontend Display:** Shows AI-generated recipes in a clean, easy-to-read interface.
- **Database Storage:** Stores user interactions and generated recipes in MongoDB Atlas for future reference

# Features

- **AI-Powered Recipe Generation:** Uses Gemini 2.5 Flash to generate recipes from ingredients.
  
- **Smart Recipe Matching:** Converts ingredients, conditions, and existing recipes into embeddings using sentence transformers (all-MiniLM-L6-v2) to find similar recipes and provide context-aware AI suggestions.

- **Ingredient-Based Suggestions:** Provides recipes based on what users have at home.

- **Dietary Conditions Handling:** Accounts for user dietary restrictions.

- **User-Friendly Interface:** Clean, responsive frontend.

- **Database Integration:** Saves recipes and user inputs in MongoDB Atlas.

# Tech Stack

- **Frontend:** Vite + React, Bootstrap 

- **Backend:** FastAPI, Python

- **AI Model:** Google Gemini 2.5 Flash (for natural language recipe generation)

- **Database:** MongoDB Atlas 

- **Deployment:** TBA


