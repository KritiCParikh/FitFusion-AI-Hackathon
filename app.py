# import gradio as gr
# import os
# from datetime import datetime
# from utils.model_manager import ModelManager
# from utils.emotion_detect import EmotionDetector
# from utils.workout_reference import WorkoutReference

# import gradio as gr
# from dotenv import load_dotenv
# import requests

# from config import PROMPT_TEMPLATES
# import logging

# # Set up logging
# logging.basicConfig(level=logging.INFO)
# logger = logging.getLogger(__name__)

# # Dietary options
# DIETARY_OPTIONS = [
#     "Standard",
#     "Vegetarian",
#     "Vegan",
#     "Pescatarian",
#     "Gluten-Free",
#     "Dairy-Free",
#     "Low-Carb",
#     "Keto",
#     "Paleo",
#     "Mediterranean",
#     "Low-Fat",
#     "High-Protein"
# ]

# # Mood examples
# MOOD_EXAMPLES = [
#     "I'm feeling energetic and ready to push myself today!",
#     "A bit tired but motivated to get moving",
#     "Stressed from work, need something relaxing",
#     "Feeling great and looking for a challenge",
#     "A bit down, could use some uplifting movement",
#     "Super excited to try something new!",
#     "Feeling anxious, need to clear my mind",
#     "Tired but want to stay active",
#     "Feeling strong and confident today",
#     "Need a gentle workout to unwind"
# ]

# # Initialize models and services
# try:
#     model_manager = ModelManager()
#     emotion_detector = EmotionDetector()
#     workout_reference = WorkoutReference()
#     logger.info("Models and services initialized successfully")
# except Exception as e:
#     logger.error(f"Failed to initialize models: {str(e)}")
#     raise

# def generate_meal_plan(time, budget, diet, mood):
#     try:
#         logger.info(f"Generating meal plan for time={time}, budget={budget}, diet={diet}, mood={mood}")
#         prompt = model_manager.format_prompt(
#             PROMPT_TEMPLATES["meal_plan"],
#             time=time,
#             budget=budget,
#             diet=diet,
#             mood=mood
#         )
#         return model_manager.generate_text(prompt)
#     except Exception as e:
#         logger.error(f"Error generating meal plan: {str(e)}")
#         return f"Error generating meal plan: {str(e)}"

# def generate_workout_plan(time, mood):
#     try:
#         logger.info(f"Generating workout plan for time={time}, mood={mood}")
#         # Calculate main workout time (total time minus warm-up and cool-down)
#         main_workout_time = max(time - 20, 10)  # Ensure at least 10 minutes for main workout
        
#         prompt = model_manager.format_prompt(
#             PROMPT_TEMPLATES["workout"],
#             time=time,
#             main_workout_time=main_workout_time,
#             mood=mood
#         )
#         workout_plan = model_manager.generate_text(prompt)
        
#         # Extract exercise names and get references
#         exercises = extract_exercises(workout_plan)
#         references = {}
#         for exercise in exercises:
#             refs = workout_reference.get_exercise_references(exercise)
#             if refs:
#                 references[exercise] = refs
        
#         return workout_plan, references
#     except Exception as e:
#         logger.error(f"Error generating workout plan: {str(e)}")
#         return f"Error generating workout plan: {str(e)}", {}

# def extract_exercises(workout_plan):
#     # Simple exercise extraction - can be improved
#     exercises = []
#     for line in workout_plan.split('\n'):
#         if any(word in line.lower() for word in ['squat', 'push-up', 'lunge', 'plank', 'crunch', 'jump']):
#             exercises.append(line.strip())
#     return exercises[:3]  # Return top 3 exercises

# def detect_emotion(text):
#     try:
#         logger.info(f"Detecting emotion for text: {text}")
#         emotion_result = emotion_detector.detect_emotion(text)
#         garden_element = emotion_detector.get_garden_element(emotion_result['emotion'])
#         return f"{garden_element} {emotion_result['emotion']} (Confidence: {emotion_result['confidence']:.2f})"
#     except Exception as e:
#         logger.error(f"Error detecting emotion: {str(e)}")
#         return f"Error detecting emotion: {str(e)}"

# def create_daily_wellness_planner():
#     with gr.Blocks() as planner:
#         gr.Markdown("# Daily Wellness Planner")
#         with gr.Row():
#             with gr.Column():
#                 time_input = gr.Slider(minimum=15, maximum=120, value=30, label="Time Available (minutes)")
#                 budget_input = gr.Slider(minimum=10, maximum=100, value=30, label="Budget ($)")
#                 diet_input = gr.Dropdown(
#                     choices=DIETARY_OPTIONS,
#                     value="Standard",
#                     label="Dietary Preferences",
#                     info="Select your dietary preference"
#                 )
                
#                 # Mood input with examples
#                 with gr.Group():
#                     mood_input = gr.Textbox(
#                         label="How are you feeling today?",
#                         placeholder="Describe your current mood...",
#                         info="You can use the examples below or write your own feelings"
#                     )
#                     gr.Examples(
#                         examples=MOOD_EXAMPLES,
#                         inputs=mood_input,
#                         label="Example Moods",
#                         examples_per_page=5
#                     )
                
