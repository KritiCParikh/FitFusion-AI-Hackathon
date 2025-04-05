import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# API Keys
HUGGINGFACE_API_KEY = os.getenv("HUGGINGFACE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Model Configurations
MODEL_CONFIG = {
    "text_generation": {
        "model_name": "google/flan-t5-base",
        "max_length": 1024,
        "temperature": 0.9,
        "top_k": 50,
        "top_p": 0.95,
        "repetition_penalty": 1.2,
    },
    "emotion_detection": {
        "model_name": "j-hartmann/emotion-english-distilroberta-base",
        "return_all_scores": True,
    }
}

# Prompt Templates
PROMPT_TEMPLATES = {
    "meal_plan": "prompts/meal_prompt.txt",
    "workout": "prompts/workout_prompt.txt",
} 