# FitFusion-AI-Hackathon

![FitFusion Hackathon](https://github.com/KritiCParikh/FitFusion-AI-Hackathon/blob/main/v1-Hackathon.png?raw=true)

## 🧩 Problem Statement

Modern individuals often face **decision fatigue** when trying to maintain their health — juggling diet, workouts, and emotional well-being. The challenge lies in creating a **unified, personalized wellness assistant** that not only tailors meal and fitness plans, but also understands emotional states to offer holistic care in real time.

**FitFusion AI** addresses this by providing an interactive, AI-powered web app that generates personalized **meal plans**, **workout routines**, and **emotional insights** based on how you're feeling, how much time you have, and your dietary preferences. 

It also features a built-in chatbot powered by the **Tavily API**, offering live web results to help users discover local resources and answer wellness-related questions.


## 🤖 Models Used

- **Text Generation**: `google/flan-t5-base`  
- **Emotion Detection**: `j-hartmann/emotion-english-distilroberta-base`  
- **Optional (Tested Separately)**: `mistralai/Mistral-7B-Instruct-v0.2` for large-scale instruction tuning

--

## What It Does

- 🍽️ **Meal Plan Generator**  
  Suggests meal ideas based on your mood, dietary preferences, time, and budget.

- 🏋️‍♂️ **Workout Plan Generator**  
  Recommends tailored workouts that suit your energy and mood.

- 🌿 **Emotion Garden**  
  Detects your current emotion and reflects it using symbolic visuals (e.g., 🌸 for joy, 🌧️ for sadness).  
  It also connects to a companion project where users grow a digital **AI-powered garden** based on their daily emotional check-ins.

  **Problem Solved:**  
  Many people don’t regularly check in with their mental or emotional state, or feel overwhelmed when they do.

  **Solution:**  
  Every time you describe how you feel, the AI:
  - Labels your emotion
  - Plants a flower, tree, or stone in your personal **Emotion Garden**
  - Optionally turns your mood into a piece of **poetry** or **music**

- 🔍 **Smart Wellness Chatbot**  
  Uses the **Tavily API** to provide helpful web articles, suggestions, and images in real time.


---

## 🤖 Models Used

- **Text Generation**:  
  [`google/flan-t5-base`](https://huggingface.co/google/flan-t5-base) – for meal and workout plan generation

- **Emotion Detection**:  
  [`j-hartmann/emotion-english-distilroberta-base`](https://huggingface.co/j-hartmann/emotion-english-distilroberta-base) – classifies emotional tone from user text

- **Optional Test Model**:  
  [`mistralai/Mistral-7B-Instruct-v0.2`](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.2) – tested for advanced instruction-following (in `test_mistral.py`)

  --

  ## 🛠️ Tech Stack

- **Frontend:** Gradio (interactive UI)
- **Backend:** Python, dotenv, logging, requests
- **API:** Tavily (live web search and media)

--

## 🌱 Future Enhancements

### 🌥️ Emotion Garden:
- Planning to track **emotion trends over time**.
- If a user’s emotional responses frequently trend negative (e.g., sadness or anxiety), the system will:
  - Prompt them gently: *“Would you like to talk to a no-judgment support bot?”*
  - Offer an opt-in, emotionally safe **chat feature for support**.

### 🤝 No-Judgment Chat Bot
- For users expressing **sadness or distress**, a companion chat interface will ask:  
  > “Would you like to talk about how you’re feeling?”
- This aims to create a **compassionate, stigma-free space** for emotional expression.

### 🔍 Tavily Integration
- The **Tavily API** enables live search for:
  - Nearby **gyms**
  - Local **grocery stores**
  - **Videos or GIFs of workouts** to help ensure proper form
  - Quick answers to wellness-related questions
- Helps users connect with **real-world wellness resources** based on their input.

### 🖼️ Image Generation
- Exploring image generation for:
  - Visualizing **custom meal bowls** based on generated recipes
  - Adding a creative layer so users can “see” their personalized meal plan
- Could be implemented using **Stable Diffusion** or tools from **Hugging Face**.

Thank You. Let’s keep learning and growing together!