#                 generate_btn = gr.Button("Generate Plan")
            
#             with gr.Column():
#                 meal_output = gr.Textbox(label="Meal Plan")
#                 workout_output = gr.Textbox(label="Workout Plan")
#                 emotion_output = gr.Textbox(label="Emotion Analysis")
#                 references_output = gr.JSON(label="Exercise References")
        
#         generate_btn.click(
#             fn=lambda t, b, d, m: (
#                 generate_meal_plan(t, b, d, m),
#                 *generate_workout_plan(t, m),
#                 detect_emotion(m)
#             ),
#             inputs=[time_input, budget_input, diet_input, mood_input],
#             outputs=[meal_output, workout_output, references_output, emotion_output]
#         )
#     return planner

# def create_emotion_garden():
#     with gr.Blocks() as garden:
#         gr.Markdown("# Emotion Garden")
#         with gr.Row():
#             with gr.Column():
#                 mood_check = gr.Textbox(
#                     label="How are you feeling?",
#                     placeholder="Describe your current mood...",
#                     info="You can use the examples below or write your own feelings"
#                 )
#                 gr.Examples(
#                     examples=MOOD_EXAMPLES,
#                     inputs=mood_check,
#                     label="Example Moods",
#                     examples_per_page=5
#                 )
#                 check_btn = gr.Button("Check Mood")
#             garden_display = gr.Textbox(label="Your Garden")
        
#         check_btn.click(
#             fn=detect_emotion,
#             inputs=[mood_check],
#             outputs=[garden_display]
#         )
#     return garden

# def main():
#     with gr.Blocks(title="FitFusion AI", analytics_enabled=False) as app:
#         gr.Markdown("# 🏋️‍♂️ FitFusion AI - Your Personal Wellness Companion")
        
#         with gr.Tabs():
#             with gr.TabItem("Daily Wellness Planner"):
#                 create_daily_wellness_planner()
            
#             with gr.TabItem("Emotion Garden"):
#                 create_emotion_garden()
                
                
    
#     app.launch(share=False, server_name="0.0.0.0")

# if __name__ == "__main__":
#     main() 


import gradio as gr
import os
from datetime import datetime
from utils.model_manager import ModelManager
from utils.emotion_detect import EmotionDetector
from utils.workout_reference import WorkoutReference

from dotenv import load_dotenv
import requests

from config import PROMPT_TEMPLATES
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Load API key from .env
load_dotenv()
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

# Dietary options
DIETARY_OPTIONS = [
    "Standard", "Vegetarian", "Vegan", "Pescatarian", "Gluten-Free",
    "Dairy-Free", "Low-Carb", "Keto", "Paleo", "Mediterranean",
    "Low-Fat", "High-Protein"
]

# Mood examples
MOOD_EXAMPLES = [
    "I'm feeling energetic and ready to push myself today!",
    "A bit tired but motivated to get moving",
    "Stressed from work, need something relaxing",
    "Feeling great and looking for a challenge",
    "A bit down, could use some uplifting movement",
    "Super excited to try something new!",
    "Feeling anxious, need to clear my mind",
    "Tired but want to stay active",
    "Feeling strong and confident today",
    "Need a gentle workout to unwind"
]

# Initialize models and services
try:
    model_manager = ModelManager()
    emotion_detector = EmotionDetector()
    workout_reference = WorkoutReference()
    logger.info("Models and services initialized successfully")
except Exception as e:
    logger.error(f"Failed to initialize models: {str(e)}")
    raise

# Tavily functions
def tavily_search(query):
    url = "https://api.tavily.com/search"
    headers = {"Content-Type": "application/json"}
    payload = {
        "api_key": TAVILY_API_KEY,
        "query": query,
        "include_images": True,
        "include_answer": True
    }
    response = requests.post(url, json=payload, headers=headers)
    return response.json()

# def chatbot_response(user_message):
#     data = tavily_search(user_message)
#     answer = data.get("answer", "I couldn't find anything.")
#     top_result = data.get("results", [{}])[0]
#     image_links = data.get("images", [])[:2]

#     reply = f"\U0001F4AC **Answer**: {answer}\n\n"
#     reply += f"\U0001F517 **Top Link**: [{top_result.get('title')}]({top_result.get('url')})\n\n"
#     for i, img_url in enumerate(image_links):
#         reply += f"\U0001F5BC️ Image {i+1}: {img_url}\n"

#     return reply

def chatbot_response(user_message):
    data = tavily_search(user_message)
    
    answer = data.get("answer", "Sorry, I couldn’t find a good answer.")
    top_result = data.get("results", [{}])[0]
    title = top_result.get("title", "See more info")
    url = top_result.get("url", "")
    image_links = data.get("images", [])
    
    # Create a nicer response with formatting
    response = f"**🧠 Assistant:** {answer}\n\n"
    if url:
        response += f"🔗 [More Info - {title}]({url})\n\n"
    
    if image_links:
        response += f"![image]({image_links[0]})\n\n"

    return response

