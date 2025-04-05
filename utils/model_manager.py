from transformers import pipeline, AutoModelForSeq2SeqLM, AutoTokenizer
import torch
from config import MODEL_CONFIG, HUGGINGFACE_API_KEY
import os
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ModelManager:
    def __init__(self):
        self.text_generation_model = None
        self.text_generation_tokenizer = None
        self.emotion_classifier = None
        try:
            self._initialize_models()
        except Exception as e:
            logger.error(f"Error initializing models: {str(e)}")
            raise

    def _initialize_models(self):
        try:
            # Initialize text generation model
            logger.info("Initializing text generation model...")
            model_config = MODEL_CONFIG["text_generation"]
            self.text_generation_tokenizer = AutoTokenizer.from_pretrained(
                model_config["model_name"],
                use_auth_token=HUGGINGFACE_API_KEY
            )
            self.text_generation_model = AutoModelForSeq2SeqLM.from_pretrained(
                model_config["model_name"],
                use_auth_token=HUGGINGFACE_API_KEY
            )
            logger.info("Text generation model initialized successfully")

            # Initialize emotion detection model
            logger.info("Initializing emotion detection model...")
            emotion_config = MODEL_CONFIG["emotion_detection"]
            self.emotion_classifier = pipeline(
                "text-classification",
                model=emotion_config["model_name"],
                return_all_scores=emotion_config["return_all_scores"],
                use_auth_token=HUGGINGFACE_API_KEY
            )
            logger.info("Emotion detection model initialized successfully")
        except Exception as e:
            logger.error(f"Error in model initialization: {str(e)}")
            raise

    def generate_text(self, prompt, max_length=None, temperature=None):
        try:
            logger.info(f"Generating text for prompt: {prompt[:100]}...")
            model_config = MODEL_CONFIG["text_generation"]
            
            # Use provided parameters or fall back to config
            max_length = max_length or model_config["max_length"]
            temperature = temperature or model_config["temperature"]
            
            inputs = self.text_generation_tokenizer(
                prompt,
                return_tensors="pt",
                max_length=max_length,
                truncation=True,
                padding=True
            )
            
            with torch.no_grad():
                outputs = self.text_generation_model.generate(
                    **inputs,
                    max_length=max_length,
                    temperature=temperature,
                    num_return_sequences=1,
                    do_sample=True,
                    top_k=model_config.get("top_k", 50),
                    top_p=model_config.get("top_p", 0.95),
                    repetition_penalty=model_config.get("repetition_penalty", 1.2),
                    no_repeat_ngram_size=3
                )
            
            generated_text = self.text_generation_tokenizer.decode(outputs[0], skip_special_tokens=True)
            
            # Post-process the generated text
            generated_text = self._format_response(generated_text)
            
            logger.info("Text generation completed successfully")
            return generated_text
        except Exception as e:
            logger.error(f"Error in text generation: {str(e)}")
            return f"Error generating response: {str(e)}"

    def _format_response(self, text):
        # Add proper spacing and formatting
        sections = text.split('\n\n')
        formatted_sections = []
        
        for section in sections:
            if section.strip():
                # Add bullet points for lists
                if any(line.startswith('-') for line in section.split('\n')):
                    lines = section.split('\n')
                    formatted_lines = []
                    for line in lines:
                        if line.strip().startswith('-'):
                            formatted_lines.append(f"• {line.strip()[1:].strip()}")
                        else:
                            formatted_lines.append(line)
                    section = '\n'.join(formatted_lines)
                
                formatted_sections.append(section)
        
        return '\n\n'.join(formatted_sections)

    def detect_emotion(self, text):
        try:
            logger.info(f"Detecting emotion for text: {text[:100]}...")
            results = self.emotion_classifier(text)
            logger.info("Emotion detection completed successfully")
            return results[0]
        except Exception as e:
            logger.error(f"Error in emotion detection: {str(e)}")
            return [{"label": "error", "score": 0.0}]

    def format_prompt(self, template_path, **kwargs):
        try:
            logger.info(f"Formatting prompt from template: {template_path}")
            with open(template_path, 'r') as f:
                template = f.read()
            formatted_prompt = template.format(**kwargs)
            logger.info("Prompt formatting completed successfully")
            return formatted_prompt
        except Exception as e:
            logger.error(f"Error formatting prompt: {str(e)}")
            return "Error: Could not format prompt" 