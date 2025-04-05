# FitFusion-AI-Hackathon

## 🧩 Problem Statement
Modern individuals face decision fatigue around maintaining health—balancing diet, workouts, and emotional well-being. The challenge is creating a unified, personalized wellness assistant that tailors meal and fitness plans and understands user emotions to provide holistic care all in real time. FitFusion AI is an interactive AI-powered web app that generates personalized **meal plans**, **workout routines**, and **emotional insights** based on how you're feeling, how much time you have, and your dietary preferences. It also features a real-time chatbot powered by the **Tavily API** to offer live web results for wellness queries.


## 🤖 Models Used

- **Text Generation**: `google/flan-t5-base`  
- **Emotion Detection**: `j-hartmann/emotion-english-distilroberta-base`  
- **Optional (Tested Separately)**: `mistralai/Mistral-7B-Instruct-v0.2` for large-scale instruction tuning

--

## 💡 Features

- 🍽️ **Meal Plan Generator**  
  Personalized meals based on mood, time, budget, and dietary preference.

- 🏋️‍♂️ **Workout Plan Generator**  
  Adaptive exercise routines based on emotional state and available time.

- 🌸 **Emotion Garden**  
  Detects emotion from mood descriptions and visualizes it symbolically.

- 🔍 **Web Wellness Assistant**  
  Get real-time search results, answers, and images via Tavily's smart API.

---

## 🤖 Models Used

- **Text Generation**:  
  [`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base) – for meal and workout plan generation

- **Emotion Detection**:  
  [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) – classifies emotional tone from user text

- **Optional Test Model**:  
  [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) – tested for advanced instruction-following (in `test_mistral.py`)