def generate_meal_plan(time, budget, diet, mood):
    try:
        logger.info(f"Generating meal plan for time={time}, budget={budget}, diet={diet}, mood={mood}")
        prompt = model_manager.format_prompt(
            PROMPT_TEMPLATES["meal_plan"],
            time=time,
            budget=budget,
            diet=diet,
            mood=mood
        )
        return model_manager.generate_text(prompt)
    except Exception as e:
        logger.error(f"Error generating meal plan: {str(e)}")
        return f"Error generating meal plan: {str(e)}"

def generate_workout_plan(time, mood):
    try:
        logger.info(f"Generating workout plan for time={time}, mood={mood}")
        main_workout_time = max(time - 20, 10)
        prompt = model_manager.format_prompt(
            PROMPT_TEMPLATES["workout"],
            time=time,
            main_workout_time=main_workout_time,
            mood=mood
        )
        workout_plan = model_manager.generate_text(prompt)
        return workout_plan
    except Exception as e:
        logger.error(f"Error generating workout plan: {str(e)}")
        return f"Error generating workout plan: {str(e)}"

def detect_emotion(text):
    try:
        logger.info(f"Detecting emotion for text: {text}")
        emotion_result = emotion_detector.detect_emotion(text)
        garden_element = emotion_detector.get_garden_element(emotion_result['emotion'])
        return f"{garden_element} {emotion_result['emotion']} (Confidence: {emotion_result['confidence']:.2f})"
    except Exception as e:
        logger.error(f"Error detecting emotion: {str(e)}")
        return f"Error detecting emotion: {str(e)}"

def create_daily_wellness_planner():
    with gr.Blocks() as planner:
        gr.Markdown("# Daily Wellness Planner")
        with gr.Row():
            with gr.Column():
                time_input = gr.Slider(minimum=15, maximum=120, value=30, label="Time Available (minutes)")
                budget_input = gr.Slider(minimum=10, maximum=100, value=30, label="Budget ($)")
                diet_input = gr.Dropdown(
                    choices=DIETARY_OPTIONS,
                    value="Standard",
                    label="Dietary Preferences",
                    info="Select your dietary preference"
                )
                with gr.Group():
                    mood_input = gr.Textbox(
                        label="How are you feeling today?",
                        placeholder="Describe your current mood...",
                        info="You can use the examples below or write your own feelings"
                    )
                    gr.Examples(
                        examples=MOOD_EXAMPLES,
                        inputs=mood_input,
                        label="Example Moods",
                        examples_per_page=5
                    )
                generate_btn = gr.Button("Generate Plan")
            with gr.Column():
                meal_output = gr.Textbox(label="Meal Plan")
                workout_output = gr.Textbox(label="Workout Plan")
                emotion_output = gr.Textbox(label="Emotion Analysis")
                gr.Image(value="image.jpg", label="Wellness Inspiration", show_label=True)
        generate_btn.click(
            fn=lambda t, b, d, m: (
                generate_meal_plan(t, b, d, m),
                generate_workout_plan(t, m),
                detect_emotion(m)
            ),
            inputs=[time_input, budget_input, diet_input, mood_input],
            outputs=[meal_output, workout_output, emotion_output]
        )

        # Tavily chatbot assistant below the main planner
        with gr.Accordion("\U0001F30D Smart Web Assistant", open=True):
            gr.Markdown("Ask for gyms nearby, food suggestions, or wellness tips from the web.")
            chat_input = gr.Textbox(label="Your Question")
            chat_button = gr.Button("Search")
            chat_output = gr.Markdown()
            chat_button.click(fn=chatbot_response, inputs=chat_input, outputs=chat_output)
    return planner

def create_emotion_garden():
    with gr.Blocks() as garden:
        gr.Markdown("# Emotion Garden")
        with gr.Row():
            with gr.Column():
                mood_check = gr.Textbox(
                    label="How are you feeling?",
                    placeholder="Describe your current mood...",
                    info="You can use the examples below or write your own feelings"
                )
                gr.Examples(
                    examples=MOOD_EXAMPLES,
                    inputs=mood_check,
                    label="Example Moods",
                    examples_per_page=5
                )
                check_btn = gr.Button("Check Mood")
            garden_display = gr.Textbox(label="Your Garden")
        check_btn.click(
            fn=detect_emotion,
            inputs=[mood_check],
            outputs=[garden_display]
        )
    return garden

def main():
    with gr.Blocks(title="FitFusion AI", analytics_enabled=False) as app:
        gr.Markdown("# \U0001F3CB️‍♂️ FitFusion AI - Your Personal Wellness Companion")
        with gr.Tabs():
            with gr.TabItem("Daily Wellness Planner"):
                create_daily_wellness_planner()
            with gr.TabItem("Emotion Garden"):
                create_emotion_garden()
    app.launch(share=False, server_name="0.0.0.0")

if __name__ == "__main__":
    main()