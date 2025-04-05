from transformers import pipeline
import json

class EmotionDetector:
    def __init__(self):
        self.classifier = pipeline(
            "text-classification",
            model="j-hartmann/emotion-english-distilroberta-base",
            return_all_scores=True
        )
        
    def detect_emotion(self, text):
        results = self.classifier(text)
        emotions = results[0]
        
        # Get the top emotion
        top_emotion = max(emotions, key=lambda x: x['score'])
        
        return {
            'emotion': top_emotion['label'],
            'confidence': top_emotion['score'],
            'all_emotions': emotions
        }
    
    def get_garden_element(self, emotion):
        # Map emotions to garden elements
        garden_map = {
            'joy': '🌻',  # Sunflower
            'sadness': '🌧',  # Rain cloud
            'anger': '🔥',  # Fire
            'fear': '🌪',  # Tornado
            'surprise': '🌈',  # Rainbow
            'disgust': '🌱',  # Sprout
            'neutral': '🌳'  # Tree
        }
        return garden_map.get(emotion.lower(), '🌱') 